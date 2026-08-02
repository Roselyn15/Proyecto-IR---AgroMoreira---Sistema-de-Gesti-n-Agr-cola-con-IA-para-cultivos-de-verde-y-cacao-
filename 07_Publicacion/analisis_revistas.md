# Analisis de revistas objetivo (07_Publicacion/analisis_revistas.md)

Proyecto: AgriMoreira - Sistema de Gestion Agricola con IA
Enfoque empirico: Enfoque 1 (Calidad de RF humanos vs. LLM)
Integrante responsable: Escudero Plaza Maria del Rosario
Fecha de verificacion de metricas: 2026-08-01 (JCR publicado en junio de 2026, datos 2025/2024 segun la fuente de cada metrica)

Titulo del manuscrito (preliminar):
*"Comparacion de la calidad de requisitos funcionales elicitados por analistas humanos frente a los generados por un modelo de lenguaje (LLM) en un sistema agricola con IA"*

Resumen del manuscrito (preliminar):
Los modelos de lenguaje de gran escala (LLM) se estan integrando cada vez mas
en la fase de elicitacion de requisitos de la ingenieria de software. Sin
embargo, la evidencia empirica sobre la calidad de los requisitos funcionales
generados por un LLM frente a los elicitados por analistas humanos a partir de
un mismo material fuente es todavia limitada. En este trabajo se realiza un
cuasi-experimento apareado en el dominio agroindustrial ecuatoriano: un equipo
humano y un LLM (gpt-4o-2024-08-06) producen sendos conjuntos de requisitos
funcionales (minimo 25 cada uno) a partir de la misma transcripcion
anonimizada de una entrevista de campo del sistema AgriMoreira. Tres o mas
evaluadores expertos independientes puntuan a ciegas ambos conjuntos en cinco
dimensiones de calidad (completitud, ausencia de ambiguedad, verificabilidad,
correccion respecto de la fuente y consistencia interna). El acuerdo
inter-evaluador se mide con kappa de Cohen y de Fleiss; las medias se comparan
con t pareada o Wilcoxon segun normalidad, reportando el tamano del efecto
(d de Cohen o delta de Cliff) y el calculo de potencia previo
(alpha = 0.05, 1-beta = 0.80).

## Criterio de la guia (Seccion 6.4)

Se registran al menos dos candidatas por editorial (Springer Nature, Elsevier
e IEEE): una en modalidad de acceso abierto con APC y otra en modalidad por
suscripcion o hibrida sin cargo obligatorio para las personas autoras. La
decision final de envio se tomara en la semana 16 comparando la puntuacion de
la herramienta oficial de cada editorial, la coherencia tematica y la
viabilidad economica.

---

## 1. Springer Nature

### 1.1 Requirements Engineering (Springer London) - SIN cargo obligatorio (hibrida por suscripcion)

| Campo | Valor |
|---|---|
| Nombre completo | Requirements Engineering |
| Editorial | Springer Nature (Springer London) |
| ISSN | 0947-3602 / 1432-010X |
| Indexacion JCR | SCIE - Computer Science, Information Systems (Q2); Computer Science, Software Engineering (Q2) |
| Factor de impacto | 3.3 (2024, publicado en junio de 2026) |
| CiteScore (Scopus) | 9.0 |
| SJR | 0.798 |
| Modelo de acceso | Hibrida: por suscripcion (sin cargo para autores) o acceso abierto opcional |
| APC (si se elige OA) | ~2.780 USD (OpenAlex); tarifa oficial de la editorial a confirmar en la herramienta |
| Tiempo medio a primera decision | No publicado oficialmente; verificar en journalsuggester.springer.com |
| Tasa de aceptacion | No publicada oficialmente |
| Herramienta oficial | journalsuggester.springer.com |
| Justificacion de ajuste tematico | Revista especializada en elicitation, representacion y validacion de requisitos; alinea directamente con la pregunta de investigacion RQ1 (calidad de RF elicitados por humanos vs. LLM). Es la revista de referencia del area de ingenieria de requisitos. |

**Razon de candidatura sin cargo obligatorio:** publicar en modalidad de
suscripcion no genera APC; es la alternativa realista para un equipo de
pregrado sin financiamiento.

