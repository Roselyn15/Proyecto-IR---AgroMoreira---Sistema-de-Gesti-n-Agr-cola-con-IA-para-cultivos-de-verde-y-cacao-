# Metodología de Priorización — MoSCoW + Kano + WSJF

## Archivos en esta carpeta
- `priorizacion_moscow_kano.csv` — los 16 requisitos funcionales (RF-01 a RF-16) ya
  especificados en el ERS de la Entrega 2, priorizados con las tres técnicas exigidas por la
  Sección 5 de la guía de Entrega 3.

> **Nota de alcance:** la guía de Entrega 3 exige un mínimo de 25 RF en total (Sección 3.3).
> Esta priorización cubre por ahora los 16 RF ya validados con evidencia en la Entrega 2. Si
> el/la compañero(a) a cargo de la Sección 3 agrega nuevos RF para llegar al mínimo de 25, esas
> filas nuevas deben añadirse a este CSV siguiendo el mismo método descrito abajo — no renumerar
> ni reordenar las 16 filas existentes, ya que la matriz de trazabilidad referencia estos IDs.

## MoSCoW
Reutilizado directamente del ERS de la Entrega 2 (Tabla 5.2), donde cada RF ya estaba
justificado frente a las necesidades operativas reales de la finca. No se recalculó aquí.

## Modelo de Kano
Cada RF fue clasificado en una de tres categorías presentes en este proyecto (no se
identificaron requisitos *indiferentes* ni *de rechazo*):
- **Básica (must-be):** funcionalidad base esperada; su ausencia genera fuerte insatisfacción,
  pero su presencia no se percibe como un "plus" (ej.: login, registro de parcelas/cultivos).
- **Desempeño (lineal):** la satisfacción aumenta de forma aproximadamente lineal según qué tan
  bien esté implementada la funcionalidad (ej.: reportes, estadísticas, seguimiento de tareas).
- **Deleite (excitement):** supera la expectativa base; recibida explícitamente como novedad
  positiva por el administrador durante la entrevista de la Entrega 1B/2A (recomendaciones de
  IA, alertas automáticas de enfermedad).

## WSJF (Weighted Shortest Job First)
Fórmula (marco SAFe):

```
WSJF = Costo de Demora / Tamaño de la Tarea
Costo de Demora (CoD) = Valor de Negocio (VN) + Criticidad en el Tiempo (CT) + Reduccion de Riesgo / Habilitacion de Oportunidad (RR)
```

Cada componente se puntuó en una escala relativa de 1 a 9 (no en story points Fibonacci, ya que
en esta etapa el equipo aún no tiene datos de velocidad para normalizar):
- **VN (Valor de Negocio):** cuánto valora el administrador esta capacidad, con base en la
  entrevista (ej.: el registro de cosecha obtuvo la puntuación más alta — era su principal
  molestia).
- **CT (Criticidad en el Tiempo):** cuánto valor se pierde si se retrasa (ej.: el login es
  crítico en el tiempo porque todo el resto de módulos depende de él).
- **RR (Reducción de Riesgo / Habilitación de Oportunidad):** cuánto reduce este RF el riesgo
  del proyecto o habilita a otros RF (ej.: Gestión de Parcelas/Cultivos habilita casi todo lo
  demás).
- **Tamaño de la tarea:** estimación relativa del equipo del esfuerzo de implementación (no en
  horas — una escala gruesa de 1 a 8), usada como denominador para que los ítems pequeños de
  alto valor se prioricen sobre los grandes.

**Ranking obtenido (WSJF de mayor a menor):** RF-02, RF-03, RF-05 (empatados en 7.33) → RF-01
(7.0) → RF-07 (6.5) → RF-14 (6.33) → RF-10 (6.0) → RF-04 (5.67) → RF-08, RF-09 (empatados en
5.0) → RF-06, RF-16 (empatados en 4.2) → RF-12 (4.0) → RF-13 (3.67) → RF-11 (3.2) → RF-15 (1.75,
el más bajo — coherente con su clasificación Could Have / Deleite: alto valor pero el trabajo
de implementación más grande).

Este orden de WSJF da una recomendación de secuenciación basada en evidencia para el MVP
(Sección 6 de la guía de Entrega 3: el MVP debe cubrir ≥60% de los RF *Debe tener*) — el equipo
debería implementar desde el tope de este ranking hacia abajo al decidir qué RF *Debe tener*
entran primero al MVP.
