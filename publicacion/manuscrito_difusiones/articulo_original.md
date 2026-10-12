# INTEGRACIÓN DE AGENTES DE INTELIGENCIA ARTIFICIAL Y PROTOCOLO MCP EN LA EVALUACIÓN CONTINUA UNIVERSITARIA: ARQUITECTURA TÉCNICA Y EXPERIENCIA DE TRANSFERENCIA DOCENTE

# *INTEGRATION OF ARTIFICIAL INTELLIGENCE AGENTS AND MCP PROTOCOL IN UNIVERSITY CONTINUOUS ASSESSMENT: TECHNICAL ARCHITECTURE AND TEACHER TRANSFER EXPERIENCE*

---

### RESUMEN
El avance acelerado de los Modelos de Lenguaje de Gran Escala (LLM) plantea desafíos sustanciales para las prácticas de evaluación en la enseñanza universitaria de la programación. Este trabajo tuvo como objetivo diseñar, implementar y evaluar preliminarmente una arquitectura sociotécnica basada en el Protocolo de Contexto de Modelo (*Model Context Protocol*, MCP) y el principio de supervisión docente activa (*Human-in-the-Loop*, HITL) para asistir la evaluación formativa continua, así como analizar las condiciones de transferibilidad de dicha propuesta en una experiencia de capacitación docente. Metodológicamente, se adoptó un enfoque de Investigación Basada en el Diseño (DBR) estructurado en tres fases secuenciales: diseño de artefactos de gobernanza contextual en texto plano (`AGENTS.md`, `MEMORY.md`, rúbricas analíticas y especificaciones formales de habilidades docentes), pilotaje curricular en asignaturas universitarias de programación y desarrollo de un taller intensivo de transferencia de diez horas reloj. La muestra estuvo constituida por 70 participantes sobre 80 personas inscriptas (tasa de asistencia del 87,5 %), integrada por profesores universitarios de ingeniería en informática y estudiantes avanzados de profesorado y licenciatura en informática educativa. La recolección de datos combinó telemetría del repositorio plantilla, registros de ejecución de integración continua en GitHub Actions y notas de campo estructuradas. Los resultados mostraron una amplia participación en los recursos interactivos desacoplados; no obstante, únicamente 1 de los 70 participantes completó de forma autónoma el flujo de integración continua durante el taller. Este hallazgo evidencia una pronunciada brecha de instrumentación técnica (*tooling gap*) vinculada a la fricción operativa del control de versiones por consola. La principal limitación radica en el carácter exploratorio del estudio y la ausencia de mediciones basales estandarizadas. Se concluye que la arquitectura proporciona bases operativas viables para encauzar la IA hacia una asistencia formativa supervisada, requiriendo interfaces visuales accesibles para su adopción generalizada.

**Palabras clave:** Evaluación formativa, Agentes de inteligencia artificial, Protocolo de contexto de modelo (MCP), Formación docente, Educación en ciencias de la computación.

---

### ABSTRACT
The rapid advancement of Large Language Models (LLMs) poses substantial challenges for traditional assessment practices in university computer science and programming education. This empirical study aimed to design, implement, and preliminarily evaluate a sociotechnical architecture based on the Model Context Protocol (MCP) and the active Human-in-the-Loop (HITL) principle to assist continuous formative assessment, as well as to analyze the transferability conditions of this approach within a teacher professional development context. Methodologically, the research adopted a Design-Based Research (DBR) framework structured across three sequential phases: the design of plain-text contextual governance artifacts (`AGENTS.md`, `MEMORY.md`, analytical rubrics, and formal teaching skill specifications), curricular piloting in university programming courses, and the delivery of an intensive ten-hour teacher training workshop. The study sample comprised 70 attendees out of 80 registered individuals (an 87.5% attendance rate), consisting of computer engineering faculty and advanced pre-service teachers from educational informatics degree programs. Data collection combined template repository telemetry metrics, continuous integration execution logs on GitHub Actions, and structured qualitative field observation notes. Findings showed broad participation in the decoupled interactive resources; however, only 1 of the 70 participants autonomously completed the continuous integration pipeline during the workshop. This outcome highlights a pronounced technical tooling gap associated with the operational friction of command-line version control tools. The main limitation lies in the exploratory nature of the study and the absence of standardized baseline measurements. We conclude that the architecture establishes viable operational foundations to guide AI toward supervised formative assistance, though accessible visual interfaces are essential for widespread faculty adoption.

