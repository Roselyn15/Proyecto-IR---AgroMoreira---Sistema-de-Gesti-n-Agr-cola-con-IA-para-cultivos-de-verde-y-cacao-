# Prompt del experimento - Enfoque 1 (Calidad de RF humanos vs. LLM)

Proyecto: AgriMoreira - Sistema de Gestion Agricola con IA
Integrante responsable: Escudero Plaza Maria del Rosario
Carpeta: `06_Experimento/prompts_llm/`
Estado: plantilla de registro; la ejecucion queda registrada con su fecha y
hora en el bloque "Bitacora de consulta" al momento de correr el LLM.

## Material fuente entregado al LLM

- `02_Evidencias/Transcripciones/2026-06-20 entrevista administrador entr-01.txt`
  (EV-01, transcripcion anonimizada, sin nombres propios).

El LLM NO recibe ningun otro contexto, ni el ERS del equipo, ni la matriz de
trazabilidad. Esto garantiza que el Conjunto A (LLM) se produce
independientemente del Conjunto B (humano).

## Consigna exacta (verbatim de la guia)

> A partir del siguiente material fuente, redacta requisitos funcionales del
> sistema descrito, con los ocho atributos de la plantilla del silabo.

Los ocho atributos de la plantilla del silabo son:

1. Identificador
2. Nombre
3. Descripcion
4. Actor(es)
5. Prioridad (MoSCoW)
6. Precondiciones
7. Flujo principal
8. Postcondiciones

## Parametros de la consulta (a registrar en la ejecucion)

| Parametro | Valor registrado |
|---|---|
| Modelo | gpt-4o-2024-08-06 (o claude-3-5-sonnet-20241022) |
| Temperatura | 0.0 |
| top-p | 1.0 |
| top-k | N/A (no aplica a los modelos usados) |
| Semilla | 42 |
| Fecha de la consulta | [registrar fecha ISO 8601 en la ejecucion] |
| Hora de la consulta | [registrar hora local en la ejecucion] |

## Bitacora de consulta

| Fecha (ISO 8601) | Hora | Modelo | Temp. | top-p | Semilla | Conjunto producido | Archivo de salida |
|---|---|---|---|---|---|---|---|
| (pendiente) | (pendiente) | gpt-4o-2024-08-06 | 0.0 | 1.0 | 42 | A | `06_Experimento/resultados/conjunto_a_llm.csv` |

## Salida esperada

El LLM produce su propio conjunto de requisitos funcionales (Conjunto A), que
se guarda en `06_Experimento/resultados/` y se aparea con el Conjunto B (los RF
del ERS, RF-01 a RF-16 segun la matriz de trazabilidad) para la evaluacion a
ciegas con la rubrica de cinco dimensiones.

## Cita de referencia

Open Science Framework: https://osf.io (registro previo del protocolo).
