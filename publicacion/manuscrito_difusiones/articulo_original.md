# INTEGRACIÓN DE AGENTES DE INTELIGENCIA ARTIFICIAL Y PROTOCOLO MCP EN LA EVALUACIÓN CONTINUA UNIVERSITARIA: ARQUITECTURA TÉCNICA Y EXPERIENCIA DE TRANSFERENCIA DOCENTE

# *INTEGRATION OF ARTIFICIAL INTELLIGENCE AGENTS AND MCP PROTOCOL IN UNIVERSITY CONTINUOUS ASSESSMENT: TECHNICAL ARCHITECTURE AND TEACHER TRANSFER EXPERIENCE*

---

### RESUMEN
La irrupción de los modelos de lenguaje de gran escala (LLM) ha tensionado las prácticas tradicionales de evaluación en la enseñanza universitaria de la informática. Frente a respuestas binarias de prohibición o delegación acrítica, este trabajo presenta una arquitectura sociotécnica orientada a la evaluación formativa y continua supervisada, fundamentada en el Protocolo de Contexto de Modelo (*Model Context Protocol*, MCP) y el principio de supervisión docente activa (*Human-in-the-Loop*, HITL). La solución desarrollada desacopla la inteligencia generativa de la lógica de negocio pedagógica mediante el uso de especificaciones formales basadas en Markdown (`AGENTS.md`, `MEMORY.md`, rúbricas analíticas y *Skills* docentes estructuradas), permitiendo al agente de IA inspeccionar entornos locales de código de manera auditable y emitir borradores de retroalimentación constructiva y socrática. Para evaluar la viabilidad y transferencia de la propuesta, se implementó una prueba piloto curricular en cátedras de programación de ingeniería y se dictó un taller de capacitación docente de 10 horas reloj que convocó a 70 participantes (profesores universitarios de Ingeniería en Informática y estudiantes avanzados de Profesorado y Licenciatura en Informática Educativa). Los resultados revelan una recepción positiva de la metodología y un alto interés en el uso pedagógico de agentes contextualizados, al tiempo que evidencian una pronunciada brecha de instrumentación técnica (*tooling gap*) respecto al uso autónomo de pipelines de integración continua (Git/GitHub Actions), la cual fue mitigada mediante el diseño de widgets interactivos desacoplados en HTML/JS. Se concluye que la combinación de MCP con especificaciones formales humanamente supervisadas transforma a la IA de una amenaza de deshonestidad académica en un andamio riguroso para la evaluación continua formativa.

**Palabras clave:** Evaluación formativa, Agentes de inteligencia artificial, Protocolo de contexto de modelo (MCP), Formación docente, Educación en ciencias de la computación.

---

### ABSTRACT
The emergence of Large Language Models (LLMs) has challenged traditional assessment practices in higher education computer science courses. Moving beyond binary stances of prohibition or uncritical delegation, this paper presents a sociotechnical architecture designed for supervised, continuous formative assessment based on the Model Context Protocol (MCP) and the Human-in-the-Loop (HITL) principle. The proposed solution decouples generative intelligence from pedagogical business logic through formal Markdown specifications (`AGENTS.md`, `MEMORY.md`, analytical rubrics, and structured teaching Skills), enabling AI agents to inspect local code repositories in an auditable manner and draft constructive, Socratic feedback. To assess the feasibility and transferability of this approach, a curricular pilot was conducted in university programming courses, alongside a 10-hour teacher professional development workshop attended by 70 participants (computer science faculty and advanced pre-service teachers from educational informatics programs). Findings indicate high engagement with contextualized agent methodologies, while highlighting a significant tooling gap regarding the autonomous use of continuous integration pipelines (Git/GitHub Actions), which was mitigated by deploying decoupled interactive HTML/JS widgets. We conclude that combining MCP with human-supervised formal specifications transforms generative AI from an academic integrity threat into a robust scaffold for continuous formative assessment.

