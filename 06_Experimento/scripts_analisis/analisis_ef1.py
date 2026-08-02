#!/usr/bin/env python3
"""
analisis_ef1.py - Analisis estadistico del Enfoque 1 (Calidad de RF humanos vs. LLM)

Proyecto: AgriMoreira - Sistema de Gestion Agricola con IA
Integrante responsable: Escudero Plaza Maria del Rosario
Reproduce exactamente las tablas y figuras del manuscrito a partir de los
datos crudos en 06_Experimento/resultados/.

Dependencias (ver requirements.txt):
    pandas, numpy, scipy, statsmodels, matplotlib, seaborn

Uso:
    python analisis_ef1.py                     # datos en rutas por defecto
    python analisis_ef1.py --csv ruta.csv      # CSV de puntuaciones
    python analisis_ef1.py --out directorio    # salida de tablas/figuras
"""

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats


def cargar_puntuaciones(ruta: Path) -> pd.DataFrame:
    """Carga el CSV de puntuaciones por RF, dimension y evaluador."""
    df = pd.read_csv(ruta, sep=";")
    requeridas = {
        "conjunto",
        "id_rf",
        "evaluador",
        "completitud",
        "ausencia_ambiguedad",
        "verificabilidad",
        "correccion_fuente",
        "consistencia_interna",
    }
    faltantes = requeridas - set(df.columns)
    if faltantes:
        raise ValueError(f"Columnas faltantes en {ruta}: {sorted(faltantes)}")
    return df


def test_normalidad_shapiro_wilk(diferencias: np.ndarray) -> dict:
    """Prueba de normalidad Shapiro-Wilk sobre las diferencias apareadas."""
    stat, p = stats.shapiro(diferencias)
    return {"estadistico": float(stat), "valor_p": float(p),
            "es_normal": bool(p > 0.05)}


def prueba_apareada(a: np.ndarray, b: np.ndarray, normal: bool) -> dict:
    """t pareada si los datos son normales, Wilcoxon en caso contrario."""
    if normal:
        stat, p = stats.ttest_rel(a, b)
        prueba = "t_pareada"
    else:
        stat, p = stats.wilcoxon(a, b)
        prueba = "wilcoxon"
    return {"prueba": prueba, "estadistico": float(stat), "valor_p": float(p)}


def d_cohen(a: np.ndarray, b: np.ndarray) -> float:
    """Tamano del efecto d de Cohen para muestras apareadas."""
    d = np.asarray(a, dtype=float) - np.asarray(b, dtype=float)
    n = len(d)
    media = np.mean(d)
    # desviacion de las diferencias; denominator estandar (apareada)
    var = np.var(d, ddof=1)
    if var == 0:
        return 0.0
    denom = np.sqrt(var) / np.sqrt(n)
    return float(media / denom) if denom > 0 else 0.0


def delta_cliff(a: np.ndarray, b: np.ndarray) -> float:
    """Tamano del efecto delta de Cliff para datos no normales."""
    x = np.asarray(a, dtype=float)
    y = np.asarray(b, dtype=float)
    n = len(x)
    m = len(y)
    if n == 0 or m == 0:
        return 0.0
    favor = 0.0
    atado = 0.0
    for xi in x:
        favor += np.sum(y < xi)
        atado += np.sum(y == xi)
    delta = (favor - (n * m - favor - atado)) / (n * m)
    return float(delta)


def kappa_cohen(y1: np.ndarray, y2: np.ndarray) -> float:
    """Kappa de Cohen entre dos evaluadores (categorias 1..5)."""
    n = len(y1)
    if n == 0:
        return 0.0
    po = np.mean(y1 == y2)
    p1 = np.bincount(y1.astype(int), minlength=6) / n
    p2 = np.bincount(y2.astype(int), minlength=6) / n
    pe = np.sum(p1 * p2)
    if pe == 1.0:
        return 0.0
    return float((po - pe) / (1.0 - pe))


def kappa_fleiss(ratings: np.ndarray, k: int = 5) -> float:
    """Kappa de Fleiss para n sujetos y r evaluadores con k categorias."""
    n, r = ratings.shape
    if n == 0:
        return 0.0
    counts = np.zeros((n, k + 1))
    for i in range(n):
        counts[i] = np.bincount(ratings[i].astype(int), minlength=k + 1)
    pj = counts.sum(axis=0) / (n * r)
    pe = np.sum(pj ** 2)
    pi = (counts ** 2).sum(axis=1)
    po = (pi.sum() - n * r) / (n * r * (r - 1))
    if pe == 1.0:
        return 0.0
    return float((po - pe) / (1.0 - pe))