---

### 1.2 Empirical Software Engineering (Springer Netherlands) - CON APC

| Campo | Valor |
|---|---|
| Nombre completo | Empirical Software Engineering |
| Editorial | Springer Nature (Springer Netherlands) |
| ISSN | 1382-3256 / 1573-7616 |
| Indexacion JCR | SCIE - Computer Science, Software Engineering (Q2) |
| Factor de impacto | 3.4 (2025, publicado en junio de 2026) |
| CiteScore (Scopus) | 7.9 |
| SJR | 0.895 |
| Modelo de acceso | Hibrida: suscripcion o acceso abierto |
| APC (si se elige OA) | 2.890 USD (lista oficial de hibr... de Springer Nature 2026) |
| Tiempo medio a primera decision | No publicado oficialmente; verificar en journalsuggester.springer.com |
| Tasa de aceptacion | No publicada oficialmente |
| Herramienta oficial | journalsuggester.springer.com |
| Justificacion de ajuste tematico | Revista dedicada a la investigacion empirica en ingenieria de software, con guias de reporte de experimentos (Molleri, Petersen, Mendes) que nuestro protocolo sigue literalmente; es el destino natural de un cuasi-experimento como el Enfoque 1. |

---

## 2. Elsevier

### 2.1 Information and Software Technology (Elsevier BV) - SIN cargo obligatorio (hibrida por suscripcion)

| Campo | Valor |
|---|---|
| Nombre completo | Information and Software Technology |
| Editorial | Elsevier BV |
| ISSN | 0950-5849 / 1873-6025 |
| Indexacion JCR | SCIE - Computer Science, Software Engineering (Q1); Computer Science, Information Systems (Q2) |
| Factor de impacto | 4.6 (2025, publicado en junio de 2026) |
| CiteScore (Scopus) | 10.8 |
| SJR | 1.054 |
| Modelo de acceso | Hibrida: suscripcion (sin cargo para autores) o acceso abierto opcional |
| APC (si se elige OA) | 3.890 USD (ScienceDirect; algunas fuentes listan 3.350 USD) |
| Tiempo medio a primera decision | No publicado oficialmente; verificar en journalfinder.elsevier.com |
| Tasa de aceptacion | No publicada oficialmente |
| Herramienta oficial | journalfinder.elsevier.com |
| Justificacion de ajuste tematico | Publica estudios empiricos de ingenieria de software y de requisitos; su cuartil Q1 y su cobertura de metodos empiricos son compatibles con el alcance del manuscrito. |

---

### 2.2 Journal of Systems and Software (Elsevier Inc.) - CON APC

| Campo | Valor |
|---|---|
| Nombre completo | Journal of Systems and Software |
| Editorial | Elsevier Inc. |
| ISSN | 0164-1212 / 1873-1228 |
| Indexacion JCR | SCIE - Computer Science, Software Engineering (Q2 en 2026; Q1 en ediciones previas); Computer Science, Theory & Methods (Q2) |
| Factor de impacto | 3.8 (2025, publicado en junio de 2026) |
| CiteScore (Scopus) | 10.1 |
| SJR | 0.95 |
| Modelo de acceso | Hibrida: suscripcion o acceso abierto |
| APC (si se elige OA) | 3.670 USD (ScienceDirect; otras fuentes listan 3.560 USD) |
| Tiempo medio a primera decision | No publicado oficialmente; verificar en journalfinder.elsevier.com |
| Tasa de aceptacion | No publicada oficialmente |
| Herramienta oficial | journalfinder.elsevier.com |
| Justificacion de ajuste tematico | Cubre ingenieria de software y de sistemas con secciones frecuentes sobre requisitos y LLM; el articulo se enmarca en el alcance de "software systems engineering" que la revista declara. |

---

## 3. IEEE

### 3.1 IEEE Transactions on Software Engineering (IEEE Computer Society) - SIN cargo obligatorio (hibrida por suscripcion)