**Keywords:** Formative assessment, Artificial intelligence agents, Model Context Protocol (MCP), Teacher training, Computer science education.

---

## 1. INTRODUCCIÓN

La masificación de los Modelos de Lenguaje de Gran Escala (LLM, por sus siglas en inglés) ha producido cambios sustanciales en la educación superior, con repercusiones inmediatas en las carreras de Ciencias de la Computación e Ingeniería en Informática (Becker et al., 2023; Denny et al., 2024). La capacidad demostrada por estos modelos para generar código sintáctica y semánticamente funcional, resolver problemas algorítmicos introductorios y explicar errores de depuración ha tensionado los esquemas tradicionales de evaluación sumativa basados en entregas asincrónicas de código fuente sin supervisión de procesos (Finnie-Ansley et al., 2022).

Frente a esta situación, se observan dos respuestas institucionales contrastantes en el ámbito universitario. Por una parte, posturas restrictivas han procurado limitar el uso de herramientas generativas mediante normativas punitivas o el regreso exclusivo a exámenes manuscritos presenciales; tales medidas resultan de difícil sostenimiento práctico, distancian la formación académica de las prácticas profesionales contemporáneas de la ingeniería de software y no garantizan el desarrollo del pensamiento crítico (Denny et al., 2024). Por otra parte, aproximaciones de adopción informal han promovido la interacción libre mediante interfaces de chat comercial (*prompts zero-shot*), introduciendo riesgos asociados con la generación de afirmaciones técnicas inexactas (alucinaciones), la variabilidad de criterios evaluativos, la falta de reproducibilidad y una delegación no supervisada del juicio pedagógico en sistemas propietarios (Lau & Guo, 2023).

En la didáctica de la programación, la evaluación continua y formativa busca proporcionar retroalimentación (*feedback*) accionable, dialógica y andamiada que permita a los estudiantes identificar modelos mentales erróneos y refactorizar sus soluciones algorítmicas de manera iterativa (Black & Wiliam, 1998; Shute, 2008). No obstante, en comisiones universitarias numerosas, la revisión exhaustiva y personalizada de entregas individuales impone una carga horaria que suele sobrepasar la disponibilidad del cuerpo docente.

La emergencia de agentes de inteligencia artificial y la reciente formalización del Protocolo de Contexto de Modelo (*Model Context Protocol* - MCP) ofrecen nuevas oportunidades para abordar este dilema (Anthropic, 2024). MCP es un estándar abierto de comunicación que permite estructurar la interoperabilidad entre modelos de razonamiento y fuentes externas de datos o herramientas locales (sistemas de archivos, analizadores estáticos o motores de pruebas). Esta característica técnica permite que un agente explore un entorno de desarrollo de forma estandarizada. Sin embargo, el protocolo por sí solo no garantiza pertinencia didáctica ni seguridad operativa si no está mediado por principios de Desarrollo Guiado por Especificaciones (*Spec-Driven Development* - SDD) y por una gobernanza estricta basada en el principio de supervisión docente activa (*Human-in-the-Loop* - HITL).

A partir de este contexto, el presente estudio se planteó como objetivo general: **diseñar, implementar y evaluar preliminarmente una arquitectura sociotécnica basada en MCP y supervisión docente activa para asistir la evaluación continua en asignaturas universitarias de programación, así como analizar las condiciones de transferibilidad de dicha propuesta en una experiencia de formación docente**.

Para orientar la investigación, se definieron tres preguntas de investigación:
- **PI1:** ¿Qué componentes técnicos y pedagógicos requiere una arquitectura basada en MCP para estructurar un proceso auditable de evaluación continua asistida por agentes?
- **PI2:** ¿Qué nivel de adopción instrumental y técnica alcanzan los participantes al interactuar con una plantilla basada en integración continua y agentes durante un taller de formación docente?
- **PI3:** ¿Qué barreras técnicas y pedagógicas emergen durante la interacción de los docentes con dicha infraestructura y qué andamiajes resultan pertinentes para mitigarlas?

---

## 2. MÉTODOS

