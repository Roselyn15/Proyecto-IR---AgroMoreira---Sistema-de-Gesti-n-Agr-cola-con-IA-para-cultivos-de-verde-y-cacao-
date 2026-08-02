# AgroMoreira — Sistema de Gestión Agrícola con Inteligencia Artificial

Sistema de Gestión Agrícola con Inteligencia Artificial desarrollado para **Agrícola Moreira**, orientado a la administración y monitoreo de cultivos de **cacao** y **plátano verde**.

Este proyecto fue desarrollado como parte del **Proyecto Integrador de la asignatura Ingeniería de Requerimientos [20303]** de la **Universidad Técnica Estatal de Quevedo (UTEQ)**.

---

# Tabla de Contenidos

- [Resumen del dominio](#resumen-del-dominio)
- [Equipo de desarrollo](#equipo-de-desarrollo)
- [Enlaces del proyecto](#enlaces-del-proyecto)
- [Documentación del proyecto](#documentación-del-proyecto)
- [Reproducción del proyecto](#reproducción-del-proyecto)
- [Estructura del repositorio](#estructura-del-repositorio)
- [Citación](#citación)
- [Integridad del repositorio](#integridad-del-repositorio)
- [Licencia](#licencia)

---

# Resumen del dominio

Agrícola Moreira administra lotes destinados a la producción de **cacao** y **plátano verde** en la provincia de **Manabí, Ecuador**.

**AgriMoreira** centraliza la información de los cultivos mediante una plataforma que permite:

- Gestión de productores y fincas.
- Administración de lotes agrícolas.
- Registro de siembras y cosechas.
- Asignación de actividades al personal de campo.
- Control de inventario de insumos agrícolas.
- Seguimiento del estado fenológico de los cultivos.
- Registro de incidencias, plagas y enfermedades.
- Generación de recomendaciones mediante Inteligencia Artificial para apoyar la toma de decisiones.

---

# Equipo de desarrollo

| Integrante | Rol | Correo institucional |
|------------|-----|----------------------|
| Robinson Espinoza Jeanpierre | Analista Líder / Ingeniería de Requerimientos | jrobisone@uteq.edu.ec |
| Calle Delgado Kamila Anabella | Analista de Requerimientos | kcalled@uteq.edu.ec |
| Arteaga Álava Danela Dayana | Diseño y Modelado UML | darteagaa@uteq.edu.ec |
| Escudero Plaza María del Rosario | Investigación Experimental y Análisis Estadístico | mescuderop@uteq.edu.ec |
| Sánchez Centeno Roselyn Andreina | Gestión del Repositorio, Infraestructura y DevOps | rsanchezc4@uteq.edu.ec |
| Mgs. Gleiston Ciceron Guerrero Ulloa | Docente Supervisor | gguerrero@uteq.edu.ec |

---

# Enlaces del proyecto

| Recurso | Enlace |
|---|---|
| ERS/SRS completo (PDF) | [01_ERS/ERS_SRS_2A_v1.0.pdf](./01_ERS/ERS_SRS_2A_v1.0.pdf) |
| MVP (código fuente) | [05_MVP/](./05_MVP/) |
| Registro previo del protocolo experimental (OSF) | [osf.io/7cvhy](https://osf.io/7cvhy) |
| Conjunto de datos (Zenodo) | *Pendiente de depósito — se publicará con la Entrega 4 (2B), siguiendo los principios FAIR* |

---

# Documentación del proyecto

| Documento | Ubicación |
|------------|-----------|
| Especificación de Requerimientos de Software (ERS/SRS) | `01_ERS/` |
| Evidencias del levantamiento de información | `02_Evidencias/` |
| Modelado UML y Mockups | `03_Modelado/` |
| Matriz de Trazabilidad | `04_Trazabilidad/` |
| MVP del sistema | `05_MVP/` |
| Protocolo y resultados experimentales | `06_Experimento/` |
| Manuscrito científico | `07_Publicacion/` |

---

# Reproducción del proyecto

## Clonar el repositorio

```bash
git clone https://github.com/Roselyn15/Proyecto-IR---AgroMoreira---Sistema-de-Gesti-n-Agr-cola-con-IA-para-cultivos-de-verde-y-cacao-.git
```

## Ingresar al proyecto

```bash
cd Proyecto-IR---AgroMoreira---Sistema-de-Gesti-n-Agr-cola-con-IA-para-cultivos-de-verde-y-cacao-
```

## Ejecutar el MVP

Diríjase a la carpeta: 05.MVP/ y siga las instrucciones descritas en el archivo `README.md` correspondiente para ejecutar la aplicación. El MVP no requiere instalación: se abre directamente en cualquier navegador.

## Reproducir el análisis experimental

1. Ubíquese en la carpeta `06_Experimento/`.
2. Instale las dependencias indicadas en `06_Experimento/scripts_analisis/` (Python o R, según corresponda).
3. Los datos crudos recolectados están en `06_Experimento/resultados/`.
4. Ejecute los scripts de `06_Experimento/scripts_analisis/` en orden — reproducen exactamente las tablas y figuras reportadas en el manuscrito a partir de los datos crudos.
5. El protocolo completo (preguntas de investigación, proposiciones del estudio, plan de análisis) está en `06_Experimento/protocolo.pdf`, registrado previamente en OSF: https://osf.io/7cvhy

---

# Estructura del repositorio

```text
AgriMoreira/
│
├── README.md
├── LICENSE
├── CITATION.cff
├── CHANGELOG.md
├── checksums.sha256
│
├── 01_ERS/
│   └── Especificación de Requerimientos de Software
│
├── 02_Evidencias/
│   └── Evidencias del levantamiento de información
│
├── 03_Modelado/
│   └── Diagramas UML y Mockups
│
├── 04_Trazabilidad/
│   └── Matriz de Trazabilidad
│
├── 05_MVP/
│   └── Prototipo funcional
│
├── 06_Experimento/
│   └── Protocolo experimental, scripts y resultados
│
└── 07_Publicacion/
    └── Manuscrito científico y material para publicación
```

---

# Citación

La forma recomendada de citar este repositorio se encuentra en el archivo:  CITATION.cff 
---

# Integridad del repositorio
Las huellas digitales SHA-256 de los archivos multimedia y documentos se encuentran en:
checksums.sha256

Para verificar la integridad del repositorio, ejecute:

```bash
sha256sum -c checksums.sha256
```

---

# Licencia

Este repositorio utiliza dos licencias según el tipo de contenido:

- **Código fuente del MVP (`05_MVP/`)**: Licencia **MIT**.
- **Documentación, ERS, evidencias, modelado, trazabilidad, experimento y publicación**: Licencia **Creative Commons Attribution 4.0 International (CC BY 4.0)**.

Consulte el archivo `LICENSE` para conocer los términos completos de ambas licencias.
