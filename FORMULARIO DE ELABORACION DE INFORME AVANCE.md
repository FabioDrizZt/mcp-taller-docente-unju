1. **IDENTIFICACIÓN DEL PROYECTO**

| Título del Proyecto  | "Agentes de IA y Protocolo MCP para evaluación continua y autoevaluación en materias de Ingeniería en Informática" |
| :---- | :---: |
| **Espacio Científico y Tecnológico**  | **Departamento Académico San Salvador, Prosecretaría de Investigación, UNIVERSIDAD CATÓLICA DE SANTIAGO DEL ESTERO** |

2. **CUERPO DEL PROYECTO**

El propósito de este informe es dar a conocer los resultados obtenidos durante esta primera etapa del proyecto (Noviembre 2025 - Junio 2026), el grado de cumplimiento conforme a lo previsto en el plan de trabajo y explicar las modificaciones o hallazgos técnicos en el desarrollo tecnológico implementado.

| Objetivos específicos | Porcentaje de cumplimiento | Dificultades, ajustes y/o modificaciones realizadas |
| ----- | :---: | ----- |
| Diseñar el ‘Toolkit de Evaluación Continua con IA’ (agentes, rúbricas, pruebas automatizadas y plantillas de feedback). | 60% | Se ha avanzado sólidamente en el diseño e implementación de los evaluadores principales. Se desarrollaron herramientas como el "Evaluador de Maquetación HTML+CSS" y el "Generador de Exámenes Prácticos de React", integrando el Model Context Protocol (MCP). El desarrollo ha tomado más tiempo del estimado dada la envergadura y complejidad que requiere la automatización de las actividades. |
| Integrar los agentes con LMS y repositorios de código institucionales (p. ej., Git) y bancos de preguntas. | 70% | Se logró la integración mediante GitHub Classroom, creando plantillas para Frontend y Backend con flujos de GitHub Actions. En esta etapa temprana, el enfoque principal se concentró en la materia "Programación II", dado que los estudiantes ya utilizan Git, lo cual facilitó la implementación inicial de la automatización de entregas y el CI/CD en un entorno controlado. |
| Pilotar el sistema en las asignaturas troncales, con protocolos de uso responsable y resguardo de datos. | 50% (en progreso) | El pilotaje se está llevando a cabo en "Programación II". Se elaboraron guías operativas detalladas (`instructions_frontend_estatico.md`, `instructions_backend.md`) para el uso responsable y la correcta configuración de las plantillas públicas de actividades. El uso cualitativo docente se mantiene en la evaluación de los Pull Requests. |
| Medir impacto con indicadores cuantitativos (tiempo de feedback, tasas de aprobación, calidad de soluciones) y cualitativos. | 20% | Fase en etapas iniciales. La medición del impacto cuantitativo se está canalizando a través del "Sistema de Puntos de Ritmo" de la asignatura, el cual evalúa la continuidad y gestión del tiempo en la realización de trabajos prácticos. El seguimiento de este ritmo y la recolección de metadatos se lleva a cabo mediante una planilla de cálculo (Excel), desde donde se extraerán las métricas de impacto definitivo (ej. aumento en la constancia de entregas) al finalizar el cuatrimestre. |
| Capacitar a docentes y generar guías y microcursos de buenas prácticas. | 50% | Se han formalizado las primeras guías arquitectónicas. Además, como resultado de esta primera mitad del proyecto, se ha propuesto para inicios del segundo cuatrimestre (agosto) el dictado de un taller de capacitación docente interno para compartir toda la experiencia y buenas prácticas adquiridas. |

**Dificultades, ajustes y/o modificaciones realizadas:**

El proyecto muestra un avance general del **50%** de acuerdo a lo pautado en el cronograma original. Inicialmente se subestimó el tiempo de configuración e integración requerido para lograr que las actividades estuvieran completamente automatizadas, dada la complejidad técnica de la materia Programación II. Por este motivo, el alcance actual se centró fuertemente en esta asignatura, aprovechando la familiaridad previa de los alumnos con Git.