### 2.1. Diseño de investigación
El estudio adoptó un enfoque de **Investigación Basada en el Diseño** (*Design-Based Research* - DBR) (Wang & Hannafin, 2005), de carácter descriptivo y exploratorio. Este marco metodológico es idóneo para la ingeniería educativa debido a su estructura iterativa de ciclos de análisis de necesidades, diseño colaborativo de intervenciones sociotécnicas, implementación en contextos educativos reales y refinamiento de principios teóricos y artefactos prácticos.

### 2.2. Contexto y fases del estudio
La investigación se desarrolló durante el ciclo lectivo 2026 en el marco de un proyecto de iniciación a la investigación acreditado institucionalmente, articulado en tres fases sucesivas:

1. **Fase 1: Diseño de la arquitectura y artefactos (Marzo - Mayo 2026):** Definición de la estructura de tres capas, formalización de directivas en archivos de texto plano (`AGENTS.md`, `MEMORY.md`), rediseño de rúbricas analíticas matriciales y especificación de habilidades docentes estandarizadas para el análisis de código fuente.
2. **Fase 2: Pilotaje curricular preliminar (Junio - Agosto 2026):** Aplicación exploratoria de la arquitectura en dos cursos de programación de una institución universitaria privada: *Programación II* (3° año de Ingeniería en Informática, orientada a desarrollo web con HTML semántico, CSS y JavaScript) y *Algoritmos y Programación* (1° año de Ingeniería en Informática, orientada a modularización algorítmica y arreglos en C++). En esta fase se utilizaron los agentes para generar borradores periciales de prediagnóstico técnico sobre tareas prácticas, los cuales fueron supervisados por el equipo docente a cargo antes de interactuar con los estudiantes. Asimismo, se adaptaron recursos de apoyo complementarios en áreas de sistemas operativos y estructuras de datos para ensayar la versatilidad de las especificaciones.
3. **Fase 3: Transferencia formativa y estudio de adopción (Octubre 2026):** Diseño y dictado de un taller intensivo de capacitación docente de diez horas reloj presenciales/sincrónicas orientado a profesores universitarios y estudiantes avanzados en formación docente.

### 2.3. Participantes
La convocatoria al taller de capacitación fue abierta, institucional y de carácter voluntario. Se registraron 80 personas inscriptas, de las cuales 70 asistieron activamente a las sesiones de trabajo, lo que representó una tasa de asistencia del 87,5 %. 

La muestra estuvo integrada por dos grupos diferenciados:
- **Grupo 1 (Docentes universitarios en ejercicio):** Profesores y auxiliares de cátedras del área de informática y computación pertenecientes a una universidad de gestión privada de la región (n = 28; 40,0 % de los asistentes).
- **Grupo 2 (Formadores en informática en etapa de graduación):** Estudiantes avanzados de los dos últimos años y graduados recientes de las carreras de Profesorado Universitario en Informática y Licenciatura en Informática Educativa pertenecientes a una universidad nacional pública de la misma región geográfica (n = 42; 60,0 % de los asistentes).

No se aplicaron pruebas diagnósticas previas estandarizadas de dominio en herramientas de control de versiones (Git/CLI) o interfaces de agentes, registrándose durante las sesiones una marcada heterogeneidad en las competencias instrumentales de partida.

### 2.4. Arquitectura sociotécnica e instrumentos
La arquitectura desarrollada desacopla la inteligencia generativa de la lógica pedagógica mediante tres capas operativas:

**Figura 1**  
*Arquitectura sociotécnica de tres capas para la evaluación continua asistida por agentes*  
[Insertar Figura 1 aquí]  
*Nota.* Elaboración propia con base en las directrices del estándar abierto MCP (Anthropic, 2024) y los principios HITL.

1. **Capa de Gobernanza Contextual:** 
   - `AGENTS.md`: Establece el rol pedagógico del agente, estipulando explícitamente el uso de metodologías formativas socráticas, la restricción de proveer soluciones completas o código corregido directamente y la exigencia de asociar cada observación a evidencias verificables en el código.
   - `MEMORY.md`: Archivo de persistencia de contexto que almacena acuerdos curriculares, restricciones del compilador o estándares de estilo adoptados por la cátedra.
   - Rúbricas Analíticas en Markdown: Matrices con criterios descriptivos y niveles de desempeño observables.
   - Habilidades Docentes (*Skills*): Archivos de instrucciones operativas con metadatos YAML (*frontmatter*), delimitadores de secciones (`<contexto>`, `<restricciones>`, `<procedimiento>`) y esquemas de salida estructurada.
