# INTEGRACIÓN DE AGENTES DE INTELIGENCIA ARTIFICIAL Y PROTOCOLO MCP EN LA EVALUACIÓN CONTINUA UNIVERSITARIA: ARQUITECTURA TÉCNICA, GOBERNANZA CONTEXTUAL Y REQUISITOS DE SEGURIDAD

# *INTEGRATION OF ARTIFICIAL INTELLIGENCE AGENTS AND THE MODEL CONTEXT PROTOCOL IN CONTINUOUS UNIVERSITY ASSESSMENT: TECHNICAL ARCHITECTURE, CONTEXTUAL GOVERNANCE, AND SECURITY REQUIREMENTS*

---

### RESUMEN
El avance acelerado de los Modelos de Lenguaje de Gran Escala (LLM) plantea desafíos sustanciales para las prácticas de evaluación en la enseñanza universitaria de la programación. Este artículo técnico presenta el diseño y la implementación de una arquitectura sociotécnica basada en el Protocolo de Contexto de Modelo (*Model Context Protocol*, MCP) y en el principio de supervisión docente activa (*Human-in-the-Loop*, HITL) para asistir la evaluación formativa continua. La arquitectura se organiza en tres capas: gobernanza contextual mediante archivos de texto plano (`AGENTS.md`, `MEMORY.md`, rúbricas analíticas y especificaciones formales de habilidades), interoperabilidad protocolizada con un servidor MCP de sistema de archivos restringido a rutas permitidas y privilegios mínimos, y supervisión docente de los borradores de prediagnóstico generados por el agente. Se describen, además, los instrumentos de transferencia desarrollados: un repositorio plantilla con evaluador automático en Python y flujo de integración continua en GitHub Actions sobre una escala de 100 puntos, y una colección de 35 aplicaciones web interactivas autocontenidas. El trabajo adopta un enfoque de Investigación Basada en el Diseño (DBR) y documenta un pilotaje curricular en dos asignaturas de programación y el diseño de un taller de transferencia de diez horas reloj, sin presentar datos ni observaciones de participantes como resultados de investigación. Se discuten los requisitos de seguridad conforme a las recomendaciones de OWASP y las implicancias de diseño derivadas de la literatura sobre carga cognitiva y dificultades instrumentales con el control de versiones. Las principales limitaciones son la ausencia de evaluación empírica con participantes, de medición de la calidad pedagógica de las devoluciones y de concordancia con evaluadores humanos. Se concluye que la arquitectura ofrece una base técnica viable y auditable para encauzar la IA hacia una asistencia formativa supervisada, cuya eficacia pedagógica deberá evaluarse en estudios posteriores con las garantías éticas correspondientes.

**Palabras clave:** Evaluación formativa, Agentes de inteligencia artificial, Protocolo de contexto de modelo (MCP), Formación docente, Educación en ciencias de la computación.

---

### ABSTRACT
The rapid advancement of Large Language Models (LLMs) poses substantial challenges for assessment practices in university programming education. This technical paper presents the design and implementation of a sociotechnical architecture based on the Model Context Protocol (MCP) and the active Human-in-the-Loop (HITL) principle to support continuous formative assessment. The architecture comprises three layers: contextual governance through plain-text files (`AGENTS.md`, `MEMORY.md`, analytical rubrics, and formal skill specifications), protocolized interoperability through a file-system MCP server restricted to allowed paths and least privileges, and teacher supervision of the diagnostic drafts produced by the agent. The paper also describes the transfer instruments developed: a template repository with a Python autograder and a GitHub Actions continuous integration workflow on a 100-point scale, and a collection of 35 self-contained interactive web applications. Following a Design-Based Research (DBR) approach, it documents a curricular pilot in two programming courses and the design of a ten-hour transfer workshop, without presenting data or observations from participants as research results. Security requirements are discussed in line with OWASP recommendations, together with design implications drawn from the literature on cognitive load and the instrumental difficulties of version control systems. The main limitations are the absence of empirical evaluation with participants, of measures of the pedagogical quality of the feedback, and of agreement with human raters, so no claims are made about learning outcomes or adoption. We conclude that the architecture offers a viable and auditable technical basis for steering AI toward supervised formative assistance, whose pedagogical effectiveness must be assessed in subsequent studies with appropriate ethical safeguards.

