# README_dataset.md - Conjunto de datos AgriMoreira (Enfoque 1)

Paquete de datos para deposito en Zenodo (https://zenodo.org) al momento del
envio del manuscrito, siguiendo los principios FAIR [1].
Licencia: Creative Commons Atribucion 4.0 Internacional (CC BY 4.0).

## Cita del dataset (instrucciones)

Formato recomendado para citar el dataset (completar el DOI asignado por Zenodo):

> Escudero Plaza, M. R. (2026). AgriMoreira - Calidad de requisitos funcionales
> humanos frente a LLM: conjunto de datos anonimizado [Data set]. Zenodo.
> https://doi.org/10.5281/zenodo.XXXXXXX

El DOI se asigna automaticamente al publicar en Zenodo. Al citar, indicar la
version del dataset (v1.0.0) y la fecha de publicacion. Para el software de
analisis, seguir los principios de citacion de software [2].

## Diccionario de datos

### 1. Transcripciones anonimizadas de entrevistas (`transcripciones/`)
Archivos TXT (y JSON estructurado) con codigo de participante e identificador
de evidencia (EV-XX). Sin nombres propios, sin cargos que identifiquen de forma
univoca.

| Campo | Tipo | Descripcion |
|---|---|---|
| codigo_participante | string | Codigo anonimizado (Entr-01, Entr-03, ...) |
| rol | string | Rol en la finca (administrador, jornalero, ...) |
| fecha | date (ISO 8601) | Fecha de la entrevista |
| id_evidencia | string | Identificador de evidencia (EV-XX) |
| texto | string | Contenido de la transcripcion anonimizada |

### 2. Respuestas del cuestionario (`cuestionario/`)
Archivo CSV: `2026_07_25_respuestas_2A.csv` (datos crudos anonimizados).

| Campo | Tipo | Descripcion |
|---|---|---|
| rol | string | Rol dentro de la actividad agricola |
| rango_edad | string | Rango de edad |
| anos_experiencia | string | Anos de experiencia |
| control_cultivos | string | Como lleva el control de cultivos y cosechas |
| control_inventario | string | Como controla el inventario de insumos |
| organizacion_likert | entero (1-5) | Que tan organizado considera su registro |
| dificultades | string | Principales dificultades |
| informacion_frecuente | string | Informacion que necesita registrar con mayor frecuencia |
| control_gastos | string | Necesita control de gastos e ingresos (Si/No) |

### 3. Corpus etiquetado de RF/RNF (`requisitos/`)
Archivos JSON con los requisitos funcionales (RF) y no funcionales (RNF)
etiquetados del sistema AgriMoreira, segun la matriz de trazabilidad.

| Campo | Tipo | Descripcion |
|---|---|---|
| id_rf | string | Identificador (RF-01, ..., RNF-xx) |
| nombre | string | Nombre del requisito |
| descripcion | string | Descripcion |
| actor | string | Actor(es) |
| prioridad | string | Prioridad MoSCoW |
| id_evidencia | string | Evidencia que respalda (EV-XX) |
| tipo | string | RF o RNF |

### 4. Matriz de trazabilidad (`trazabilidad/`)
Archivo CSV con la matriz completa (TR-01 a TR-42): ley, articulo, objetivo,
stakeholder, ID-EV, ID-RF/RNF/RD, tipo, ID-CU, ID-HU, ID-CA, componente y
mockup.

### 5. Consignas y respuestas de los LLM (`prompts_llm/`)
Enfoque 1: archivo Markdown con el prompt exacto, modelo, temperatura, top-p,
semilla, fecha y hora de la consulta, y el Conjunto A de RF producidos por el
LLM en CSV.

### 6. Scripts de analisis (`scripts_analisis/`)
Scripts en Python que reproducen las tablas y figuras del manuscrito a partir
de los datos crudos. Ver `requirements.txt`.

### 7. Protocolo experimental (`protocolo/`)
Protocolo completo (PICOC, hipotesis, variables, diseno, instrumentos, plan de
analisis) y comprobante de registro OSF.

## Datos restringidos (NO se publican)

- Consentimientos originales, videos, audios y documentos originales de la
  organizacion: permanecen en la zona restringida.
- Tabla de correspondencia entre codigos de participante y personas reales:
  bajo custodia del docente responsable.
- Retencion: los datos crudos restringidos se conservan 24 meses y luego se
  eliminan de forma segura con acta firmada.

## Referencias

[1] Wilkinson, M. D., et al. (2016). The FAIR Guiding Principles for scientific
    data management and stewardship. Scientific Data, 3, 160018.
[2] Smith, A. M., et al. (2016). Software citation principles. PeerJ Computer
    Science, 2, e86.
