# Fichas Analíticas de Lectura (Knowledge Base Bibliográfica)

Estas fichas sintetizan los conceptos nucleares, citas textuales y aportes directos de la bibliografía de referencia para alimentar el contexto de la IA al momento de redactar o fundamentar los capítulos:

---

## Ficha 1: Black & Wiliam (1998) - *Inside the Black Box*
- **Cita Clave:** *"La retroalimentación para cualquier alumno debe ser de tal naturaleza que cada estudiante pueda ver cómo mejorar de manera constructiva. El feedback que se centra en lo que necesita hacerse puede fomentar que todos crean que la mejora está a su alcance"* (p. 143).
- **Aporte al Proyecto:** Fundamenta por qué los agentes no deben limitarse a decir "aprobado/desaprobado", sino suministrar pistas orientadas a la acción correctiva inmediata (*feedforward*).

---

## Ficha 2: Nicol & Macfarlane-Dick (2006) - *Seven Principles of Good Feedback*
- **Cita Clave:** *"En la educación superior, los estudiantes ya son aprendices autorregulados hasta cierto punto. El objetivo pedagógico es empoderarlos para que asuman un rol más activo y reflexivo en el monitoreo de sus propias producciones"* (p. 200).
- **Aporte al Proyecto:** Provee el marco de los 7 principios que se traducen en las métricas del "Sistema de Puntos de Ritmo" y las checklists automáticas de GitHub Classroom.

---

## Ficha 3: Anthropic (2024) - *Model Context Protocol Specification*
- **Concepto Clave:** MCP estandariza la interacción bidireccional entre modelos y herramientas externas mediante un protocolo abierto JSON-RPC, eliminando integraciones propietarias frágiles y garantizando el aislamiento de seguridad y trazabilidad de llamadas a funciones.
- **Aporte al Proyecto:** Sustento técnico-arquitectónico del Toolkit (servidores MCP de evaluadores HTML/CSS, generadores React y validadores C++).

---

## Ficha 4: UNESCO (2023) - *Guidance for Generative AI in Education and Research*
- **Concepto Clave:** Principio de agencia humana y transparencia. La IA debe ser utilizada para empoderar al estudiante y al docente, requiriendo que toda salida automatizada sea claramente identificada, auditable y respetuosa de la privacidad de datos.
- **Aporte al Proyecto:** Protocolo de rotulado de feedback de IA y consentimiento informado.

---

## Ficha 5: Zimmerman (2002) - *Becoming a Self-Regulated Learner*
- **Concepto Clave:** La autorregulación no es un rasgo fijo sino un proceso cíclico tridimensional: (1) Fase de Previsión (*Forethought* - metas y planificación estratégica); (2) Fase de Desempeño/Control (*Performance* - autocontrol y automonitoreo); y (3) Fase de Autorreflexión (*Self-reflection* - autoevaluación y atribuciones).
- **Aporte al Proyecto:** Marco teórico exacto que justifica el "Sistema de Puntos de Ritmo": medir si el alumno inicia temprano (previsión) y si itera ante fallos de tests (automonitoreo).

---

## Ficha 6: Elliott (1991) - *Action Research for Educational Change*
- **Concepto Clave:** La investigación-acción educativa es el estudio de una situación social con miras a mejorar la calidad de la acción dentro de ella. Se estructura en espirales dialécticas de reconocimiento, planificación, implementación de pasos de acción, observación de efectos y reflexión crítica.
- **Aporte al Proyecto:** Justificación metodológica para los pivotes pedagógicos del proyecto (e.g. migración a repositorios públicos por cuotas de Actions; adaptación presencial con recursantes).

---

## Ficha 7: Creswell & Creswell (2018) / Hernández-Sampieri (2014) - *Métodos Mixtos*
- **Concepto Clave:** Los diseños mixtos integran sistemáticamente datos cuantitativos (estadísticos, telemetría) y cualitativos (percepciones, observaciones de campo) en un solo estudio para lograr una comprensión más profunda y holística del fenómeno que la que proporcionaría cada enfoque por separado.
- **Aporte al Proyecto:** Diseño de convergencia: cruzar los Puntos de Ritmo (cuantitativo) con las encuestas de percepción y la revisión de Pull Requests (cualitativo).

---

## Ficha 8: Planificaciones Curriculares UCSE 2026 (*Algoritmos y Programación* y *Programación II*)
- **Conceptos Clave:**
  - *Algoritmos y Programación (1º año):* Competencia en algoritmia, estructuras de control, arreglos, modularización y paso de parámetros en C++, con régimen de evaluación continua y simulacros.
  - *Programación II (3º año):* Desarrollo web profesional, arquitectura por capas, control de versiones con Git/GitHub, frontend (HTML5/CSS3/React) y backend (APIs REST con Node.js), evaluado mediante entregas continuas y proyectos integradores.
- **Aporte al Proyecto:** Conexión curricular y empírica directa entre los requerimientos pedagógicos oficiales de la UCSE y las herramientas automatizadas del Toolkit MCP.

---

## Ficha 9: Traore & Tregubov (2026) - *Classmoji: A GitHub-Native LMS for Flexible CS Education*
- **Cita Clave:** *"Classmoji addresses this mismatch by treating GitHub organizations as classrooms, repositories as course modules, and issues as assignments. This direct mapping enables seamless course management within a platform already familiar to students and widely used in industry, introducing three features: (1) automated creation and management of repositories and issues; (2) an emoji-based feedback system that replaces numerical scores; and (3) a token-based time management mechanism"* (p. 1).
- **Conceptos Clave:**
  - *Infraestructura Nativa de Git:* Mapeo directo y automatizado entre organizaciones, repositorios e issues (el cierre del issue marca la entrega del alumno).
  - *Evaluación Alternativa con Emojis:* Desplaza el foco del cálculo numérico punitivo hacia el feedback cualitativo y el logro de competencias de aprendizaje (*alternative grading*).
  - *Economía de Tokens para Gestión del Tiempo:* Sustituye políticas inflexibles de penalización por tardanza por un sistema flexible de tokens administrados por el alumno, fomentando la autorregulación.
- **Aporte al Proyecto:** Fundamenta técnica y pedagógicamente el pivote de la investigación tras el cierre definitivo de GitHub Classroom (28 de agosto de 2026), sirviendo de plataforma de orquestación para el segundo semestre y complementando de manera sinérgica el "Sistema de Puntos de Ritmo".