En cuanto a la infraestructura técnica, se presentó un inconveniente imprevisto: inicialmente se plantearon repositorios privados en GitHub Classroom para impedir que los estudiantes copiaran el trabajo de sus compañeros. Sin embargo, GitHub Actions posee una cuota muy limitada de minutos gratuitos para repositorios privados. Como ajuste, se decidió que las actividades regulares operen como plantillas públicas y repositorios públicos para los alumnos, reservando el uso de repositorios privados estrictamente para instancias de exámenes formales.

| Descripción actividad | Realizada (mes) | A realizar (mes) |
| :---- | ----- | ----- |
| Planificación detallada y alta de servicios | Nov/25 ~ Dic/25 | ----------- |
| Co-diseño de rúbricas y tareas por cátedra | Dic/25 ~ Mar/26 | ----------- |
| Desarrollo e integración de agentes MCP | Feb/26 ~ May/26 | ----------- |
| Pilotaje en cursadas (Programación II - 1er semestre) | Mar/26 ~ Jun/26 | ----------- |
| Capacitación docente (Taller propuesto) | ----------- | Ago/26 |
| Recolección y análisis de datos | ----------- | Jul/26 ~ Oct/26 |
| Informe final y transferencia | ----------- | Sep/26 ~ Oct/26 |

3. **CRONOGRAMA DE ACTIVIDADES**
(Reflejado en la tabla superior).

4. **COMUNICACIÓN DE LOS RESULTADOS ALCANZADOS**

| Productos derivados de la investigación | | |
| ----- | ----- | ----- |
| **Publicaciones** | **Participación en eventos científicos** | **Acciones de transferencia** |
| No aplica en esta etapa temprana del proyecto. | No aplica en esta etapa temprana. Sin embargo, se ha propuesto para el mes de agosto (inicios del segundo cuatrimestre) el dictado de un taller de capacitación docente basado en la experiencia adquirida en el uso de MCP y automatizaciones en la cursada. | **1. Guías operativas:** Creación de `instructions_frontend_estatico.md` e `instructions_backend.md`.<br>**2. Toolkit de Evaluación:** Skills de evaluación de maquetación y generación de exámenes. Estas bases permiten la transferencia del sistema a otras cátedras. |

**PRINCIPALES PROBLEMAS**

| Problemas que acontecieron | Modo en que se resolvieron |
| :---- | :---- |
| **Límites de GitHub Actions en Repositorios Privados:** Inicialmente se pretendía usar repositorios privados para todas las actividades, pero el plan gratuito de GitHub Actions se agotaba rápidamente, bloqueando la ejecución del autograding. | Se modificó la estrategia de despliegue: las actividades formativas se transformaron en plantillas públicas, permitiendo a los alumnos aceptar *assignments* en repositorios públicos (donde Actions es gratuito e ilimitado). Los repositorios privados quedaron reservados exclusivamente para la evaluación de exámenes. |
| **Disparadores (Triggers) de la Creación de Issues Formativas:** Al aceptar la actividad de GitHub Classroom, la generación de *issues* automatizadas no se activaba correctamente de forma inmediata, requiriendo intervención. | Como solución de contingencia, se instruyó temporalmente a los alumnos a disparar manualmente las Actions (workflow_dispatch). Posteriormente, se investigó y solucionó el problema implementando una configuración en los YAML (`setup-issues.yml`) que permite disparar la creación de forma automática e idempotente sin que el alumno deba iniciarlas, lo cual es la solución definitiva que opera actualmente. |
| **Fricción en la adopción por parte de alumnos recursantes:** Algunos alumnos recursantes, acostumbrados a metodologías de cursadas anteriores, mostraron resistencia o confusión ante el flujo automático de GitHub Classrooms. En lugar de aceptar el assignment oficial, forkeaban, clonaban o descargaban el repositorio en formato ZIP y creaban un repositorio propio aparte, perdiendo así las Actions de autoevaluación. | Se generó un pequeño roce y curva inicial de adaptación. Esto se solucionó fortaleciendo la comunicación, explicando activamente el valor del feedback automático y acompañando de cerca las primeras entregas hasta que los recursantes comprendieron y adoptaron el ciclo de vida oficial (Aceptar Assignment -> Push -> Autograding) que provee la integración de Classroom. |

Fecha de presentación del informe: 29/07/2026

| Director del proyecto: | | Asesora Metodológica: |
| ----- | :---- | ----- |
|  |  |  |
