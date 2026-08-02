# Resultados - Enfoque 1 (Calidad de RF humanos vs. LLM)

Proyecto: AgriMoreira - Sistema de Gestion Agricola con IA
Integrante responsable: Escudero Plaza Maria del Rosario
Estado: estructura preparada; los datos se incorporan tras ejecutar el
experimento (Semana 12) y la segunda ronda de campo.

## Estructura de la carpeta

| Archivo | Descripcion | Estado |
|---|---|---|
| `datos_crudos.csv` | Datos crudos de la evaluacion a ciegas (plantilla) | Vacio (plantilla) |
| `datos_procesados.csv` | Puntuaciones procesadas por RF y dimension (entrada de `scripts_analisis/analisis_ef1.py`) | Vacio (plantilla) |
| `tabla_hipotesis.csv` | Tabla de resultados de hipotesis (generada por el script) | Generado por script |
| `conjunto_a_llm.csv` | Conjunto A: RF producidos por el LLM | Vacio (pendiente ejecucion) |
| `conjunto_b_ers.csv` | Conjunto B: RF humanos tomados del ERS (RF-01 a RF-16 segun matriz de trazabilidad) | Vacio (pendiente consolidacion ERS) |
| `figuras/` | Figuras en PNG y en formato vectorial (generadas por el script) | Generado por script |

## Columnas de `datos_procesados.csv`

```
conjunto;id_rf;evaluador;completitud;ausencia_ambiguedad;verificabilidad;correccion_fuente;consistencia_interna
```

- `conjunto`: A (LLM) o B (humano).
- `id_rf`: identificador del requisito dentro de su conjunto.
- `evaluador`: codigo del evaluador experto (E1, E2, ...).
- cinco columnas restantes: puntuacion 1-5 por dimension (rubrica).

## Reproducibilidad

Todas las tablas y figuras del manuscrito se producen con:

```
python 06_Experimento/scripts_analisis/analisis_ef1.py \
  --csv 06_Experimento/resultados/datos_procesados.csv \
  --out 06_Experimento/resultados/
```

Ninguna tabla ni figura del manuscrito se produce manualmente.