**Keywords:** Formative assessment, Artificial intelligence agents, Model Context Protocol (MCP), Teacher training, Computer science education.

---

## 1. INTRODUCCIÓN

La masificación de los Modelos de Lenguaje de Gran Escala (LLM, por sus siglas en inglés) ha producido cambios sustanciales en la educación superior, con repercusiones inmediatas en las carreras de Ciencias de la Computación e Ingeniería en Informática (Becker et al., 2023; Denny et al., 2024). La capacidad demostrada por estos modelos para generar código sintáctica y semánticamente funcional, resolver problemas algorítmicos introductorios y explicar errores de depuración ha tensionado los esquemas tradicionales de evaluación sumativa basados en entregas asincrónicas de código fuente sin supervisión de procesos (Finnie-Ansley et al., 2022).

Frente a esta situación, se observan dos respuestas institucionales contrastantes en el ámbito universitario. Por una parte, posturas restrictivas han procurado limitar el uso de herramientas generativas mediante normativas punitivas o el regreso exclusivo a exámenes manuscritos presenciales; tales medidas resultan de difícil sostenimiento práctico, distancian la formación académica de las prácticas profesionales contemporáneas de la ingeniería de software y no garantizan el desarrollo del pensamiento crítico (Denny et al., 2024). Por otra parte, aproximaciones de adopción informal han promovido la interacción libre mediante interfaces de chat comercial (*prompts zero-shot*), introduciendo riesgos asociados con la generación de afirmaciones técnicas inexactas (alucinaciones), la variabilidad de criterios evaluativos, la falta de reproducibilidad y una delegación no supervisada del juicio pedagógico en sistemas propietarios (Lau & Guo, 2023).

En la didáctica de la programación, la evaluación continua y formativa busca proporcionar retroalimentación (*feedback*) accionable, dialógica y andamiada que permita a los estudiantes identificar modelos mentales erróneos y refactorizar sus soluciones algorítmicas de manera iterativa (Black & Wiliam, 1998; Shute, 2008). No obstante, en comisiones universitarias numerosas, la revisión exhaustiva y personalizada de entregas individuales impone una carga horaria que suele sobrepasar la disponibilidad del cuerpo docente.

La emergencia de agentes de inteligencia artificial y la reciente formalización del Protocolo de Contexto de Modelo (*Model Context Protocol* - MCP) ofrecen nuevas oportunidades para abordar este dilema (Anthropic, 2024). MCP es un estándar abierto de comunicación que permite estructurar la interoperabilidad entre modelos de razonamiento y fuentes externas de datos o herramientas locales (sistemas de archivos, analizadores estáticos o motores de pruebas). Esta característica técnica permite que un agente explore un entorno de desarrollo de forma estandarizada. Sin embargo, el protocolo por sí solo no garantiza pertinencia didáctica ni seguridad operativa si no está mediado por principios de Desarrollo Guiado por Especificaciones (*Spec-Driven Development* - SDD) y por una gobernanza estricta basada en el principio de supervisión docente activa (*Human-in-the-Loop* - HITL).

A partir de este contexto, el presente artículo técnico tiene como objetivo general: **diseñar e implementar una arquitectura sociotécnica basada en MCP y supervisión docente activa para asistir la evaluación formativa continua en asignaturas universitarias de programación, así como describir sus instrumentos de transferencia y sus requisitos de seguridad y gobernanza**.

Para orientar el trabajo, se definieron tres preguntas:
- **PI1:** ¿Qué componentes técnicos y pedagógicos requiere una arquitectura basada en MCP para estructurar un proceso auditable de evaluación continua asistida por agentes?
- **PI2:** ¿Qué requisitos de seguridad y gobernanza debe satisfacer la configuración MCP para operar de manera auditable en entornos locales de evaluación?
- **PI3:** ¿Qué recursos y rutas de transferencia se diseñaron para facilitar la apropiación de la arquitectura por parte de docentes y qué consideraciones de diseño derivan de la literatura?

---

## 2. MÉTODOS