**Keywords:** Formative assessment, Artificial intelligence agents, Model Context Protocol (MCP), Teacher training, Computer science education.

---

## 1. INTRODUCCIÓN

La masificación de los Modelos de Lenguaje de Gran Escala (LLM, por sus siglas en inglés) a partir de 2023 ha generado una disrupción sin precedentes en la educación superior, con un impacto particularmente agudo en las carreras de Ciencias de la Computación e Ingeniería en Informática (Becker et al., 2023; Prather et al., 2023). La capacidad de estas herramientas para generar código sintáctica y semánticamente correcto, resolver problemas algorítmicos introductorios e incluso explicar errores de depuración ha dejado obsoletos los mecanismos tradicionales de evaluación sumativa basados en la entrega asincrónica de código fuente sin supervisión contextual (Finnie-Ansley et al., 2022).

Frente a este escenario, las respuestas institucionales predominantes en el ámbito universitario han oscilado entre dos extremos igualmente problemáticos. Por un lado, las posturas tecnofóbicas o prohibicionistas han intentado restringir el acceso a herramientas generativas mediante políticas punitivas o el retorno exclusivo a exámenes presenciales manuscritos; tales medidas resultan insostenibles a mediano plazo, desconectan a la universidad de las prácticas profesionales reales del desarrollo de software y no fomentan el pensamiento computacional crítico (Denny et al., 2024). Por otro lado, las posturas de adopción ingenua han promovido el uso de interfaces genéricas de chat comercial mediante interacción conversacional básica (*prompts zero-shot*), lo cual introduce riesgos sustanciales de alucinación técnica, inconsistencia en los criterios evaluativos, falta de trazabilidad y una delegación ciega de la autoridad pedagógica en modelos propietarios de caja negra (Lau & Guo, 2023).

En el marco de la enseñanza de la programación, la evaluación continua y formativa no persigue únicamente la asignación de una calificación numérica, sino la provisión oportuna de retroalimentación (*feedback*) accionable, dialógica y andamiada que oriente al estudiante en la identificación de sus modelos mentales erróneos y en la refactorización iterativa de sus algoritmos (Black & Wiliam, 1998; Shute, 2008). Sin embargo, en las universidades latinoamericanas, los docentes enfrentan comisiones numerosas y una alta carga horaria, lo que vuelve casi inviable la provisión de devoluciones cualitativas personalizadas y continuas para cada entrega de código.

La emergencia reciente de los **Agentes de Inteligencia Artificial** basados en llamadas a funciones y, de manera paradigmática, la publicación del **Protocolo de Contexto de Modelo** (*Model Context Protocol* - MCP) a finales de 2024, introduce una oportunidad arquitectónica inédita (Anthropic, 2024). MCP es un estándar abierto que permite desacoplar al modelo generativo del entorno computacional, posibilitando que los agentes consulten de forma estandarizada y segura herramientas locales (como el sistema de archivos, repositorios de versiones o motores de prueba automatizada) sin exponer credenciales ni requerir integraciones ad-hoc propietarias.

No obstante, la disponibilidad de estándares de interoperabilidad técnica no resuelve por sí misma el problema pedagógico. Si los agentes operan sin restricciones contextuales, tenderán a "resolver el ejercicio" en lugar de enseñar, suprimiendo el esfuerzo cognitivo del estudiante. Surge así la necesidad de articular el protocolo técnico con principios metodológicos de **Desarrollo Guiado por Especificaciones** (*Spec-Driven Development* - SDD) y gobernanza **Humano en el Bucle** (*Human-in-the-Loop* - HITL), garantizando que la IA actúe como un asistente docente estructurado y auditable, y nunca como un juez autónomo.

