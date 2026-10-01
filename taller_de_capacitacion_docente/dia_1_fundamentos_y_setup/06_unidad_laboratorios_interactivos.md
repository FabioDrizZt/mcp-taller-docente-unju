# Unidad 5: Más allá del Código (Aprendizaje Experiencial)

## Más allá de la corrección de código
Una visión limitada del uso educativo de la IA consiste en reducirla a la generación o corrección de código. En las asignaturas de Informática, la IA también puede ayudar a diseñar simulaciones, visualizaciones, laboratorios guiados y entornos de experimentación. Esto permite extender los beneficios de la retroalimentación inmediata a asignaturas más conceptuales y teóricas (como Sistemas Operativos o Redes).

## Generación de Simuladores y Codificación Dual
A partir de especificaciones revisadas por el docente, los agentes pueden asistir en la ideación y construcción de experiencias prácticas estructuradas en tres niveles de abstracción:
- **Nivel 1 (Modelo conceptual):** Mini-simuladores visuales (HTML/JS) que representan procesos y recursos de forma simplificada. Todo modelo conceptual debe comunicar explícitamente al alumno qué aspectos del sistema real representa, cuáles simplifica, cuáles omite y qué conclusiones no permite derivar.
- **Nivel 2 (Demostración ejecutable):** Scripts (ej. Python) que reproducen el comportamiento concurrente en condiciones controladas.
- **Nivel 3 (Práctica en entorno real aislado):** Uso de herramientas del sistema operativo (vía WSL) para observar y manipular recursos. **Seguridad operacional:** Este nivel exige ejecutar las acciones en un entorno aislado (sandbox), utilizando un usuario sin privilegios administrativos, restringido a un directorio de prácticas y limitando los comandos permitidos.

La generación asistida del laboratorio y su utilización con estudiantes constituyen etapas radicalmente diferentes. Antes de incorporarlo a una actividad, el docente debe validar de forma explícita:
- La exactitud conceptual del modelo y los límites de su simplificación.
- El comportamiento técnico ante entradas no previstas.
- La accesibilidad, claridad visual y seguridad operacional.
- La alineación con los resultados de aprendizaje esperados.

**Fundamento Pedagógico:**
1. **Teoría de la Codificación Dual (Paivio, 1971):** Distingue sistemas relacionados para procesar información verbal y no verbal. La combinación coherente de explicaciones y representaciones visuales puede ofrecer rutas complementarias para comprender y recordar un concepto. Sin embargo, los elementos multimedia deben ser relevantes, estar coordinados y evitar sobrecargar al estudiante (considerando su carga cognitiva).
2. **Aprendizaje Experiencial (Kolb, 1984):** El laboratorio interactivo (en cualquiera de sus niveles) puede proporcionar una experiencia inicial o un espacio de experimentación. Para transformarlo en una experiencia de aprendizaje genuina, la actividad debe completar el ciclo de Kolb: incluir momentos de observación reflexiva, contraste con la teoría (conceptualización abstracta) y nueva experimentación activa, no solo manipulación lúdica de controles.

## 💡 El Impacto en el Aula (Ejemplo: Sistemas Operativos)
Comprender la concurrencia y el interbloqueo (deadlock) es altamente abstracto. A partir del diseño validado de un simulador generado con asistencia de IA, el docente puede estructurar un verdadero ciclo de Kolb:
1. **Experiencia concreta:** El estudiante ejecuta una simulación en la que dos procesos adquieren recursos en distinto orden hasta bloquearse.
2. **Observación reflexiva:** Registra qué proceso tomó cada recurso, cuándo dejó de existir progreso y qué esperaba que sucediera.
3. **Conceptualización abstracta:** Relaciona lo observado con las cuatro condiciones necesarias para la aparición del interbloqueo: exclusión mutua, retención y espera, no expropiación y espera circular.
4. **Experimentación activa:** Modifica el orden de adquisición o la política de prevención, formula una predicción y vuelve a ejecutar el escenario.

**Resultado:** El alumno transita desde la interacción con un modelo conceptual simplificado hasta la experimentación en un entorno real aislado. En cada nivel, la experiencia se acompaña con observación, conceptualización y nueva experimentación, transformando la manipulación del entorno en conocimiento estructurado. Mediante herramientas expuestas a través de MCP, el Agente puede conectarse a un entorno Linux aislado (como una terminal WSL configurada para la práctica), ejecutar las pruebas autorizadas y recopilar evidencias para validar el trabajo del estudiante, operando siempre bajo estrictos límites de seguridad.
