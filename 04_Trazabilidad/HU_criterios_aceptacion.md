# Historias de Usuario y Criterios de Aceptación
### Sistema de Gestión Agrícola con IA (verde y cacao) — 12 RF *Debe tener*

Cada historia sigue la plantilla Connextra (Cohn, 2004): *"Como ⟨rol⟩, quiero ⟨funcionalidad⟩,
para ⟨beneficio esperado⟩"*. Los criterios de aceptación siguen el formato Gherkin
Dado-Cuando-Entonces. Los IDs (HU-XX, CA-XX) coinciden con los ya usados en
`04_Trazabilidad/matriz_trazabilidad.csv`. El contenido de cada historia y sus escenarios se
deriva directamente de las especificaciones de casos de uso (`UC-02_Detailed_Use_Case_
Specifications.md`) y de los fragmentos `alt` ya definidos en los diagramas de secuencia
correspondientes — no se introducen flujos nuevos.


### HU-01 — Iniciar sesión (RF-01 / UC-01 / SEQ-01)
**Historia:** Como usuario del sistema (Administrador o Jornalero), quiero iniciar sesión con
usuario y contraseña, para acceder únicamente a las funciones que corresponden a mi rol.

**INVEST:** Independiente (no depende de otra HU) · Negociable (mecanismo de bloqueo es
ajustable) · Valiosa (habilita el control de acceso de todo el sistema) · Estimable · Pequeña ·
Verificable (criterios abajo).

**CA-01:**
```gherkin
Escenario: Inicio de sesión exitoso
  Dado que el usuario está registrado en el sistema
  Cuando ingresa un usuario y contraseña válidos
  Entonces el sistema concede acceso y redirige a la pantalla correspondiente a su rol

Escenario: Credenciales incorrectas
  Dado que el usuario ingresa un usuario o contraseña inválidos
  Cuando intenta iniciar sesión
  Entonces el sistema muestra un mensaje de error y permite reintentar

Escenario: Bloqueo temporal por intentos fallidos
  Dado que el usuario ha fallado 5 intentos consecutivos
  Cuando intenta iniciar sesión una vez más
  Entonces el sistema bloquea la cuenta temporalmente
```


### HU-02 — Gestionar parcelas (RF-02 / UC-02 / SEQ-02)
**Historia:** Como Administrador, quiero registrar, consultar, actualizar y eliminar parcelas,
para mantener un inventario correcto de los lotes de la finca.

**INVEST:** Independiente · Negociable · Valiosa (base de todo el modelo de datos) · Estimable ·
Pequeña · Verificable.

**CA-02:**
```gherkin
Escenario: Registro de una nueva parcela con datos válidos
  Dado que el Administrador ha iniciado sesión
  Cuando registra una parcela con nombre, ubicación, área y estado
  Entonces el sistema guarda la parcela y la muestra en el listado

Escenario: Intento de registro con campos obligatorios vacíos
  Dado que el Administrador deja el nombre de la parcela vacío
  Cuando intenta guardar
  Entonces el sistema solicita completar los campos obligatorios y no guarda el registro

Escenario: Intento de registro con nombre de parcela duplicado
  Dado que ya existe una parcela con el mismo código
  Cuando el Administrador intenta guardar otra con el mismo código
  Entonces el sistema solicita un nombre único y no guarda el duplicado
```


### HU-03 — Gestionar cultivos (RF-03 / UC-03 / SEQ-03)
**Historia:** Como Administrador, quiero registrar los cultivos de verde y cacao asociados a
cada parcela, para saber qué se está produciendo en cada lote.

**INVEST:** Depende de HU-02 (debe existir al menos una parcela) · Negociable · Valiosa ·
Estimable · Pequeña · Verificable.

**CA-03:**
```gherkin
Escenario: Registro de un cultivo en una parcela existente
  Dado que existe al menos una parcela registrada
  Cuando el Administrador registra un cultivo indicando tipo, variedad, fecha de siembra y estado
  Entonces el sistema asocia el cultivo a la parcela seleccionada

Escenario: Intento de registro con campos incompletos
  Dado que falta un campo obligatorio del cultivo
  Cuando el Administrador intenta guardar
  Entonces el sistema solicita completar los campos requeridos

Escenario: Parcela ya alcanzó el máximo de cultivos permitidos
  Dado que la parcela seleccionada ya tiene el número máximo de cultivos activos
  Cuando el Administrador intenta agregar otro cultivo a esa parcela
  Entonces el sistema sugiere seleccionar otra parcela
```