### 2.1. Diseño de investigación
El trabajo adoptó un enfoque de **Investigación Basada en el Diseño** (*Design-Based Research* - DBR) (Wang & Hannafin, 2005), de carácter descriptivo y orientado al diseño de artefactos. Este marco metodológico es idóneo para la ingeniería educativa debido a su estructura iterativa de ciclos de análisis de necesidades, diseño colaborativo de intervenciones sociotécnicas, implementación en contextos educativos reales y refinamiento de principios teóricos y artefactos prácticos.

La lógica iterativa propia de la DBR se materializó en el refinamiento progresivo de los artefactos entre las fases: las dificultades identificadas durante el pilotaje curricular permitieron ajustar las restricciones de `AGENTS.md`, reorganizar las rúbricas y simplificar las plantillas del repositorio de transferencia.

El alcance del trabajo se circunscribe a la descripción de la arquitectura, de sus artefactos de gobernanza, de la configuración MCP, del repositorio con su flujo de integración continua y de los requisitos de seguridad. No se evaluaron la calidad pedagógica de las devoluciones generadas, su concordancia con evaluadores humanos, la mejora del aprendizaje ni el ahorro efectivo de tiempo docente, y no se presentan datos ni observaciones de participantes humanos como resultados de investigación.

### 2.2. Contexto y fases del estudio
La investigación se desarrolló durante el ciclo lectivo 2026 en el marco de un proyecto de investigación acreditado institucionalmente, articulado en tres fases sucesivas:

1. **Fase 1: Diseño de la arquitectura y artefactos (marzo - mayo de 2026):** Definición de la estructura de tres capas, formalización de directivas en archivos de texto plano (`AGENTS.md`, `MEMORY.md`), rediseño de rúbricas analíticas matriciales y especificación de habilidades docentes estandarizadas para el análisis de código fuente.
2. **Fase 2: Pilotaje curricular preliminar (junio - agosto de 2026):** Aplicación exploratoria de la arquitectura en dos cursos de programación de una institución universitaria privada: *Programación II* (3° año de Ingeniería en Informática, orientada a desarrollo web con HTML semántico, CSS y JavaScript) y *Algoritmos y Programación* (1° año de Ingeniería en Informática, orientada a modularización algorítmica y arreglos en C++). En esta fase se utilizaron los agentes para generar borradores periciales de prediagnóstico técnico (entendido como un análisis técnico preliminar de una entrega, sin valor evaluativo definitivo hasta su revisión docente) sobre tareas prácticas, los cuales fueron supervisados por el equipo docente a cargo antes de interactuar con los estudiantes. Asimismo, se adaptaron recursos de apoyo complementarios en áreas de sistemas operativos y estructuras de datos para ensayar la versatilidad de las especificaciones.
3. **Fase 3: Diseño de la experiencia de transferencia (octubre de 2026):** Diseño y dictado de un taller intensivo de capacitación docente de diez horas reloj presenciales/sincrónicas orientado a profesores universitarios y estudiantes avanzados en formación docente. Esta fase se describe como parte del diseño de los recursos de transferencia; no se informan datos ni observaciones de los asistentes como resultados.

### 2.3. Arquitectura sociotécnica e instrumentos
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
   Conexión local entre el entorno de desarrollo y un servidor MCP de sistema de archivos (*Filesystem Server*). La herramienta permite al agente listar directorios y leer archivos de código de forma estandarizada. En términos de seguridad informática, conforme a las directrices de OWASP (2025), la configuración se diseñó para requerir la restricción de la ejecución a rutas locales aisladas, la aplicación de privilegios mínimos y el establecimiento de listas de directorios permitidos, con el propósito de reducir el riesgo de exposición de credenciales y accesos no autorizados al sistema operativo.
3. **Capa de Supervisión Docente (*Human-in-the-Loop*):**
   Mecanismo de gobernanza mediante el cual el agente genera únicamente un borrador de prediagnóstico técnico. El docente verifica la existencia de las evidencias citadas, modula el tono comunicacional y aprueba la devolución definitiva.

Como instrumentos de transferencia y recolección se diseñaron:
- **Repositorio Plantilla Abierto:** Entorno de trabajo estructurado en GitHub conteniendo guías del taller, directorios de referencia, un evaluador automático en Python (`autograder_taller.py`) y un flujo de trabajo de integración continua en GitHub Actions configurado para una escala de 100 puntos.
- **Colección de Widgets Interactivos Desacoplados:** Banco de 35 actividades didácticas implementadas en HTML/CSS/JS autocontenidas en archivos locales, concebidas para ejecutarse directamente en el navegador sin dependencias de consola o servidores.