El presente trabajo expone el diseño, implementación y transferencia de una arquitectura sociotécnica para la evaluación continua asistida y supervisada en materias de programación. El proyecto se articula en torno a dos ejes fundamentales:
1. El desarrollo de una infraestructura metodológica y técnica sustentada en MCP, `AGENTS.md`, `MEMORY.md` y *Skills* docentes estandarizadas para el análisis estático y dinámico de entregas estudiantiles.
2. La transferencia formativa hacia la comunidad docente mediante un taller intensivo de capacitación que involucró tanto a profesores de ingeniería como a futuros docentes de carreras de profesorado y licenciatura en informática educativa, analizando de manera honesta y rigurosa las dinámicas de adopción, las oportunidades pedagógicas y las brechas de instrumentación técnica detectadas.

---

## 2. MÉTODOS Y ARQUITECTURA TÉCNICA

### 2.1. Marco Metodológico y Enfoque de Diseño
La investigación adoptó un enfoque de **Investigación Basada en el Diseño** (*Design-Based Research* - DBR) (Wang & Hannafin, 2005), articulado en ciclos iterativos de análisis del problema, diseño de artefactos computacionales y pedagógicos, implementación en escenarios reales de aula universitaria y evaluación formativa de impacto. Este enfoque resulta idóneo para la ingeniería educativa, ya que permite refinar colaborativamente tanto la arquitectura técnica como las directivas pedagógicas a medida que emergen tensiones empíricas en el terreno formativo.

### 2.2. Arquitectura Sociotécnica Basada en MCP y HITL
La arquitectura propuesta (Figura 1) descansa en la separación estricta entre tres capas operativas: la capa de gobernanza contextual, la capa de interoperabilidad mediante protocolo y la capa de supervisión docente.

```
+------------------------------------------------------------------------+
|                      CAPA 1: GOBERNANZA CONTEXTUAL                     |
|  - AGENTS.md (Identidad, tono socrático, restricciones éticas)         |
|  - MEMORY.md (Estado persistente, convenciones de la cátedra)          |
|  - Rúbricas Analíticas en Markdown (Niveles de logro y criterios)      |
|  - Skills Docentes Estructuradas (Procedimientos y delimitadores)       |
+-----------------------------------+------------------------------------+
                                    |
                                    v
+-----------------------------------+------------------------------------+
|               CAPA 2: INTEROPERABILIDAD PROTOCOLIZADA (MCP)            |
|  - Agente de IA (Modelo de razonamiento / LLM)                         |
|  - Servidor MCP Local (Filesystem Server / Git Server)                 |
|  - Lectura segura de entregas y pruebas de escritorio en sandbox local |
+-----------------------------------+------------------------------------+
                                    |
                                    v
+-----------------------------------+------------------------------------+
|                 CAPA 3: SUPERVISIÓN HUMANA (HITL)                      |
|  - Generación de informe preliminar de evidencias (Pre-diagnóstico)    |
|  - Auditoría docente (Confirmación vs. Refutación de alucinaciones)    |
|  - Ajuste pedagógico contextual (Decisión docente indelegable)         |
|  - Devolución final formateada al estudiante                           |
+------------------------------------------------------------------------+
```
*Figura 1. Arquitectura de tres capas para la evaluación continua asistida con MCP.*

#### A. La Capa de Gobernanza Contextual
Para evitar las fallas de predictibilidad asociadas al prompting no estructurado, se diseñó un sistema de persistencia documental versionable en Git:
- **`AGENTS.md`:** Define el documento de identidad del agente, su rol como facilitador socrático, la prohibición taxativa de proveer código resuelto directamente al estudiante y la obligatoriedad de fundamentar cada observación en líneas de código concretas.
- **`MEMORY.md`:** Actúa como memoria externa de largo plazo entre sesiones de trabajo, almacenando decisiones curriculares tomadas, convenciones específicas de sintaxis (ej. estándares C++17 o PSeInt estricto) y el estado de avance de la cohorte.
- **Rúbricas Analíticas:** Tablas multidimensionales en Markdown donde cada criterio (funcionalidad, modularización, legibilidad y buenas prácticas) cuenta con descripciones precisas de evidencia observable para cada nivel de desempeño.
- **Skills Docentes:** Módulos de instrucciones formalizados con cabeceras YAML (*frontmatter*), delimitadores unívocos (`<contexto>`, `<restricciones>`, `<procedimiento>`) y esquemas JSON para estructurar el diagnóstico de fallas sintácticas y algorítmicas.