2. **Capa de Interoperabilidad Protocolizada (MCP):**
   Conexión local entre el entorno de desarrollo y un servidor MCP de sistema de archivos (*Filesystem Server*). La herramienta permite al agente listar directorios y leer archivos de código de forma estandarizada. En términos de seguridad informática, conforme a las directrices de OWASP (2025), la configuración requirió restringir la ejecución a rutas locales aisladas, aplicar privilegios mínimos y establecer listas de directorios permitidos, con el propósito de reducir el riesgo de exposición de credenciales y accesos no autorizados al sistema operativo.
3. **Capa de Supervisión Docente (*Human-in-the-Loop*):**
   Mecanismo de gobernanza mediante el cual el agente genera únicamente un borrador de prediagnóstico técnico. El docente verifica la existencia de las evidencias citadas, modula el tono comunicacional y aprueba la devolución definitiva.

Como instrumentos de transferencia y recolección se diseñaron:
- **Repositorio Plantilla Abierto:** Entorno de trabajo estructurado en GitHub conteniendo guías del taller, directorios de referencia, un evaluador automático en Python (`autograder_taller.py`) y un flujo de trabajo de integración continua en GitHub Actions configurado para una escala de 100 puntos.
- **Colección de Widgets Interactivos Desacoplados:** Banco de 35 actividades didácticas implementadas en HTML/CSS/JS autocontenidas en archivos locales, concebidas para ejecutarse directamente en el navegador sin dependencias de consola o servidores.

### 2.5. Procedimiento del taller
El taller se estructuró en dos jornadas consecutivas de cinco horas reloj cada una:
- **Jornada 1 (Fundamentos y Persistencia):** Presentación del protocolo MCP, configuración del agente en el entorno de desarrollo, creación de `AGENTS.md`, `MEMORY.md`, programa analítico y resolución del cuestionario interactivo de fundamentos (acumulando 60 puntos en el evaluador).
- **Jornada 2 (Skills Avanzadas y Laboratorio Integrador):** Construcción guiada del Trabajo Práctico 1 (`rubrica.md`, 20 puntos) y de la habilidad formal de evaluación (`skill_evaluador.md`, 20 puntos) utilizando plantillas predefinidas del toolkit docente, finalizando con la verificación de la suite de pruebas local (`python autograder_taller.py`) y la sincronización con el repositorio remoto.

### 2.6. Fuentes y análisis de datos
Para responder a las preguntas de investigación se triangularon tres fuentes de datos:
1. **Telemetría y registros de actividad en repositorios:** Seguimiento de bifurcaciones (*forks*), confirmaciones de cambios (*commits*) y registros de ejecución de integración continua en GitHub Actions generados por los participantes durante las sesiones sincrónicas.
2. **Notas de campo estructuradas:** Registros sistemáticos tomados por el equipo capacitador durante el desarrollo del taller, focalizados en los momentos de bloqueo procedimental, consultas reiteradas y verbalizaciones de los asistentes.
3. **Registro de consultas e incidencias técnicas:** Documentación de dudas formuladas durante las instancias prácticas de laboratorio.

El análisis de los registros cuantitativos fue de carácter descriptivo (frecuencias absolutas y porcentajes). Las notas de campo y las consultas se sometieron a un análisis temático cualitativo mediante codificación inductiva abierta, realizada por dos integrantes del equipo investigador a partir del conjunto completo de notas de campo e incidencias registradas durante ambas jornadas; posteriormente, los códigos afines se agruparon en los tres patrones temáticos informados.

### 2.7. Consideraciones éticas
El estudio utilizó registros agregados de asistencia, métricas técnicas anonimizadas y notas de campo procedentes de una actividad formativa voluntaria. Antes del desarrollo del taller, los participantes fueron informados sobre el propósito pedagógico e investigativo de la experiencia y sobre el tratamiento agregado de los resultados. No se recopilaron nombres de usuario, datos personales sensibles ni información que permitiera vincular los resultados publicados con participantes individuales. La actividad no tuvo consecuencias académicas ni evaluativas. Debido a su carácter de innovación educativa desarrollada en un contexto formativo ordinario, el estudio no fue sometido a evaluación previa por un comité de ética institucional.