### 2.4. Procedimiento del taller
El taller se estructuró en dos jornadas consecutivas de cinco horas reloj cada una:
- **Jornada 1 (Fundamentos y Persistencia):** Presentación del protocolo MCP, configuración del agente en el entorno de desarrollo, creación de `AGENTS.md`, `MEMORY.md`, programa analítico y resolución del cuestionario interactivo de fundamentos (acumulando 60 puntos en el evaluador).
- **Jornada 2 (Skills Avanzadas y Laboratorio Integrador):** Construcción guiada del Trabajo Práctico 1 (`rubrica.md`, 20 puntos) y de la habilidad formal de evaluación (`skill_evaluador.md`, 20 puntos) utilizando plantillas predefinidas del toolkit docente, finalizando con la verificación de la suite de pruebas local (`python autograder_taller.py`) y la sincronización con el repositorio remoto.

### 2.5. Alcance de los datos y consideraciones éticas
Este trabajo no recopila ni analiza datos de participantes humanos como objeto de estudio. La experiencia de transferencia se describe únicamente como contexto de diseño de los recursos formativos, sin informar frecuencias de progresión, observaciones de conducta, verbalizaciones ni notas de campo. Las observaciones del pilotaje curricular se refieren al comportamiento de la arquitectura y a la estructura de los borradores generados bajo supervisión docente, en el marco de la actividad ordinaria de enseñanza, y no incluyen información de estudiantes.

---

## 3. RESULTADOS TÉCNICOS

### 3.1. Arquitectura técnica y ecosistema de recursos desarrollados (PI1)
En respuesta a la primera pregunta de investigación, la implementación permitió operacionalizar la separación entre las reglas pedagógicas almacenadas en archivos de especificación y la capacidad generativa del modelo. 

A través del protocolo MCP, el agente accedió a las soluciones de código ubicadas en carpetas locales, contrastándolas contra los criterios expresados en `rubrica.md` y generando borradores de devolución que citaban números de línea concretos. Durante el pilotaje se observó que los prediagnósticos generados bajo habilidades estructuradas tendían a conservar una organización común compuesta por: (a) identificación de fortalezas observadas, (b) señalamiento de inconsistencias algorítmicas con cita textual de código y (c) formulación de preguntas orientadoras para la corrección autónoma. Esta observación procede del pilotaje exploratorio y debe leerse como evidencia descriptiva: no se acompañó de un recuento sistemático de entregas, prediagnósticos generados ni revisiones docentes.

Asimismo, se desarrolló un banco de recursos didácticos de transferencia estructurado en 35 aplicaciones interactivas web autocontenidas para *Algoritmos y Programación*, complementado con módulos de prueba en estructuras dinámicas, simulaciones estocásticas y verificación de permisos en sistemas operativos.

### 3.2. Flujo de integración continua y evaluador automático (PI1)
El repositorio plantilla incorpora un evaluador automático en Python (`autograder_taller.py`) y un flujo de trabajo de integración continua en GitHub Actions configurado sobre una escala de 100 puntos. La puntuación se distribuye en tres componentes: 60 puntos acumulados durante la primera jornada (configuración de `AGENTS.md`, `MEMORY.md`, programa analítico y cuestionario de fundamentos), 20 puntos por la rúbrica del trabajo práctico (`rubrica.md`) y 20 puntos por la habilidad formal de evaluación (`skill_evaluador.md`). Esta correspondencia entre los pasos del procedimiento y el puntaje permite verificar cada avance de manera automática y reproducible.

### 3.3. Requisitos de seguridad y gobernanza de la configuración MCP (PI2)
En términos de seguridad informática, y conforme a las directrices de OWASP (2025), la configuración del servidor MCP de sistema de archivos se diseñó para requerir:
- restringir la ejecución a rutas locales aisladas y establecer listas de directorios permitidos;
- aplicar privilegios mínimos, limitando las herramientas del agente a listar directorios y leer archivos de código;
- adoptar mecanismos de protección de credenciales para reducir el riesgo de exposición y de accesos no autorizados al sistema operativo;
- exigir que cada observación del agente se asocie a evidencias verificables en el código, y que el docente verifique esas evidencias y apruebe la devolución definitiva.

