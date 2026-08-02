# Registro previo en el OSF (preregistro)

Proyecto: AgriMoreira - Sistema de Gestion Agricola con IA
Integrante responsable: Escudero Plaza Maria del Rosario
Plataforma: https://osf.io
Estado: texto listo para pegar en el formulario de preregistro; el registro
debe completarse en la semana 11, con fecha anterior a la ejecucion del
experimento. El comprobante (URL persistente + time stamp) se guardara como
`06_Experimento/osf_registration.pdf`.

## Paso a paso

1. Crear una cuenta en https://osf.io (o iniciar sesion).
2. Crear un proyecto nuevo llamado "AgriMoreira - Enfoque 1 - RF humanos vs LLM".
3. En el proyecto, ir a **Registrations > New Registration** y elegir la
   plantilla de preregistro **"OSF Preregistration"**.
4. Completar los campos con el texto de la seccion "Contenido del registro".
5. Enviar el registro. El sistema asigna una URL persistente
   (`https://osf.io/xxxxxxxx`) y registra la fecha/hora.
6. Descargar el comprobante y guardarlo como `06_Experimento/osf_registration.pdf`.

## Contenido del registro

### Titulo del estudio
Comparacion de la calidad de requisitos funcionales elicitados por analistas
humanos frente a los generados por un modelo de lenguaje (LLM) en un sistema
agricola con IA (Enfoque 1).

### Autores
Escudero Plaza Maria del Rosario (UTEQ), en representacion del equipo
AgriMoreira del Proyecto de Fin de Curso - Ingenieria de Requerimientos.

### Hipotesis
- H0: No existe diferencia estadisticamente significativa entre la puntuacion
  media de calidad de los RF humanos (Conjunto B) y la de los RF generados por
  LLM (Conjunto A) en cada dimension de calidad.
- H1: Existe una diferencia estadisticamente significativa entre ambas
  puntuaciones medias en la dimension.

Nivel de significancia: alpha = 0.05. Potencia: 1 - beta = 0.80.

### Variables
- Independiente: origen del conjunto de requisitos (A = LLM, B = equipo humano).
- Dependientes: puntuacion de calidad por dimension (1-5): completitud,
  ausencia de ambiguedad, verificabilidad, correccion respecto de la fuente,
  consistencia interna; y acuerdo inter-evaluador (kappa de Cohen y de Fleiss).
- De control: material fuente unico (transcripcion anonimizada EV-01),
  rubrica identica, evaluadores ciegos, parametros del LLM fijos.

### Diseno
Cuasi-experimento apareado. Conjunto A: RF producidos por el LLM (gpt-4o-2024-08-06,
temperatura 0.0, top-p 1.0, semilla 42) a partir del material fuente unico.
Conjunto B: RF humanos del ERS (RF-01 a RF-16 segun la matriz de trazabilidad).
Evaluacion a ciegas por un minimo de 3 evaluadores expertos independientes.

### Plan de analisis
1. Normalidad: Shapiro-Wilk sobre las diferencias apareadas.
2. Comparacion: t pareada (normales) o Wilcoxon (no normales).
3. Tamano del efecto: d de Cohen o delta de Cliff.
4. Correccion por comparaciones multiples (Bonferroni).
5. Acuerdo inter-evaluador: kappa de Cohen por pares y kappa de Fleiss.
6. Potencia estadistica previa (alpha 0.05, 1-beta 0.80).

### Materiales (archivos del repositorio)
- `06_Experimento/protocolo.tex` - protocolo experimental completo.
- `06_Experimento/instrumentos/` - guion v2.0, cuestionario v2.0, rubrica.
- `06_Experimento/prompts_llm/experimento_enf1_prompt.md` - consigna y parametros.
- `06_Experimento/scripts_analisis/analisis_ef1.py` - scripts de analisis.
- `02_Evidencias/Transcripciones/` - transcripciones anonimizadas (material fuente).

### Declaracion de datos y licencia
Los datos anonimizados se depositaran en Zenodo con licencia CC BY 4.0 siguiendo
los principios FAIR.