---

## 3. RESULTADOS

### 3.1. Arquitectura técnica y ecosistema de recursos desarrollados (PI1)
En respuesta a la primera pregunta de investigación, la implementación permitió operacionalizar la separación entre las reglas pedagógicas almacenadas en archivos de especificación y la capacidad generativa del modelo. 

A través del protocolo MCP, el agente accedió a las soluciones de código ubicadas en carpetas locales, contrastándolas contra los criterios expresados en `rubrica.md` y generando borradores de devolución que citaban números de línea concretos. La formalización mediante habilidades estructuradas favoreció que los prediagnósticos conservaran una estructura común compuesta por: (a) identificación de fortalezas observadas, (b) señalamiento de inconsistencias algorítmicas con cita textual de código y (c) formulación de preguntas orientadoras para la corrección autónoma.

Asimismo, se desarrolló un banco de recursos didácticos de transferencia estructurado en 35 aplicaciones interactivas web autocontenidas para *Algoritmos y Programación*, complementado con módulos de prueba en estructuras dinámicas, simulaciones estocásticas y verificación de permisos en sistemas operativos.

### 3.2. Participación y adopción instrumental durante el taller (PI2)
La convocatoria registró 80 postulantes y 70 asistentes efectivos durante las dos jornadas (tasa de asistencia del 87,5 %). Sin embargo, la interacción con la infraestructura técnica del repositorio plantilla reveló una dinámica disímil en función de las herramientas empleadas.

La Tabla 1 resume los niveles de progresión observados entre los participantes durante el tiempo sincrónico de las sesiones de laboratorio.

**Tabla 1**  
*Progresión de los participantes en las actividades técnicas del taller (N = 70)*

| Nivel de progresión técnica | Frecuencia (n) | Porcentaje (%) |
| :--- | :---: | :---: |
| Asistentes presentes en el taller | 70 | 100,0 % |
| Acceso y clonación del repositorio plantilla | 41 | 58,6 % |
| Resolución del cuestionario web interactivo (`index.html`) | 52 | 74,3 % |
| Ejecución local del evaluador (`autograder_taller.py`) | 19 | 27,1 % |
| Realización de al menos un *commit* local | 14 | 20,0 % |
| Envío exitoso de cambios a GitHub (*push*) | 6 | 8,6 % |
| Culminación integral autónoma del flujo CI/CD (100 pts) | 1 | 1,4 % |

*Nota.* Las categorías no representan etapas mutuamente excluyentes ni necesariamente acumulativas. El cuestionario web interactivo también estuvo disponible mediante acceso directo desde el navegador (sin requerir clonación previa del repositorio). Los datos de acceso al repositorio y ejecuciones de integración continua se obtuvieron de la telemetría de GitHub Actions, mientras que las acciones locales (ejecución de scripts y confirmación de cambios) fueron registradas mediante observación directa y asistencia técnica en el aula. Se consideró culminación autónoma la obtención de 100 puntos en GitHub Actions durante el horario sincrónico del taller, sin intervención directa del equipo capacitador sobre el equipo, los archivos o los comandos ejecutados por el participante.

Como se observa en la Tabla 1, mientras que el 74,3 % de los asistentes resolvió con éxito las actividades conceptuales provistas mediante la interfaz web desacoplada (`index.html`), únicamente 6 personas (8,6 %) lograron sincronizar cambios remotos hacia GitHub, y **un único participante (1,4 %) completó de manera plenamente autónoma la totalidad de los requisitos verificados por GitHub Actions (100 puntos)** durante el horario del taller.

### 3.3. Factores asociados a la adopción y barreras emergentes (PI3)
El análisis temático de las notas de campo y las consultas de los participantes permitió identificar tres patrones recurrentes asociados con la brecha observada en la culminación del flujo técnico:

1. **Fricción instrumental con el ecosistema de control de versiones (Git/CLI):** El principal factor asociado con la interrupción de la progresión práctica no estuvo relacionado con consultas sobre la comprensión de MCP, sino con incidentes instrumentales registrados durante el uso de la terminal: errores en la autenticación de cuentas mediante tokens de acceso personal en GitHub, fallas de sintaxis en comandos de consola y desorientación ante mensajes de conflicto entre ramas locales y remotas.
2. **Modalidad de participación predominantemente observacional:** En las notas de campo se registraron casos reiterados de participantes que siguieron las demostraciones del instructor en pantalla, tomaron notas metodológicas y postergaron la configuración en sus propios equipos para una instancia posterior sin presión sincrónica.
3. **Disposición favorable hacia interfaces interactivas desacopladas:** Se observó una marcada fluidez operativa cuando los participantes interactuaron con los widgets web en HTML/JS. Al no requerir dependencias de compilación ni ejecución de comandos de consola, estos recursos permitieron a los asistentes validar conceptos algorítmicos y de evaluación sin experimentar bloqueos técnicos.

---

## 4. DISCUSIÓN

### 4.1. La brecha de instrumentación (*Tooling Gap*) como factor crítico
El marcado contraste entre la elevada asistencia e interés manifestado por la cohorte (87,5 %) y la baja culminación sincrónica del pipeline automatizado en GitHub Actions (1,4 %) constituye el hallazgo empírico más relevante de la experiencia.

En el campo de la educación en informática, investigaciones previas han señalado que la incorporación de herramientas profesionales de integración continua en entornos formativos iniciales suele introducir una sobrecarga cognitiva secundaria que compite con los objetivos pedagógicos centrales (Buffardi et al., 2020). Los resultados de este estudio sugieren que dicho fenómeno se reproduce de manera acentuada en la formación docente: cuando se intenta capacitar en el diseño de agentes de IA y se exige simultáneamente el dominio de flujos completos de Git y terminal, la fricción instrumental inhibe la apropiación pedagógica.

Este hallazgo fundamenta la necesidad de repensar los canales de entrega. Para que arquitecturas basadas en MCP puedan ser adoptadas de forma amplia por docentes universitarios de diversas disciplinas, es imprescindible encapsular la complejidad de la consola de comandos mediante editores con interfaces gráficas amigables, extensiones integradas o plataformas de aprendizaje nativas que no requieran manipulación directa de flujos Git de bajo nivel.

### 4.2. Especificaciones formales y consistencia en los prediagnósticos
Durante las pruebas de pilotaje curricular en *Programación II* y *Algoritmos y Programación*, se observó una mayor consistencia aparente en la estructura de los borradores de evaluación cuando el agente operó subordinado a archivos `AGENTS.md` y rúbricas analíticas formalizadas. 

La exigencia protocolizada de vincular cada dictamen a evidencias localizables en el código facilitó la labor docente de detección de afirmaciones erróneas y redujo el riesgo de aceptar alucinaciones evaluativas no verificadas. Al limitar las herramientas del agente a la inspección pericial mediante MCP, se restringió operativamente la generación directa de soluciones completas y se orientó la respuesta hacia observaciones diagnósticas y preguntas de andamiaje. No obstante, esta consistencia observada requiere ser validada en investigaciones futuras mediante coeficientes estandarizados de concordancia interjueces y diseños cuasiexperimentales controlados.

### 4.3. Supervisión humana (*Human-in-the-Loop*) y gobernanza ética
La experiencia respalda el uso de los agentes como asistentes de diagnóstico preliminar, manteniendo la decisión evaluativa final bajo responsabilidad docente. Durante el pilotaje, el equipo docente percibió que el prediagnóstico asistido disminuía el trabajo rutinario de localización y cotejo de patrones de código; sin embargo, esta percepción no fue cuantificada mediante un protocolo temporal controlado.

Delegar la retroalimentación final directamente en un modelo generativo sin intervención humana vulnera el principio de responsabilidad pedagógica e incrementa la desprotección del estudiante ante eventuales sesgos algorítmicos. La supervisión activa no representa un obstáculo burocrático, sino la condición indispensable para que la tecnología opere de manera ética y formativamente significativa.