| Campo | Valor |
|---|---|
| Nombre completo | IEEE Transactions on Software Engineering (IEEE TSE) |
| Editorial | IEEE Computer Society |
| ISSN | 0098-5589 / 1939-3520 |
| Indexacion JCR | SCIE - Computer Science, Software Engineering (Q1); Engineering, Electrical & Electronic (Q1) |
| Factor de impacto | 6.0 (2025, publicado en junio de 2026) |
| CiteScore (Scopus) | 13.9 |
| SJR | 1.568 |
| Modelo de acceso | Hibrida: suscripcion (sin cargo para autores) o acceso abierto opcional |
| APC (si se elige OA) | 2.800 USD (tarifa IEEE 2026 para revistas hibridas) |
| Tiempo medio a primera decision | No publicado oficialmente; verificar en publication-recommender.ieee.org |
| Tasa de aceptacion | No publicada oficialmente |
| Herramienta oficial | publication-recommender.ieee.org |
| Justificacion de ajuste tematico | IEEE TSE publica estudios empiricos y de requisitos con impacto; el protocolo sigue las guias de reporte empirico que la revista promueve. Alternativa sin cargo por publicacion por suscripcion. |

---

### 3.2 IEEE Access (IEEE) - CON APC (gold open access)

| Campo | Valor |
|---|---|
| Nombre completo | IEEE Access |
| Editorial | IEEE |
| ISSN | 2169-3536 |
| Indexacion JCR | SCIE - Computer Science, Information Systems (Q2); Engineering, Electrical & Electronic (Q2); Telecommunications (Q2) |
| Factor de impacto | 4.2 (2025, publicado en junio de 2026) |
| CiteScore (Scopus) | 3.6-3.9 |
| Modelo de acceso | Gold open access (todos los articulos de acceso abierto) |
| APC | 2.160 USD por articulo (sin limite de paginas; tarifa oficial IEEE Access) |
| Tiempo medio a primera decision | Envio a publicacion 4-6 semanas (declarado por la editorial) |
| Tasa de aceptacion | No publicada oficialmente |
| Herramienta oficial | publication-recommender.ieee.org |
| Justificacion de ajuste tematico | Revista multidisciplinar de acceso abierto; acepta estudios empiricos de ingenieria de software y es la alternativa de acceso abierto con APC mas economica del portafolio IEEE (2.160 USD). |

---

## 4. Resumen comparativo y decision preliminar

| Editorial | Candidata | Modelo | APC (USD) | Cuartil JCR | IF |
|---|---|---|---|---|---|
| Springer | Requirements Engineering | Hibrida / suscripcion | 0 (sin cargo) / ~2.780 si OA | Q2 | 3.3 |
| Springer | Empirical Software Engineering | Hibrida | 2.890 si OA | Q2 | 3.4 |
| Elsevier | Information and Software Technology | Hibrida / suscripcion | 0 (sin cargo) / 3.890 si OA | Q1 | 4.6 |
| Elsevier | Journal of Systems and Software | Hibrida | 3.670 si OA | Q2 | 3.8 |
| IEEE | IEEE TSE | Hibrida / suscripcion | 0 (sin cargo) / 2.800 si OA | Q1 | 6.0 |
| IEEE | IEEE Access | Gold OA | 2.160 | Q2 | 4.2 |

**Decision preliminar (semana 16):** el equipo de pregrado no dispone de
financiamiento para APC (1500-3500 USD). La alternativa viable de envio es una
revista hibrida por suscripcion sin cargo: **Requirements Engineering
(Springer)** por ajuste tematico, o **Information and Software Technology
(Elsevier)** por cuartil Q1. IEEE Access (2.160 USD) queda como alternativa de
acceso abierto si se consigue financiamiento institucional. La puntuacion
exacta de ajuste de cada herramienta oficial se registrara en la semana 16
antes de decidir el envio.

Nota metodologica: las metricas de impacto y cuartil corresponden al JCR
publicado en junio de 2026 (datos 2025/2024 segun cada fuente); las tarifas
APC provienen de las paginas oficiales de la editorial y de listas de tarifas
publicadas (IEEE 2026, Springer Nature 2026). Los tiempos medios a primera
decision y las tasas de aceptacion no estan publicados oficialmente por las
editoriales para estas revistas; se verificaran con la herramienta oficial de
cada editorial antes de la semana 16.
