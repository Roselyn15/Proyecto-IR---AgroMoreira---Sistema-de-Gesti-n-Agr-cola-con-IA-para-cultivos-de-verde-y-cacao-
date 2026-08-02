# Rubrica de evaluacion experta a ciegas

Proyecto: AgriMoreira - Sistema de Gestion Agricola con IA
Enfoque empirico: Enfoque 1 (Calidad de RF humanos vs. LLM)
Integrante responsable: Escudero Plaza Maria del Rosario
Version: 2.0

## Procedimiento

1. Cada evaluador recibe los dos conjuntos de RF mezclados y anonimizados
   (Conjunto A = LLM, Conjunto B = humanos) sin saber cual es cual.
2. Cada RF se puntua de 1 a 5 en cada una de las cinco dimensiones siguientes.
3. Las puntuaciones se registran en la plantilla `hoja_evaluacion_a_ciegas.csv`.
4. Se requiere un minimo de 3 evaluadores independientes (5 recomendado).

## Dimensiones (escala 1-5)

### D1. Completitud
- 5 = El RF cubre totalmente la necesidad identificada en la fuente, sin
  informacion faltante para su implementacion.
- 4 = Cubre casi toda la necesidad; falta un detalle menor.
- 3 = Cubre parcialmente la necesidad; falta informacion relevante.
- 2 = Cubre una fraccion pequena de la necesidad.
- 1 = No cubre la necesidad o es irrelevante respecto de la fuente.

### D2. Ausencia de ambiguedad
- 5 = El RF tiene una unica interpretacion posible y terminos precisos.
- 4 = Una unica interpretacion, con un termino levemente impreciso.
- 3 = Dos interpretaciones plausibles.
- 2 = Varias interpretaciones posibles; requiere aclaracion del autor.
- 1 = Imposible de interpretar de forma no ambigua.

### D3. Verificabilidad
- 5 = Existe un procedimiento de verificacion claro y medible para el RF.
- 4 = El procedimiento es claro pero parcialmente subjetivo.
- 3 = Existe una idea de verificacion sin procedimiento concreto.
- 2 = Solo verificacion subjetiva.
- 1 = No es posible verificar el RF con los medios descritos.

### D4. Correccion respecto de la fuente
- 5 = Todo el contenido del RF esta respaldado por la evidencia fuente
  (transcripcion), sin inventos ni contradicciones.
- 4 = Respaldo completo con un detalle menor sin soporte explicito.
- 3 = Parte del RF no se deriva de la fuente.
- 2 = La mayor parte del RF no se deriva de la fuente.
- 1 = El RF contradice la fuente o inventa contenido sin respaldo.

### D5. Consistencia interna
- 5 = El RF no contradice ningun otro RF del mismo conjunto y usa terminologia
  uniforme.
- 4 = Sin contradicciones, con una inconsistencia menor de terminologia.
- 3 = Una contradiccion o inconsistencia relevante dentro del conjunto.
- 2 = Varias contradicciones o inconsistencias.
- 1 = El RF es incompatible con el resto del conjunto.

## Calculo posterior (ver scripts_analisis/)

- Acuerdo inter-evaluador: kappa de Cohen (por pares) y kappa de Fleiss
  (conjunto completo).
- Comparacion de medias entre conjuntos: t pareada o Wilcoxon segun
  normalidad (Shapiro-Wilk).
- Tamano del efecto: d de Cohen o delta de Cliff.
- Correccion por comparaciones multiples (Bonferroni).