### 4.4. Implicaciones para la formación docente en informática
La interacción entre docentes de ingeniería en ejercicio y futuros formadores en informática educativa permitió observar aportes potencialmente complementarios para la innovación educativa. Las notas de campo sugirieron diferencias de énfasis entre ambos perfiles: en las intervenciones de participantes vinculados con ingeniería se registraron consultas relacionadas con el control sintáctico y el aislamiento de entornos, mientras que entre los perfiles de formación pedagógica fueron recurrentes las preguntas sobre rúbricas, lenguaje de retroalimentación y accesibilidad. Integrar ambas miradas resulta imprescindible para evitar tanto el determinismo técnico como la adopción pedagógica ingenua de la IA.

### 4.5. Limitaciones del estudio
Los hallazgos del presente trabajo deben interpretarse a la luz de diversas limitaciones metodológicas:
1. **Muestra intencional y localizada:** La población del taller estuvo conformada por una muestra no probabilística de participantes pertenecientes a dos instituciones de una misma región, lo que restringe la generalización de los resultados.
2. **Diseño descriptivo sin grupo de comparación:** La investigación no contempló un grupo de control ni mediciones de tipo pretest/postest para evaluar cuantitativamente el aprendizaje o la ganancia de competencias en comparación con metodologías formativas tradicionales.
3. **Ausencia de mediciones de línea de base:** No se aplicó un instrumento previo estandarizado para cuantificar el nivel de competencia de los participantes en herramientas de control de versiones (Git) o en el uso de IA generativa, lo que impide aislar con precisión el peso relativo de las habilidades previas sobre la baja culminación del pipeline.
4. **Restricción temporal del taller:** La duración de diez horas reloj concentradas en dos jornadas consecutivas pudo haber acentuado la sobrecarga cognitiva, limitando el tiempo disponible para la resolución autónoma de contingencias técnicas complejas.
5. **Doble rol del equipo investigador:** La participación de los investigadores como diseñadores de la arquitectura, docentes a cargo del pilotaje y capacitadores en el taller introduce un potencial sesgo de observación, atenuado parcialmente mediante el uso de registros técnicos automatizados.
6. **Carácter preliminar del análisis temporal:** Las observaciones sobre el ahorro de tiempo docente en la revisión son cualitativas y proceden de la experiencia de pilotaje, no habiendo sido sometidas a un protocolo formal de cronometraje y comparación experimental.

---

## 5. CONCLUSIONES Y TRABAJO FUTURO

El presente artículo expuso el diseño, implementación y estudio de transferencia de una arquitectura sociotécnica para la evaluación continua asistida por agentes de inteligencia artificial en programación universitaria, basada en el Protocolo de Contexto de Modelo (MCP), especificaciones en texto plano (`AGENTS.md`, `MEMORY.md`, rúbricas analíticas) y supervisión docente activa (*Human-in-the-Loop*).

Las principales conclusiones son:
1. **Viabilidad técnica y pedagógica:** La articulación entre MCP y especificaciones estructuradas permite inspeccionar entornos locales de código de manera auditable y reducir el acoplamiento con integraciones propietarias específicas, siempre que el servidor opere con rutas restringidas, privilegios mínimos y mecanismos adecuados de protección de credenciales.
2. **Relevancia del prediagnóstico asistido:** La subordinación del agente a un rol de asistente pericial supervisado preserva la autoridad pedagógica docente, favoreciendo una retroalimentación formativa contextualizada y sometida a revisión ética y pedagógica humana.
3. **Identificación de la brecha instrumental:** El estudio identificó la fricción asociada con Git y la consola como el principal cuello de botella observado durante el taller, validando la conveniencia de desarrollar interfaces visuales y recursos desacoplados que faciliten una apropiación pedagógica gradual.

Como líneas de trabajo futuro se plantean:
- El desarrollo de estudios cuasiexperimentales con seguimiento temporal y grupos de control para medir el impacto de la retroalimentación asistida sobre el rendimiento académico final de los estudiantes.
- La evaluación de plataformas educativas e interfaces gráficas simplificadas que permitan operar con el protocolo MCP reduciendo la fricción de consola detectada.
- La profundización en estudios de concordancia interjueces para cuantificar la consistencia evaluativa alcanzada mediante el uso de especificaciones matriciales formales.

---

## 6. DECLARACIONES OBLIGATORIAS

### Declaración de financiamiento
La información completa sobre la entidad de financiamiento, convocatoria y código del proyecto institucional fue suministrada al Comité Editorial en la sección de metadatos de la plataforma y se incorporará al manuscrito tras la finalización del proceso de evaluación por pares.