### HU-04 — Registrar actividad agrícola (RF-04 / UC-04 / SEQ-04)
**Historia:** Como Jornalero, quiero registrar las labores que realizo en el campo (siembra,
fertilización, fumigación, poda, cosecha), para que el Administrador tenga visibilidad del
trabajo realizado.

**INVEST:** Independiente · Negociable · Valiosa (elimina el registro manual en bitácora física,
hallazgo directo de la entrevista) · Estimable · Pequeña · Verificable.

**CA-04:**
```gherkin
Escenario: Registro exitoso de una actividad
  Dado que el Jornalero ha iniciado sesión
  Cuando registra una actividad indicando fecha, tipo y parcela
  Entonces el sistema guarda el registro y queda disponible para el Administrador

Escenario: Registro con datos incompletos
  Dado que el Jornalero no indica el tipo de actividad
  Cuando intenta guardar el registro
  Entonces el sistema solicita completar los campos obligatorios
```


### HU-05 — Registrar cosecha (RF-05 / UC-05 / SEQ-05)
**Historia:** Como Jornalero, quiero registrar la cantidad cosechada de cada cultivo, para que
el Administrador pueda controlar la producción y detectar caídas de rendimiento a tiempo.

**INVEST:** Depende de HU-03 (debe existir el cultivo) · Negociable · Valiosa (máxima prioridad
de negocio según WSJF, ver `priorizacion_moscow_kano.csv`) · Estimable · Pequeña · Verificable.

**CA-05:**
```gherkin
Escenario: Registro de cosecha con datos válidos
  Dado que existe un cultivo previamente registrado
  Cuando el usuario ingresa cantidad, unidad, parcela, fecha y observaciones
  Entonces el sistema guarda el registro y actualiza el historial de producción

Escenario: Cantidad inválida
  Dado que el usuario ingresa una cantidad igual o menor a cero
  Cuando intenta guardar el registro
  Entonces el sistema muestra una advertencia y no guarda el registro

Escenario: Campos obligatorios incompletos
  Dado que falta un campo obligatorio (por ejemplo la unidad de medida)
  Cuando el usuario intenta guardar
  Entonces el sistema solicita completar el campo faltante
```


### HU-06 — Gestionar inventario de insumos (RF-06 / UC-06 / SEQ-06)
**Historia:** Como Administrador, quiero registrar y actualizar el inventario de insumos y
herramientas, para evitar desabastecimiento durante labores críticas.

**INVEST:** Independiente · Negociable · Valiosa (alta reducción de riesgo según WSJF) ·
Estimable · Pequeña/mediana · Verificable.

**CA-06:**
```gherkin
Escenario: Registro de un insumo nuevo
  Dado que el insumo no existe previamente en el inventario
  Cuando el Administrador lo registra con nombre, tipo, cantidad y unidad
  Entonces el sistema lo agrega al inventario

Escenario: Actualización de cantidad de un insumo existente
  Dado que el insumo ya existe en el inventario
  Cuando el Administrador registra una entrada o salida de stock
  Entonces el sistema actualiza la cantidad disponible

Escenario: Cantidad disponible cae por debajo del umbral mínimo
  Dado que la cantidad disponible de un insumo queda por debajo de su umbral mínimo
  Cuando el sistema recalcula el stock tras una actualización
  Entonces se genera una alerta dirigida al Administrador (ver RF-16)
```


### HU-07 — Consultar producción por período (RF-07 / UC-07 / SEQ-07)
**Historia:** Como Administrador, quiero consultar la producción registrada en un período
específico, para dar seguimiento al rendimiento de los cultivos a lo largo del tiempo.

**INVEST:** Depende de HU-05 (deben existir registros de cosecha) · Negociable · Valiosa ·
Estimable · Pequeña · Verificable.

**CA-07:**
```gherkin
Escenario: Consulta con resultados
  Dado que existen registros de producción en el período seleccionado
  Cuando el Administrador selecciona una fecha de inicio y fin
  Entonces el sistema muestra la producción agregada de ese período

Escenario: Consulta sin resultados
  Dado que no existen registros de producción en el período seleccionado
  Cuando el Administrador realiza la consulta
  Entonces el sistema informa que no hay datos disponibles para ese rango
```


### HU-08 — Planificar actividad agrícola (RF-08 / UC-08 / SEQ-08)
**Historia:** Como Administrador, quiero planificar actividades agrícolas con anticipación, para
organizar el trabajo del equipo de campo antes de asignarlo.

**INVEST:** Depende de HU-02 · Negociable · Valiosa · Estimable · Pequeña · Verificable.