### 3.4. Consideraciones de diseño para la transferencia (PI3)
El diseño de la experiencia de transferencia incorporó dos canales de acceso: un flujo técnico completo (Git, consola y GitHub Actions) y recursos web desacoplados (`index.html` y el banco de 35 aplicaciones interactivas) que no requieren consola. Esta duplicidad responde a una hipótesis de diseño sustentada en la literatura, y no en datos propios de adopción: la carga instrumental simultánea compite con el aprendizaje conceptual (Sweller, 1988; Kirschner et al., 2006) y Git presenta dificultades conceptuales para usuarios sin experiencia previa (Perez De Rosso & Jackson, 2013). La evaluación empírica de esta hipótesis requerirá un estudio específico con las garantías éticas correspondientes.

---

## 4. DISCUSIÓN

### 4.1. Especificaciones formales y consistencia en los prediagnósticos
Durante las pruebas de pilotaje curricular en *Programación II* y *Algoritmos y Programación*, se observó una mayor consistencia aparente en la estructura de los borradores de evaluación cuando el agente operó subordinado a archivos `AGENTS.md` y rúbricas analíticas formalizadas. 

La exigencia protocolizada de vincular cada dictamen a evidencias localizables en el código facilitó la detección docente de afirmaciones erróneas y estableció condiciones operativas orientadas a reducir el riesgo de aceptar evaluaciones no verificadas. Al limitar las herramientas del agente a la inspección pericial mediante MCP, se restringió operativamente la generación directa de soluciones completas y se orientó la respuesta hacia observaciones diagnósticas y preguntas de andamiaje. No obstante, esta consistencia observada requiere ser validada en investigaciones futuras mediante coeficientes estandarizados de concordancia interjueces y diseños cuasiexperimentales controlados. Esta cautela es consistente con las revisiones sobre rúbricas analíticas, que asocian criterios explícitos y descriptores de desempeño con una mayor consistencia de las puntuaciones sin que ello garantice por sí solo la validez de la evaluación (Jonsson & Svingby, 2007); en este trabajo, la formalización de criterios en `rubrica.md` constituye una condición plausible, pero no demostrada, de la consistencia aparente observada.

### 4.2. Supervisión humana (*Human-in-the-Loop*) y gobernanza ética
La experiencia respalda el uso de los agentes como asistentes de diagnóstico preliminar, manteniendo la decisión evaluativa final bajo responsabilidad docente. Durante el pilotaje, el equipo docente percibió que el prediagnóstico asistido disminuía el trabajo rutinario de localización y cotejo de patrones de código; sin embargo, esta percepción no fue cuantificada mediante un protocolo temporal controlado. Este rol de supervisión coincide con la evidencia de que la eficacia de la retroalimentación depende de su especificidad, su vínculo con la tarea y su orientación hacia la acción (Hattie & Timperley, 2007), atributos que la revisión docente permite verificar antes de comunicarla, y con las advertencias sobre inexactitudes y variabilidad de los modelos generativos en la educación en computación (Denny et al., 2024; Lau & Guo, 2023).

Delegar la retroalimentación final directamente en un modelo generativo, sin intervención humana, puede debilitar la responsabilidad pedagógica e incrementar la exposición del estudiante a respuestas inexactas o sesgadas. La supervisión activa no representa un obstáculo burocrático, sino una salvaguarda central de la arquitectura propuesta para que la tecnología opere de manera ética y formativamente significativa.

### 4.3. Implicaciones de diseño para la adopción
Para que arquitecturas basadas en MCP puedan ser adoptadas de forma amplia por docentes universitarios de diversas disciplinas, es razonable encapsular la complejidad de la consola mediante editores con interfaces gráficas amigables, extensiones integradas o plataformas de aprendizaje nativas que no requieran manipular directamente flujos de Git de bajo nivel. Esta recomendación se apoya en la teoría de la carga cognitiva (Sweller, 1988), en la evidencia sobre la menor eficacia de la guía mínima para quienes tienen poca experiencia previa (Kirschner et al., 2006) y en el análisis conceptual de las dificultades de Git (Perez De Rosso & Jackson, 2013), y se formula como hipótesis de diseño a evaluar, no como hallazgo empírico.

