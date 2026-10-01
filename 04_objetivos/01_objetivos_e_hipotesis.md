# Objetivos, Preguntas de Investigación e Hipótesis

## 1. Objetivo General
Diseñar, implementar y evaluar un sistema de evaluación continua asistido por inteligencia artificial y fundamentado en agentes orquestados mediante el protocolo **Model Context Protocol (MCP)** en asignaturas de la carrera de Ingeniería en Informática y carreras afines de la UCSE-DASS, midiendo su impacto en la calidad del aprendizaje, la capacidad de autorregulación del estudiante y la eficiencia pedagógica de la retroalimentación docente.

---

## 2. Objetivos Específicos

- **OE1 (Diseño Tecnológico y Arquitectura):**  
  Diseñar y desarrollar la arquitectura del *Toolkit de Evaluación Continua con IA*, implementando servidores y agentes compatibles con el protocolo MCP para tareas de validación estática de código, ejecución de pruebas automáticas, evaluación de maquetación/lógica y generación de plantillas formativas de feedback.

- **OE2 (Integración Curricular y Plataformas):**  
  Integrar los agentes y flujos automatizados con el ecosistema de desarrollo de las asignaturas mediante GitHub Classroom, GitHub Actions y repositorios de código institucionales, formulando guías operativas para estudiantes y docentes.

- **OE3 (Evaluación de Impacto Cuantitativo y Cualitativo):**  
  Evaluar el impacto de la intervención en las cátedras seleccionadas mediante un enfoque metodológico mixto, cuantificando la regularidad de entregas (Sistema de Puntos de Ritmo), tiempos de respuesta y tasas de aprobación, e indagando las percepciones de docentes y alumnos.

- **OE4 (Transferencia y Buenas Prácticas Institucionales):**  
  Documentar los hallazgos técnicos y pedagógicos, sistematizar las lecciones aprendidas y ejecutar acciones de transferencia institucional, incluyendo talleres de capacitación docente, liberación de plantillas y propuesta de lineamientos éticos para el uso de IA en la universidad.

---

## 3. Preguntas de Investigación
1. **P1:** ¿En qué medida la retroalimentación inmediata proporcionada por agentes MCP disminuye el tiempo de detección y corrección de errores sintácticos y lógicos en las actividades prácticas de programación?
2. **P2:** ¿Cómo influye el andamiaje del sistema automatizado en el desarrollo de hábitos de autorregulación, medidos a través de la constancia y ritmo de entregas en GitHub Classroom?
3. **P3:** ¿Qué nivel de aceptación, confianza y utilidad pedagógica perciben los estudiantes regulares y recursantes respecto a las devoluciones generadas con asistencia de IA?
4. **P4:** ¿Qué restricciones técnicas (e.g. cuotas de cómputo en GitHub Actions, latencia de agentes) y culturales emergen durante la adopción institucional y cómo deben resolverse?

---

## 4. Hipótesis de Trabajo
- **H1 (Pedagógica/Autorregulación):** Los estudiantes que disponen de autograding y retroalimentación inmediata estructurada mediante agentes MCP presentan un incremento estadísticamente significativo en la constancia de trabajo (medida por los Puntos de Ritmo) y una menor acumulación de entregas sobre el límite del plazo respecto a cohortes históricas sin autoevaluación continua.
- **H2 (Eficiencia y Calidad Docente):** La automatización de la primera línea de revisión de código permite al equipo docente concentrarse en la evaluación cualitativa profunda de la arquitectura y la lógica en Pull Requests, reduciendo la dispersión y heterogeneidad de los criterios de corrección.