### Declaración sobre uso de inteligencia artificial
Durante la preparación del manuscrito, los autores utilizaron el entorno Antigravity IDE y el modelo Claude 3.7 Sonnet para asistir en la organización preliminar del texto, la revisión gramatical de estilo académico en español y la traducción del resumen al inglés. Los autores redactaron, revisaron y editaron críticamente la totalidad del contenido conceptual, definieron el diseño metodológico, analizaron los datos empíricos de campo, verificaron las referencias bibliográficas y asumen total responsabilidad por el contenido de la publicación.

### Aprobación ética
El estudio utilizó registros agregados de asistencia, métricas técnicas anonimizadas y notas de campo procedentes de una actividad formativa voluntaria. Antes del desarrollo del taller, los participantes fueron informados sobre el propósito pedagógico e investigativo de la experiencia y sobre el tratamiento agregado de los resultados. No se recopilaron nombres de usuario, datos personales sensibles ni información que permitiera vincular los resultados publicados con participantes individuales. La actividad no tuvo consecuencias académicas ni evaluativas. Debido a su carácter de innovación educativa desarrollada en un contexto formativo ordinario, el estudio no fue sometido a evaluación previa por un comité de ética institucional.

---

## 7. AGRADECIMIENTOS
*(Esta sección se incorporará formalmente tras la culminación del proceso de evaluación por pares a doble ciego).*

---

## 8. REFERENCIAS BIBLIOGRÁFICAS

Anthropic. (2024). *Model Context Protocol: An open standard for connecting AI models to data sources*. Anthropic Engineering Blog. https://www.anthropic.com/news/model-context-protocol

Becker, B. A., Denny, P., Finnie-Ansley, J., Luxton-Reilly, A., Prather, J., & Santos, E. A. (2023). Programming is hard—or at least it used to be: Educational opportunities and challenges of AI code generation. En *Proceedings of the 54th ACM Technical Symposium on Computer Science Education V. 1* (SIGCSE 2023) (pp. 500-506). Association for Computing Machinery. https://doi.org/10.1145/3545945.3569759

Black, P., & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education: Principles, Policy & Practice, 5*(1), 7-74. https://doi.org/10.1080/0969595980050102

Buffardi, K., Valdivia, P., & Rogers, D. (2020). Guerrilla testing: Effective software testing in CS1. En *Proceedings of the 51st ACM Technical Symposium on Computer Science Education* (SIGCSE '20) (pp. 377-383). Association for Computing Machinery. https://doi.org/10.1145/3328778.3366867

Denny, P., Prather, J., Becker, B. A., Finnie-Ansley, J., Blum, A., Luxton-Reilly, A., MacNeil, S., Petersen, A., Reeves, M., & Santos, E. A. (2024). Computing education in the era of generative AI. *Communications of the ACM, 67*(2), 56-67. https://doi.org/10.1145/3624720

Finnie-Ansley, J., Denny, P., Becker, B. A., Luxton-Reilly, A., & Prather, J. (2022). The robots are coming: Exploring the implications of OpenAI Codex on introductory programming. En *Proceedings of the 24th Australasian Computing Education Conference* (ACE '22) (pp. 10-19). Association for Computing Machinery. https://doi.org/10.1145/3511861.3511863

Lau, S., & Guo, P. J. (2023). From "ban it till we understand it" to "resistance is futile": How university programming instructors plan to adapt as more students use AI code generation and explanation tools such as ChatGPT and GitHub Copilot. En *Proceedings of the 2023 ACM Conference on International Computing Education Research V. 1* (ICER '23) (pp. 106-121). Association for Computing Machinery. https://doi.org/10.1145/3568813.3600138

OWASP. (2025). *Model Context Protocol (MCP) Security Cheat Sheet*. Open Web Application Security Project. https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html

Shute, V. J. (2008). Focus on formative feedback. *Review of Educational Research, 78*(1), 153-189. https://doi.org/10.3102/0034654307313795

Wang, F., & Hannafin, M. J. (2005). Design-based research and technology-enhanced learning environments. *Educational Technology Research and Development, 53*(4), 5-23. https://doi.org/10.1007/BF02504682