### 4.4. Limitaciones
1. **Ausencia de evaluación empírica con participantes:** No se presentan datos ni observaciones de participantes humanos como resultados, por lo que el trabajo no permite inferir adopción, aprendizaje ni satisfacción.
2. **Evidencia exploratoria del pilotaje curricular:** La observación sobre la estructura común de los prediagnósticos procede de un pilotaje descriptivo que no registró de manera sistemática la cantidad de entregas analizadas, de borradores generados, de docentes revisores, de afirmaciones erróneas detectadas ni la proporción de borradores aceptados o modificados; en consecuencia, no permite inferir calidad pedagógica, exactitud ni causalidad.
3. **Ausencia de medición de calidad y concordancia:** No se evaluó la exactitud de las devoluciones frente a evaluadores humanos ni la consistencia interjueces.
4. **Carácter preliminar de la percepción de ahorro de tiempo:** La percepción docente de menor trabajo rutinario no fue cuantificada mediante un protocolo temporal controlado.
5. **Doble rol del equipo:** Los autores fueron a la vez diseñadores de la arquitectura y docentes a cargo del pilotaje, lo que introduce un potencial sesgo.
6. **Contexto acotado:** El pilotaje se realizó en dos asignaturas de una misma institución, lo que restringe la generalización.

---

## 5. CONCLUSIONES Y TRABAJO FUTURO

El presente artículo expuso el diseño y la implementación de una arquitectura sociotécnica para la evaluación continua asistida por agentes de inteligencia artificial en programación universitaria, basada en el Protocolo de Contexto de Modelo (MCP), especificaciones en texto plano (`AGENTS.md`, `MEMORY.md`, rúbricas analíticas) y supervisión docente activa (*Human-in-the-Loop*).

Las principales conclusiones son:
1. **Viabilidad técnica:** La articulación entre MCP y especificaciones estructuradas permite inspeccionar entornos locales de código de manera auditable y reducir el acoplamiento con integraciones propietarias específicas, siempre que el servidor opere con rutas restringidas, privilegios mínimos y mecanismos adecuados de protección de credenciales.
2. **Relevancia del prediagnóstico asistido:** La subordinación del agente a un rol de asistente pericial supervisado preserva la autoridad pedagógica docente, favoreciendo una retroalimentación formativa contextualizada y sometida a revisión humana.
3. **Consideraciones de diseño para la adopción:** La literatura sugiere que la fricción asociada con Git y la consola puede competir con el aprendizaje conceptual, lo que justifica ofrecer interfaces visuales y recursos desacoplados; esta hipótesis requiere evaluación empírica.

Como líneas de trabajo futuro se plantean:
- Un estudio empírico de adopción por parte de docentes y estudiantes, con evaluación ética previa, consentimiento informado, libre y previo, y recolección de datos definida a priori.
- El desarrollo de estudios cuasiexperimentales con seguimiento temporal y grupos de control para medir el impacto de la retroalimentación asistida sobre el rendimiento académico.
- La evaluación de plataformas educativas e interfaces gráficas simplificadas que permitan operar con el protocolo MCP reduciendo la fricción de consola.
- La profundización en estudios de concordancia interjueces para cuantificar la consistencia evaluativa alcanzada mediante especificaciones matriciales formales.

---

## 6. DECLARACIONES OBLIGATORIAS

### Declaración de financiamiento y apoyo institucional
La información identificatoria sobre la fuente institucional de apoyo, financiamiento y acreditación del proyecto se ha omitido temporalmente para preservar la evaluación a doble ciego y fue comunicada al Comité Editorial mediante la plataforma OJS. Se incorporará formalmente en la versión aceptada.

### Declaración sobre uso de IA
Durante la preparación de este trabajo, los autores utilizaron el entorno Antigravity IDE (operando con los modelos Claude 3.7 Sonnet y Gemini) y el asistente Microsoft Copilot para asistir en la organización preliminar del contenido, la revisión estilística y gramatical del manuscrito en español, la traducción y revisión del resumen al inglés, y el cotejo normativo de directrices editoriales. Las herramientas de inteligencia artificial no fueron utilizadas para generar datos empíricos, resultados observacionales ni referencias bibliográficas. Los autores revisaron y editaron críticamente el contenido asistido, verificaron la integridad de las citas y asumen plena responsabilidad por el contenido final de la publicación.