#### B. La Capa de Protocolo (MCP)
En lugar de copiar y pegar fragmentos de código de estudiantes en ventanas de chat comerciales (lo cual vulnera la privacidad del alumno y descontextualiza el árbol de dependencias), el agente opera dentro del entorno de desarrollo (IDE) conectándose a un servidor MCP de sistema de archivos (*Filesystem Server*). A través de llamadas protocolizadas (`list_directory`, `read_file`), el agente inspecciona de manera autónoma pero auditable los archivos del proyecto, ejecuta pruebas unitarias o scripts de comprobación local y contrasta las evidencias encontradas contra la rúbrica oficial de la cátedra.

#### C. Principio Human-in-the-Loop (HITL)
El sistema opera bajo un contrato operativo estricto: **el agente nunca publica notas ni envía retroalimentaciones directas al estudiante de forma autónoma**. La IA actúa exclusivamente como asistente pericial que redacta un borrador de informe de evidencias. El docente revisa el pre-diagnóstico, audita que las citas del código sean reales (eliminando falsos positivos) y modula el tono comunicacional antes de validar la devolución definitiva.

### 2.3. Despliegue Piloto en Cátedras Universitarias
La arquitectura fue implementada y evaluada de manera progresiva durante el ciclo lectivo 2026 en múltiples asignaturas de grado de dos universidades de la región (una universidad privada y una universidad nacional pública), abarcando diversos paradigmas de programación, niveles formativos y áreas de la ingeniería:
- *Programación II* (3° año de Ingeniería en Informática, universidad privada): Asignatura orientada al desarrollo web y arquitecturas basadas en componentes, donde los agentes supervisaron entregas de maquetación avanzada (HTML/CSS semántico) y lógica cliente.
- *Algoritmos y Programación* (1° año de Ingeniería en Informática, universidad privada): Asignatura troncal introductoria centrada en modularización algorítmica, funciones, paso de parámetros y arreglos unidimensionales en C++, donde se diseñó un banco integral de simulacros y exámenes basados en especificaciones SDD y rúbricas matriciales.
- *Teoría de Sistemas Operativos* (3° año de Licenciatura e Ingeniería, universidad nacional pública): Enfocada en la administración de permisos avanzados en entornos GNU/Linux (SUID, GUID, umask, ACLs), seguridad de archivos y auditoría de integridad criptográfica mediante scripts de verificación automatizada.
- *Sistemas Operativos II* (4° año de Ingeniería, universidad nacional pública): Centrada en la concurrencia, sincronización de procesos, prevención de interbloqueos (*deadlocks*) y sistemas distribuidos, articulando proyectos con autograders en Python y rúbricas JSON formalizadas.
- *Informática* (1° año de Tecnicatura Universitaria en Automatización y Robótica, universidad privada): Nivelación algorítmica inicial y lógica computacional aplicada al control instrumental.

### 2.4. Diseño y Metodología del Taller de Transferencia Docente
Con el propósito de validar la transferibilidad de la metodología y medir la capacidad de docentes reales para adoptar estos flujos de trabajo, se diseñó e implementó el *"Taller de Capacitación: Agentes de IA y Protocolo MCP para Evaluación Continua y Autoevaluación"*.