**CA-08:**
```gherkin
Escenario: Planificación sin conflicto de horario
  Dado que no existe otra actividad planificada para la misma parcela y fecha
  Cuando el Administrador planifica una nueva actividad
  Entonces el sistema la guarda con estado "Pendiente"

Escenario: Conflicto de horario detectado
  Dado que ya existe una actividad planificada para la misma parcela y fecha
  Cuando el Administrador intenta planificar otra actividad en el mismo horario
  Entonces el sistema muestra una advertencia y permite confirmar de todas formas
```


### HU-09 — Asignar tarea (RF-09 / UC-09 / SEQ-09)
**Historia:** Como Administrador, quiero asignar actividades planificadas a un trabajador
específico, para coordinar al equipo de campo de forma clara.

**INVEST:** Depende de HU-08 · Negociable · Valiosa · Estimable · Pequeña · Verificable.

**CA-09:**
```gherkin
Escenario: Asignación exitosa
  Dado que existe una actividad planificada sin asignar
  Cuando el Administrador selecciona un trabajador y confirma la asignación
  Entonces la tarea queda visible en la lista de tareas del trabajador

Escenario: No hay actividades planificadas disponibles
  Dado que no existen actividades planificadas pendientes de asignación
  Cuando el Administrador intenta asignar una tarea
  Entonces el sistema sugiere planificar una actividad primero (HU-08)
```


### HU-10 — Dar seguimiento al cumplimiento de tareas (RF-10 / UC-10 / SEQ-10)
**Historia:** Como Administrador, quiero consultar el estado de las tareas asignadas
(Pendiente/En curso/Bloqueado/Completado), para saber cómo avanza el trabajo de campo.

**INVEST:** Depende de HU-09 · Negociable · Valiosa · Estimable · Pequeña · Verificable.

**CA-10:**
```gherkin
Escenario: Consulta con tareas asignadas
  Dado que existen tareas previamente asignadas
  Cuando el Administrador abre el módulo de seguimiento
  Entonces el sistema muestra cada tarea con su estado actual

Escenario: Sin tareas asignadas todavía
  Dado que no se ha asignado ninguna tarea
  Cuando el Administrador abre el módulo de seguimiento
  Entonces el sistema informa que no hay tareas asignadas
```


### HU-11 — Generar reportes de producción (RF-11 / UC-11 / SEQ-11)
**Historia:** Como Administrador, quiero generar reportes de producción filtrados por cultivo,
parcela o período, para analizar el desempeño de la finca y tomar decisiones informadas.

**INVEST:** Depende de HU-05/HU-07 · Negociable · Valiosa · Estimable · Mediana (incluye
exportación) · Verificable.

**CA-11:**
```gherkin
Escenario: Generación exitosa del reporte
  Dado que existen registros que coinciden con los filtros seleccionados
  Cuando el Administrador genera el reporte
  Entonces el sistema lo muestra y permite descargarlo

Escenario: Sin registros que coincidan con los filtros
  Dado que no existen registros para los filtros seleccionados
  Cuando el Administrador intenta generar el reporte
  Entonces el sistema informa que no hay datos para reportar
```


### HU-12 — Gestionar usuarios (RF-14 / UC-14 / SEQ-12)
**Historia:** Como Administrador, quiero registrar, editar y desactivar cuentas de usuario, para
controlar quién tiene acceso al sistema y con qué rol.

**INVEST:** Independiente · Negociable · Valiosa · Estimable · Pequeña · Verificable.

**CA-12:**
```gherkin
Escenario: Registro exitoso de un nuevo usuario
  Dado que el nombre de usuario elegido es único y los datos son válidos
  Cuando el Administrador guarda la nueva cuenta
  Entonces el sistema la crea y queda disponible para iniciar sesión (ver HU-01)

Escenario: Nombre de usuario duplicado
  Dado que ya existe una cuenta con el mismo nombre de usuario
  Cuando el Administrador intenta registrar otra cuenta con ese nombre
  Entonces el sistema solicita un nombre de usuario único

Escenario: Desactivación de una cuenta
  Dado que el Administrador selecciona desactivar una cuenta existente
  Cuando confirma la desactivación
  Entonces el sistema revoca el acceso sin eliminar los registros históricos asociados a esa cuenta
```


### Trazabilidad con la matriz extendida
Estos 12 pares HU/CA corresponden exactamente a las columnas `ID-HU` e `ID-CA` ya presentes en
`04_Trazabilidad/matriz_trazabilidad.csv` (filas TR-01 a TR-XX según el RF). No se requieren
cambios en la matriz: los IDs ya coinciden.
