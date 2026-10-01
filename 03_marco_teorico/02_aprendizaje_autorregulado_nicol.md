# Aprendizaje Autorregulado y Principios de Feedback: Marco de Nicol & Macfarlane-Dick

## 1. El Aprendizaje Autorregulado (Self-Regulated Learning - SRL)
El aprendizaje autorregulado describe el grado en que los estudiantes participan activamente en su propio proceso de aprendizaje a nivel metacognitivo, motivacional y conductual (Zimmerman). En programación informática, la autorregulación es un predictor crítico del éxito: los estudiantes deben planificar la arquitectura de su código, monitorear la ejecución, depurar errores y evaluar si la solución satisface los requerimientos funcionales y no funcionales.

---

## 2. Los Siete Principios de la Buena Práctica de Retroalimentación (Nicol & Macfarlane-Dick, 2006)
David Nicol y Debra Macfarlane-Dick sintetizaron cómo la evaluación formativa fortalece directamente la autorregulación a través de siete principios:

1. **Clarifica qué es un buen desempeño:** Proporciona metas, criterios y estándares esperados (rúbricas y matrices transparentes).
2. **Facilita el desarrollo de la autoevaluación (reflexión) en el aprendizaje:** Brinda oportunidades para que el alumno compare su trabajo con estándares antes de someterlo a calificación formal.
3. **Ofrece información de alta calidad sobre el aprendizaje:** Devoluciones oportunas, específicas, correctivas y comprensibles.
4. **Fomenta el diálogo docente-estudiante y entre pares:** Transforma la retroalimentación en una conversación interactiva en lugar de una transmisión unidireccional.
5. **Estimula creencias motivacionales positivas y la autoestima:** Valora el progreso incremental y desestigmatiza el error como parte natural de la depuración de software.
6. **Ofrece oportunidades para cerrar la brecha entre el desempeño actual y el deseado:** Permite al alumno iterar, corregir y reenviar código.
7. **Proporciona información a los docentes que puede ser utilizada para modelar la enseñanza:** Genera analíticas pedagógicas sobre los errores más frecuentes para que la cátedra ajuste sus explicaciones teóricas.

---

## 3. Operacionalización en el Toolkit del Proyecto
- **Principio 1 & 2:** A través de las plantillas públicas de GitHub Classroom y las checklists de *issues* automatizadas (`setup-issues.yml`), el estudiante conoce exactamente qué se espera y puede autoverificar cada hito.
- **Principio 3 & 6:** La integración de GitHub Actions y agentes MCP permite devoluciones inmediatas (segundos/minutos) tras cada `git push`, permitiendo ciclos iterativos de corrección antes del cierre del plazo de entrega.
- **Principio 7:** La recolección de metadatos mediante el "Sistema de Puntos de Ritmo" y las métricas de fallos de pruebas permiten al equipo docente identificar patrones de dificultad en la cohorte.
