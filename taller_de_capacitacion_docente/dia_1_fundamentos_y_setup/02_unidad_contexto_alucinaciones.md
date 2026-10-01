# Unidad 2: Contexto, fuentes y verificación

## ¿Por qué "Alucina" la IA?
Uno de los mayores temores docentes respecto a la IA es que "inventa cosas" o da respuestas que técnicamente funcionan en la industria, pero que van en contra de las convenciones enseñadas en la cátedra. 
Los modelos generativos producen respuestas plausibles a partir de patrones aprendidos. Cuando no disponen de información suficiente, criterios claros o fuentes verificables, pueden completar los vacíos con afirmaciones incorrectas. 

> [!WARNING]
> **Proporcionar contexto relevante reduce este riesgo, pero no lo elimina.**

Por eso, el contexto debe combinarse con citas, criterios de verificación y supervisión docente.

## La Inyección de Contexto como Solución Pedagógica
Para que la IA funcione como un asistente docente válido, debemos proporcionarle contexto relevante y verificable. En este taller utilizaremos informalmente la expresión "inyectar contexto", aunque ese contexto puede incorporarse mediante diferentes mecanismos, cada uno con un propósito específico:

1. **Contexto conversacional:** Instrucciones y aclaraciones escritas directamente en el mensaje interactivo del momento.
2. **Archivos adjuntos:** Proveer documentos estáticos como PDFs, apuntes teóricos, rúbricas de evaluación o el programa de la materia.
3. **Instrucciones persistentes:** Reglas estables y generales de la asignatura que el modelo debe obedecer en todas las interacciones (ej. "Prioriza la evaluación formativa sin dar el código resuelto").
4. **Recuperación documental:** Selección automática de fragmentos relevantes desde una base de conocimiento amplia (RAG).
5. **Herramientas o MCP:** Conexión estandarizada para consultar repositorios vivos, sistemas externos o leer el código actual del estudiante.
6. **Skills:** Procedimientos empaquetados y reutilizables para realizar una tarea pedagógica repetitiva (ej. "Evaluar Práctica de Ciclos"). *(Exploraremos esto a fondo en la siguiente unidad).*

Estas capas permiten orientar y restringir la evaluación según los estándares específicos de la cátedra, aunque sus resultados siempre deben permanecer sujetos a verificación.

## 💡 El Impacto en el Aula (Ejemplo: Teoría de los Sistemas Operativos - UNJu)
En materias muy teóricas y abstractas, una respuesta genérica de internet destruye el hilo pedagógico. 
En *Teoría de los Sistemas Operativos* (UNJu), en lugar de que la IA responda libremente sobre concurrencia, se le inyecta el material de estudio directo de la cátedra. 
**Resultado:** Cuando un alumno tiene problemas conceptuales con semáforos o monitores, si el sistema recupera efectivamente el fragmento correspondiente, podría responder: *"Tu análisis sobre la inanición necesita revisión. Consultá el apartado sobre condiciones de carrera de la Clase 5, página 12"*. La referencia debe mostrarse solamente cuando pueda trazarse de forma estricta hasta el documento fuente.

**Reglas centrales de salvaguarda:** 
1. El sistema (y los *Skills* que diseñemos) debe estar instruido rigurosamente para **nunca inventar una cita, una página o una referencia bibliográfica**. Si no encuentra evidencia suficiente en el contexto inyectado, debe declararlo de forma explícita. 
2. Si los documentos recuperados contienen información contradictoria (ej. una rúbrica nueva vs. una guía desactualizada), el agente debe señalar la contradicción y evitar decidir arbitrariamente cuál fuente es correcta.

De este modo, la IA asume el rol de un tutor que redirige al material oficial verificado, no de un oráculo que "alucina" justificaciones.