def potencia_estadistica(d: float, n: int, alpha: float = 0.05) -> float:
    """Potencia (1 - beta) para t pareada dado d y n (aproximacion normal)."""
    from statsmodels.stats.power import TTestPower
    analysis = TTestPower()
    return float(analysis.solve_power(
        effect_size=d, nobs=n, alpha=alpha, power=None, alternative="two-sided"))


def analizar(df: pd.DataFrame) -> dict:
    """Ejecuta el plan completo de analisis por dimension."""
    resultados = {"normalidad": {}, "hipotesis": {}, "tamano_efecto": {},
                  "acuerdo_inter_evaluador": {}, "potencia": {}}
    dimensiones = ["completitud", "ausencia_ambiguedad", "verificabilidad",
                   "correccion_fuente", "consistencia_interna"]

    conjuntos = sorted(df["conjunto"].unique())
    if len(conjuntos) != 2:
        print(f"[aviso] Se esperaban 2 conjuntos (A y B), se encontraron: {conjuntos}")

    for dim in dimensiones:
        a = df.loc[df["conjunto"] == "A", dim].to_numpy(dtype=float)
        b = df.loc[df["conjunto"] == "B", dim].to_numpy(dtype=float)
        if len(a) != len(b):
            print(f"[aviso] Dimension {dim}: tamano A={len(a)} != B={len(b)}")
        n = min(len(a), len(b))
        if n == 0:
            continue
        norm = test_normalidad_shapiro_wilk(a[:n] - b[:n])
        resultados["normalidad"][dim] = norm
        hip = prueba_apareada(a[:n], b[:n], normal=norm["es_normal"])
        resultados["hipotesis"][dim] = hip
        if norm["es_normal"]:
            efecto = {"tipo": "cohen_d", "valor": d_cohen(a[:n], b[:n])}
        else:
            efecto = {"tipo": "cliff_delta", "valor": delta_cliff(a[:n], b[:n])}
        resultados["tamano_efecto"][dim] = efecto
        resultados["potencia"][dim] = {
            "potencia": potencia_estadistica(abs(efecto["valor"]), n)}

    # Acuerdo inter-evaluador (kappa de Fleiss y Cohen)
    evaluadores = sorted(df["evaluador"].unique())
    # matriz sujeto x evaluador para cada dimension con la puntuacion cruda
    ratings = {}
    for dim in dimensiones:
        pivot = df.pivot_table(index="id_rf", columns="evaluador",
                               values=dim, aggfunc="mean")
        mat = pivot.to_numpy()
        ratings[dim] = {"fleiss": kappa_fleiss(mat),
                        "cohen_pares": {}}
        if len(evaluadores) >= 2:
            for i in range(len(evaluadores)):
                for j in range(i + 1, len(evaluadores)):
                    col_i = pivot[evaluadores[i]].to_numpy()
                    col_j = pivot[evaluadores[j]].to_numpy()
                    mask = ~(np.isnan(col_i) | np.isnan(col_j))
                    if mask.sum() >= 2:
                        ratings[dim]["cohen_pares"][
                            f"{evaluadores[i]}-{evaluadores[j]}"] = kappa_cohen(
                                col_i[mask], col_j[mask])
    resultados["acuerdo_inter_evaluador"] = ratings
    return resultados


def guardar_tablas(resultados: dict, out: Path) -> None:
    """Guarda las tablas de resultados en CSV."""
    out.mkdir(parents=True, exist_ok=True)
    filas = []
    for dim in resultados["hipotesis"]:
        filas.append({
            "dimension": dim,
            "normalidad_estadistico": resultados["normalidad"][dim]["estadistico"],
            "normalidad_p": resultados["normalidad"][dim]["valor_p"],
            "prueba": resultados["hipotesis"][dim]["prueba"],
            "estadistico": resultados["hipotesis"][dim]["estadistico"],
            "valor_p": resultados["hipotesis"][dim]["valor_p"],
            "tamano_efecto_tipo": resultados["tamano_efecto"][dim]["tipo"],
            "tamano_efecto": resultados["tamano_efecto"][dim]["valor"],
            "potencia": resultados["potencia"][dim]["potencia"],
        })
    pd.DataFrame(filas).to_csv(out / "tabla_hipotesis.csv", index=False)
    print(f"[ok] Tabla de hipotesis guardada en {out / 'tabla_hipotesis.csv'}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", default="resultados/datos_procesados.csv")
    parser.add_argument("--out", default="resultados/")
    args = parser.parse_args()

    ruta_csv = Path(args.csv)
    if not ruta_csv.exists():
        print(f"[error] No existe {ruta_csv}. Genere primero los datos crudos "
              f"y el archivo de puntuaciones procesadas.")
        return 1

    df = cargar_puntuaciones(ruta_csv)
    resultados = analizar(df)
    guardar_tablas(resultados, Path(args.out))
    print(json.dumps(resultados, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