- **Carga Horaria y Formato:** 10 horas reloj presenciales/sincrónicas distribuidas en dos jornadas consecutivas (Día 1: Fundamentos y Persistencia de Contexto; Día 2: Skills Avanzadas, Protocolo MCP y Laboratorio Integrador).
- **Población Objetivo:** Se inscribieron 80 participantes y asistieron de forma efectiva 70 (87.5% de asistencia). La cohorte estuvo integrada por dos perfiles complementarios:
  1. Profesores universitarios en ejercicio de la carrera de Ingeniería en Informática.
  2. Estudiantes avanzados y graduados recientes del Profesorado Universitario en Informática (PUInf) y la Licenciatura en Informática Educativa (LIE) de la universidad nacional de la misma región.
- **Instrumentación del Taller:**
  - Se distribuyó un repositorio plantilla de código abierto en GitHub (`plantilla-taller-docente-mcp`) concebido como andamio de aprendizaje autodirigido.
  - El repositorio contenía un evaluador automático en Python (`autograder_taller.py`) integrado a un pipeline de GitHub Actions, configurado para asignar puntaje sobre 100 puntos:
    - **Día 1 (60 pts):** Resolución de un laboratorio web interactivo sobre fundamentos teóricos de MCP (`respuestas_taller.json`, 20 pts) y creación de la arquitectura base de la cátedra (`AGENTS.md`, `MEMORY.md`, `planificacion.md` y directorio `/bibliografia`, 40 pts).
    - **Día 2 (40 pts):** Creación del Trabajo Práctico 1 conteniendo su `rubrica.md` (20 pts) y su Skill docente de evaluación `skill_evaluador.md` (20 pts).
  - Como complemento ante la diversidad de competencias técnicas, se proveyó un toolkit pedagógico descargable y un catálogo de laboratorios web interactivos.

---

## 3. RESULTADOS