### Consideraciones éticas
Este trabajo no presenta datos ni observaciones de participantes humanos como resultados de investigación. La experiencia formativa de transferencia se describe como contexto de diseño de los recursos, sin informar métricas de progresión, notas de campo ni verbalizaciones. Cualquier estudio empírico futuro sobre la adopción de la arquitectura por parte de docentes y estudiantes se realizará con evaluación ética previa y consentimiento informado, libre y previo.

---

## 7. REFERENCIAS BIBLIOGRÁFICAS

Anthropic. (2024). *Model Context Protocol: An open standard for connecting AI models to data sources*. Anthropic Engineering Blog. https://www.anthropic.com/news/model-context-protocol

Becker, B. A., Denny, P., Finnie-Ansley, J., Luxton-Reilly, A., Prather, J., & Santos, E. A. (2023). Programming is hard—or at least it used to be: Educational opportunities and challenges of AI code generation. En *Proceedings of the 54th ACM Technical Symposium on Computer Science Education V. 1* (SIGCSE 2023) (pp. 500-506). Association for Computing Machinery. https://doi.org/10.1145/3545945.3569759

Black, P., & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education: Principles, Policy & Practice, 5*(1), 7-74. https://doi.org/10.1080/0969595980050102

Denny, P., Prather, J., Becker, B. A., Finnie-Ansley, J., Blum, A., Luxton-Reilly, A., MacNeil, S., Petersen, A., Reeves, M., & Santos, E. A. (2024). Computing education in the era of generative AI. *Communications of the ACM, 67*(2), 56-67. https://doi.org/10.1145/3624720

Finnie-Ansley, J., Denny, P., Becker, B. A., Luxton-Reilly, A., & Prather, J. (2022). The robots are coming: Exploring the implications of OpenAI Codex on introductory programming. En *Proceedings of the 24th Australasian Computing Education Conference* (ACE '22) (pp. 10-19). Association for Computing Machinery. https://doi.org/10.1145/3511861.3511863

Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research, 77*(1), 81-112. https://doi.org/10.3102/003465430298487

Jonsson, A., & Svingby, G. (2007). The use of scoring rubrics: Reliability, validity and educational consequences. *Educational Research Review, 2*(2), 130-144. https://doi.org/10.1016/j.edurev.2007.05.002

Kirschner, P. A., Sweller, J., & Clark, R. E. (2006). Why minimal guidance during instruction does not work: An analysis of the failure of constructivist, discovery, problem-based, experiential, and inquiry-based teaching. *Educational Psychologist, 41*(2), 75-86. https://doi.org/10.1207/s15326985ep4102_1

Lau, S., & Guo, P. J. (2023). From "ban it till we understand it" to "resistance is futile": How university programming instructors plan to adapt as more students use AI code generation and explanation tools such as ChatGPT and GitHub Copilot. En *Proceedings of the 2023 ACM Conference on International Computing Education Research V. 1* (ICER '23) (pp. 106-121). Association for Computing Machinery. https://doi.org/10.1145/3568813.3600138

OWASP. (2025). *Model Context Protocol (MCP) Security Cheat Sheet*. Open Web Application Security Project. https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html

Perez De Rosso, S., & Jackson, D. (2013). What's wrong with Git? A conceptual design analysis. En *Proceedings of the 2013 ACM International Symposium on New Ideas, New Paradigms, and Reflections on Programming & Software* (Onward! 2013) (pp. 37-52). Association for Computing Machinery. https://doi.org/10.1145/2509578.2509584

Shute, V. J. (2008). Focus on formative feedback. *Review of Educational Research, 78*(1), 153-189. https://doi.org/10.3102/0034654307313795

Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science, 12*(2), 257-285. https://doi.org/10.1207/s15516709cog1202_4

Wang, F., & Hannafin, M. J. (2005). Design-based research and technology-enhanced learning environments. *Educational Technology Research and Development, 53*(4), 5-23. https://doi.org/10.1007/BF02504682
