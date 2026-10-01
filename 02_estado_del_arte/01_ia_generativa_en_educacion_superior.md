# Inteligencia Artificial Generativa y Autograding en Educación Superior

## 1. Evolución del Autograding en Ciencias de la Computación
Desde las primeras experiencias en sistemas como *CourseMarker*, *Web-CAT* o *Gradescope*, la corrección automatizada en educación informática se concentró en la ejecución de suites de pruebas funcionales y análisis estático con reglas cerradas.

Si bien estos sistemas garantizan consistencia y escalabilidad, la literatura internacional documenta importantes limitaciones formativas:
- **Ausencia de diálogo cualitativo:** Se limitan a informar qué casos de prueba fallaron (e.g. `AssertionError: expected 5 but got 4`), sin explicar el *por qué* ni guiar al alumno sobre la raíz del fallo.
- **Riesgo de "Trial and Error" no reflexivo:** Los estudiantes tienden a enviar modificaciones menores repetitivas intentando "pasar los tests" en lugar de razonar conceptualmente su diseño algorítmico.

---

## 2. El Impacto de los Modelos de Lenguaje de Gran Escala (LLMs)
Con la popularización de herramientas como GitHub Copilot, ChatGPT y modelos de razonamiento (Claude, Gemini), el campo de la educación en programación experimentó una disrupción sin precedentes:

- **Productividad del Desarrollador:** Estudios como Peng et al. (2023) evidencian incrementos significativos de velocidad y resolución en tareas de programación mediante asistencia por IA.
- **Desafíos Pedagógicos e Integridad Académica:** La capacidad de los LLMs para resolver ejercicios clásicos de programación generó dilemas sobre la validez de los métodos de evaluación tradicionales basados exclusivamente en la entrega de código cerrado.
- **Recomendaciones de Organismos Internacionales (UNESCO & OCDE):**
  - **UNESCO (2023):** *Guidance for Generative AI in Education and Research* enfatiza la necesidad de un enfoque centrado en el ser humano, donde la IA potencie las capacidades cognitivas del estudiante en lugar de reemplazarlas, demandando marcos éticos explícitos y resguardo estricto de la privacidad.
  - **OCDE (2021):** *Digital Education Outlook* subraya el valor de la personalización del aprendizaje asistido por IA, siempre que existan mecanismos de gobernanza algorítmica y capacitación docente robusta.

---

## 3. De Asistentes Conversacionales a Sistemas Inteligentes de Tutoría y Evaluación
La investigación contemporánea (2024–2026) converge hacia la necesidad de construir **sistemas de andamiaje evaluativo** que no suministren la solución directa ("código servido"), sino que actúen conforme a principios socráticos:
- Indicar conceptos teóricos involucrados.
- Guiar en la identificación de casos de borde no contemplados.
- Calificar la calidad técnica según rúbricas analíticas transparentes.