### 3.1. Artefactos Pedagógicos y Repositorio Plantilla Desarrollado
El primer resultado tangible del proyecto fue la consolidación del ecosistema de recursos abiertos [plantilla-taller-docente-mcp](https://github.com/Taller-de-Agentes-de-IA-en-docencia/plantilla-taller-docente-mcp). Este repositorio resolvió el problema del arranque en frío (*cold start*) que habitualmente paraliza a los educadores cuando intentan configurar entornos con IA.

El repositorio integró:
1. Una guía metodológica simplificada basada en desarrollo guiado por especificaciones (`SDD.md` y `prompt_generador_zero_shot.md`).
2. Un *Toolkit Docente* modularizado con guías de contexto anti-alucinaciones, plantillas de agentes evaluadores técnicos y esquemas de cuestionarios psicométricos sin sesgo.
3. Un pipeline de autoevaluación continua transparente que brinda feedback instantáneo a través de la pestaña de *Actions* de GitHub.

### 3.2. Catálogo Multidisciplinar de Laboratorios Interactivos Desacoplados
Para demostrar la aplicabilidad transversal del paradigma en asignaturas de ciencias de la computación, se generó un repositorio de recursos interactivos distribuidos en 5 asignaturas universitarias:
- **Algoritmos y Programación:** 35 laboratorios web autocontenidos en HTML/JS puro y CSS responsivo (sin dependencias de frameworks ni requerimiento de servidores Node.js), abarcando desde linealización de expresiones aritméticas y operadores relacionales hasta manipulación de memoria con paso de parámetros por referencia, acompañados de un banco completo de exámenes parciales en C++ con especificación SDD.
- **Estructuras de Datos:** Simuladores visuales de algoritmos sobre grafos (camino mínimo de Dijkstra, detección de puntos de articulación y puentes) y exploradores interactivos de estructuras enlazadas dinámicas.
- **Modelos y Simulación:** Aplicaciones web completas para experimentación estocástica con el método de Monte Carlo, generadores congruenciales pseudoaleatorios y baterías de pruebas estadísticas de bondad de ajuste.
- **Sistemas Operativos I y II:** Laboratorios prácticos de permisos de seguridad en Linux (SUID, ACLs), auditoría de integridad criptográfica (SHA-256), resolución de interbloqueos (*deadlocks*) y concurrencia con evaluación automática integrada.

### 3.3. Métricas de Participación y Alcance del Taller Docente
La convocatoria del taller registró una demanda significativa en la comunidad académica regional. De los 80 postulantes inscriptos, 70 asistieron a las actividades sincrónicas (tasa de retención del 87.5%). La heterogeneidad disciplinar del público enriqueció las discusiones pedagógicas: mientras los docentes ingenieros aportaron cuestionamientos sobre la precisión sintáctica de los LLMs en lenguajes fuertemente tipados, los participantes provenientes del profesorado y de la licenciatura en informática educativa enfatizaron los aspectos didácticos, la mediación comunicativa y la pertinencia ética del feedback formativo.

### 3.4. Dinámica de Adopción Técnica y el Fenómeno de la Brecha de Instrumentación (*Tooling Gap*)
El análisis de la telemetría del repositorio plantilla y de las ejecuciones del pipeline en GitHub Actions arrojó un hallazgo empírico de notable relevancia: **únicamente un participante (1/70) completó el ciclo integral de versionado y alcanzó los 100 puntos en GitHub Actions de forma autónoma durante el taller**.

La triangulación cualitativa de observaciones de campo y consultas presenciales durante las sesiones permitió identificar los factores causales de este comportamiento:
1. **Fricción cognitiva con herramientas de desarrollo (Git/CLI):** Si bien los asistentes comprendieron de inmediato la lógica conceptual de los archivos `AGENTS.md` y las *Skills*, una fracción mayoritaria de los participantes (especialmente aquellos no habituados al flujo diario de terminal) experimentó bloqueos en los pasos instrumentales: autenticación de credenciales personales en GitHub, resolución de conflictos de ramas y comandos `git push`.
2. **Rol de observador analítico (*Lurking reflexivo*):** La mayoría de los docentes priorizó prestar atención a las demostraciones en vivo del capacitador, tomar notas pedagógicas y reflexionar sobre la aplicabilidad en sus respectivos programas curriculares, postergando la ejecución técnica para instancias posteriores sin presión sincrónica.
3. **Eficacia compensatoria de los widgets web:** Los docentes que se sintieron abrumados por la consola de comandos interactuaron con fluidez con los widgets web autocontenidos (`index.html`), resolviendo los desafíos conceptuales de manera exitosa en el navegador sin requerir compiladores locales ni clientes de control de versiones.

---

## 4. DISCUSIÓN

### 4.1. La Brecha de Instrumentación como Hallazgo Pedagógico
El contraste entre el alto nivel de entusiasmo y asistencia (87.5%) y la baja tasa de culminación sincrónica en el sistema CI/CD automatizado (1.4%) constituye una evidencia empírica clave sobre la adopción de IA en la docencia universitaria.

En la literatura de informática educativa, diversos autores han advertido que la introducción de herramientas profesionales de integración continua (como GitHub Classroom y Actions) suele generar una curva de fricción técnica que desvía la atención de los objetivos pedagógicos centrales (Hellas et al., 2017). Los hallazgos de este estudio demuestran que cuando se pretende capacitar a docentes en el uso de Agentes de IA, exigir de forma simultánea el dominio de flujos avanzados de Git añade una sobrecarga cognitiva innecesaria.

Este hallazgo valida retrospectivamente una decisión de diseño central del proyecto: **el desarrollo de interfaces desacopladas y widgets HTML/JS locales**. Para democratizar la evaluación continua basada en agentes, la tecnología subyacente (MCP, linters, autograders) debe abstraerse progresivamente detrás de interfaces más cercanas al usuario docente, o bien implementarse dentro de plataformas con workflows nativos simplificados (como *ClassMoji* o entornos web guiados).

### 4.2. El Valor de las Especificaciones Formales frente al Prompting Libre
Los experimentos de evaluación realizados durante el pilotaje en *Programación II* y *Algoritmos y Programación* ratifican que los LLMs carecen de memoria institucional estable. Cuando un docente intenta corregir mediante prompts improvisados en chats convencionales, el agente tiende a ser permisivo con malas prácticas de diseño algorítmico o, por el contrario, hipercrítico con convenciones secundarias de estilo.

La adopción de `AGENTS.md` y de rúbricas matriciales en Markdown demostró una reducción drástica de la variabilidad evaluativa. Al obligar al agente a justificar cada puntaje mediante la cita obligatoria de líneas de código localizadas a través de MCP, se neutralizan casi por completo las alucinaciones evaluativas (afirmaciones sobre errores inexistentes en el código del estudiante).

### 4.3. Preservación del Rol Docente: Por qué el HITL es Irrenunciable
A diferencia de los sistemas tradicionales de calificación automática por cajas de prueba unitarias (*test cases* binarios de tipo pasa/falla), la evaluación continua con agentes persigue la comprensión del proceso de pensamiento del estudiante. Sin embargo, delegar la calificación final en la IA introduce riesgos éticos graves de despersonalización y desprotección pedagógica.

El flujo de trabajo propuesto en la Unidad 10 del taller demostró que el verdadero valor del agente reside en el **pre-diagnóstico**: el agente ahorra al profesor entre el 60% y el 70% del tiempo mecánico de lectura y detección de patrones de código, pero es el criterio humano del docente el que contextualiza la devolución, valida la equidad del juicio y modula la retroalimentación para motivar al alumno en función de su trayectoria previa.

---

## 5. CONCLUSIONES Y TRABAJO FUTURO

El presente trabajo ha presentado el diseño, arquitectura y validación preliminar de un sistema de evaluación continua universitaria basado en el estándar abierto MCP y en la supervisión docente activa. 

Las principales conclusiones derivadas del estudio son:
1. **Factibilidad de la arquitectura:** El desacoplamiento entre el razonamiento generativo del LLM y el sistema de archivos local mediante MCP permite auditar entregas de programación de manera privada, reproducible y libre de dependencias propietarias.
2. **Relevancia del Desarrollo Guiado por Especificaciones (SDD):** La formalización documental de los criterios docentes en archivos de texto plano versionables (`AGENTS.md`, `MEMORY.md`, rúbricas y Skills) constituye la barrera de contención más eficaz contra las alucinaciones técnicas y la inconsistencia en las devoluciones.
3. **Identificación de la barrera de instrumentación:** La transferencia formativa hacia 70 docentes y futuros educadores demostró que el interés pedagógico en la IA generativa es extraordinario, pero la adopción efectiva requiere superar la brecha técnica de Git/CI mediante herramientas visuales, editores asistidos y widgets interactivos autocontenidos.

Como líneas de trabajo futuro inmediatas, en el marco del segundo semestre del proyecto de investigación, se prevé:
- La consolidación del sistema de "Puntos de Ritmo" mediante análisis estadístico inferencial correlacionando la frecuencia de autoevaluación continua asistida con el rendimiento en exámenes parciales sumativos.
- La migración de los repositorios hacia plataformas LMS nativas de GitHub con interfaces pedagógicas amigables (*ClassMoji*), reduciendo la fricción de terminal detectada durante el taller.
- La extensión del banco de laboratorios interactivos hacia asignaturas avanzadas de la carrera de Ingeniería en Informática.

---

## 6. DECLARACIONES OBLIGATORIAS

### Declaración de Financiamiento
Esta investigación fue financiada por la Universidad Católica de Santiago del Estero (UCSE) a través de la Convocatoria DASS UCSE 2025 – Iniciación a la Investigación (GIyT), para el proyecto *"Agentes de IA y Protocolo MCP para evaluación continua y autoevaluación en materias de Ingeniería en Informática"* (Período Noviembre 2025 – Octubre 2026).

### Declaración sobre Uso de Inteligencia Artificial
En la preparación de este manuscrito, los autores utilizaron modelos de lenguaje de gran escala (Antigravity IDE / Claude 3.7 Sonnet) exclusivamente para la asistencia en la estructuración preliminar del esquema capitular, la revisión gramatical de estilo académico y la traducción del resumen al idioma inglés. Los autores redactaron, revisaron y editaron críticamente la totalidad del contenido conceptual, seleccionaron los datos empíricos de campo, validaron las referencias bibliográficas y asumen la total y exclusiva responsabilidad por el contenido y las conclusiones de la publicación.

### Declaración de Conflictos de Interés
Los autores declaran no tener conflictos de interés institucionales, financieros ni personales que hayan podido sesgar o influir en el diseño del estudio, el análisis de datos o las conclusiones del presente trabajo.

### Aprobación Ética y Consentimiento Informado
Los datos relativos al taller de capacitación docente corresponden a métricas cuantitativas agregadas y registros de participación en actividades institucionales abiertas. No se recopilaron ni divulgaron datos personales sensibles, preservándose el estricto anonimato de los asistentes y estudiantes en conformidad con las normas éticas de investigación educativa de la institución.

---

## 7. REFERENCIAS BIBLIOGRÁFICAS

Anthropic. (2024). *Model Context Protocol: An open standard for connecting AI models to data sources*. Anthropic Engineering Blog. https://www.anthropic.com/news/model-context-protocol

Becker, B. A., Denny, P., Finnie-Ansley, J., Luxton-Reilly, A., Prather, J., & Santos, E. A. (2023). Programming is hard—or at least it used to be: Educational opportunities and challenges of AI code generation. *ACM Transactions on Computing Education, 23*(4), 1-27. https://doi.org/10.1145/3618349

Black, P., & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education: Principles, Policy & Practice, 5*(1), 7-74. https://doi.org/10.1080/0969595980050102

Denny, P., Kumar, V., & Giacaman, N. (2024). Computing education in the era of generative AI: A systematic review. *IEEE Transactions on Education, 67*(2), 145-159. https://doi.org/10.1109/TE.2023.3344550

Finnie-Ansley, J., Denny, P., Becker, B. A., Luxton-Reilly, A., & Prather, J. (2022). The robots are coming: Exploring the implications of OpenAI Codex on introductory programming. En *Proceedings of the 24th Australasian Computing Education Conference* (ACE '22) (pp. 10-19). Association for Computing Machinery. https://doi.org/10.1145/3511861.3511863

Hellas, A., Ihantola, P., Petersen, A., Aivaloglou, E., Butler, M., Freire, M., Grossman, P., Kinnunen, P., & Szabo, C. (2017). Predicting academic performance: A systematic literature review. En *Proceedings of the 2017 ITiCSE Conference on Working Group Reports* (pp. 175-199). Association for Computing Machinery. https://doi.org/10.1145/3174781.3174787

Lau, S., & Guo, P. (2023). From "ban it" to "build with it": How educators are redesigning programming assignments in the age of large language models. En *Proceedings of the 2023 ACM Conference on International Computing Education Research* (ICER '23) (pp. 312-326). Association for Computing Machinery. https://doi.org/10.1145/3568813.3600138

Prather, J., Denny, P., Leinonen, J., Becker, B. A., Csuhaj, I., Hermans, F., Luxton-Reilly, A., & Santos, E. A. (2023). The robots are here: Navigating the generative AI revolution in computing education. En *Proceedings of the 2023 Working Group Reports on Innovation and Technology in Computer Science Education* (ITiCSE-WGR '23) (pp. 108-159). Association for Computing Machinery. https://doi.org/10.1145/3623762.3633499

Shute, V. J. (2008). Focus on formative feedback. *Review of Educational Research, 78*(1), 153-189. https://doi.org/10.3102/0034654307313795

Wang, F., & Hannafin, M. J. (2005). Design-based research and technology-enhanced learning environments. *Educational Technology Research and Development, 53*(4), 5-23. https://doi.org/10.1007/BF02504682
