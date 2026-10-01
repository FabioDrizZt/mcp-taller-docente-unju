# Unidad 3: Ecosistemas de Skills e Ingeniería de Prompts (Alineamiento Constructivo)

## La Ingeniería de Prompts para Docentes
Dar instrucciones a la Inteligencia Artificial requiere precisión. La "Ingeniería de Prompts" es el diseño meticuloso de directrices para asegurar que la IA actúe con un "tono" pedagógico, que no resuelva los ejercicios por completo, y que evalúe paso a paso.
Sin embargo, escribir estas instrucciones largas en cada clase es agotador y propenso al error humano, lo que puede resultar en evaluaciones desiguales.

## El Concepto de "Skills" y el Alineamiento Constructivo
Una **Skill** (Habilidad) es una capacidad reutilizable que encapsula instrucciones, criterios, procedimientos y, según el entorno, recursos o herramientas para realizar una tarea pedagógica específica. 
En determinados entornos, una Skill puede almacenarse como un archivo **versionable** que conserva instrucciones y procedimientos reutilizables, evitando que el docente tenga que reconstruirlos desde cero en cada conversación. Tratar a las directrices pedagógicas como artefactos versionables (al igual que el código fuente) permite a la cátedra iterarlas, mejorarlas colaborativamente y compartirlas entre todo el equipo docente.

**Taxonomía Fundamental:**
Para evitar confusiones a la hora de orquestar estas tecnologías, debemos distinguir:
- **Prompt:** Instrucción concreta para una interacción aislada.
- **Instrucción persistente:** Regla general aplicada sistemáticamente entre interacciones.
- **Skill:** Procedimiento reutilizable orientado a resolver una tarea completa.
- **Herramienta (Tool):** Capacidad externa que permite consultar datos o ejecutar acciones (ej. compilar código).
- **MCP:** Protocolo abierto que permite conectar una aplicación de IA o un agente con recursos y herramientas externas.

**Fundamento Pedagógico:** Esto materializa el **Alineamiento Constructivo (Biggs, 1996)**. Este marco propone una correspondencia explícita entre los resultados de aprendizaje previstos, las actividades que realizan los estudiantes y las tareas mediante las cuales se evalúan esos resultados. Una *Skill* puede ayudar a documentar y reutilizar esa correspondencia, siempre que sus criterios sean revisados, probados y actualizados por el docente. Esto favorece una evaluación más consistente, al reducir la variabilidad de las instrucciones y facilitar la detección de desvíos en las respuestas del agente.

## Estructura Mínima de una Skill Docente
Para que una *Skill* sea verdaderamente útil y reutilizable, no basta con una instrucción genérica; requiere un diseño estructurado. A continuación, se presenta la plantilla recomendada para este taller:

- **Propósito:** Qué tarea docente específica resuelve.
- **Entradas esperadas:** Información concreta que debe recibir para operar (ej. entrega del alumno, rúbrica, unidad temática, bibliografía).
- **Condiciones de uso:** Cuándo debe utilizarse y cuándo no.
- **Contexto requerido:** Programa analítico, bibliografía, rúbrica, nivel y contenidos enseñados.
- **Procedimiento:** Pasos secuenciales que debe seguir la IA.
- **Restricciones:** Qué *no* debe hacer (ej. "Nunca proporcionar el código resuelto").
- **Formato de salida:** Cómo debe presentar el resultado (ej. markdown, tabla, CSV).
- **Criterios de validación:** Cómo comprobar que el resultado es correcto.
- **Manejo de incertidumbre:** Qué debe hacer si falta información o existen contradicciones.

## 💡 El Impacto en el Aula (Ejemplo: Sistemas Operativos II - UNJu)
Administrar el aprendizaje práctico de cohortes masivas (más de 100 alumnos) es logísticamente complejo. 
Para la cátedra de *Sistemas Operativos II* en la UNJu, se desarrolló una *Skill* de creación de cuestionarios. 
**Resultado:** La *Skill* genera bancos de preguntas y actividades en un formato estructurado que el docente puede revisar y luego trasladar o importar directamente a plataformas como *Quizizz*. Esto permite que los más de 100 estudiantes realicen un repaso (autoevaluación) rigurosamente alineado con la teoría antes de entrar a la clase práctica, sin requerir automatizaciones ciegas ni riesgos de publicación desatendida.
