# Unidad 1: Del chatbot al agente: herramientas, autonomía y MCP

## El Problema del Paradigma Actual
Actualmente, la adopción de la Inteligencia Artificial por parte de los **docentes** suele limitarse al uso de "Chatbots" genéricos (como la interfaz web de ChatGPT). El flujo clásico consiste en que el profesor copie el código de un alumno (o el programa de la materia), lo pegue en el chat web y pida: "Corrígelo" o "Genera un examen". 
**Desventaja (Carga Cognitiva Docente):** Según la **Teoría de la Carga Cognitiva (Sweller, 1988)**, obligar al docente a fragmentar su atención, copiando y pegando fragmentos de código de 100 alumnos hacia una pestaña externa, genera un costo cognitivo y operativo inasumible. Además, la IA web es "ciega": no tiene visibilidad estructural de cómo están organizados los archivos reales del proyecto que se está evaluando.

## La Solución: Tres Conceptos Fundamentales
Para comprender el salto evolutivo de esta investigación y evitar confusiones posteriores (por ejemplo, entre *prompts*, *skills* y *herramientas*), es vital separar tres conceptos tecnológicos distintos:

1. **Chatbot:** Es una interfaz que responde pasivamente a partir del texto y los archivos que el usuario le proporciona de forma manual en cada interacción.
2. **Agente:** Es un sistema dotado de autonomía, capaz de planificar o encadenar acciones y utilizar herramientas de forma iterativa para completar una tarea compleja de múltiples pasos.
3. **Model Context Protocol (MCP):** Es un **estándar de conexión** abierto. Define la arquitectura mediante la cual una aplicación cliente puede descubrir y utilizar recursos, contextos y herramientas ofrecidas por servidores (locales o remotos). No define cómo razona la IA, solo estandariza su conexión con el entorno. *(Analogía: MCP es al Agente lo que USB es a un periférico; no le provee inteligencia, sino un protocolo estándar para conectarse al mundo).*

A diferencia del paradigma inicial (Chatbot), la combinación de un agente con herramientas expuestas mediante MCP permite una integración controlada con determinados recursos del entorno local. El docente (o el sistema automatizado) puede inspeccionar carpetas enteras, leer repositorios masivos y ejecutar scripts de validación directamente. Esto automatiza la corrección sin que el docente deba hacer copy-paste manual, reduciendo tareas repetitivas y permitiendo que el docente concentre su tiempo en los casos que requieren juicio pedagógico.

## 💡 El Impacto en el Aula (Ejemplo: Programación II)
En la materia *Programación II* (UCSE), los alumnos desarrollan aplicaciones web complejas. 
Con el flujo clásico, evaluar si un alumno centró correctamente un `div` con CSS implicaba descargar el ZIP, abrirlo en el navegador e inspeccionar el código. 
Con el nuevo flujo, el proceso se descompone y orquesta de la siguiente manera:
1. **La integración continua (CI)** inicia el proceso al detectar una entrega del alumno en GitHub.
2. **El navegador headless (Herramienta)** renderiza la aplicación web en segundo plano.
3. **Los scripts de validación** recogen evidencias del DOM.
4. **El agente conectado mediante MCP** interpreta esas evidencias.
5. **El Skill** determina el procedimiento de evaluación aplicando la rúbrica y el formato de devolución.
6. **El docente** revisa excepciones o casos de alto impacto.

**Resultado:** El agente produce una retroalimentación trazable y no resolutiva directamente en el repositorio: *"En `index.css`, línea 15, el contenedor utiliza `display: flex`, pero no se encontró una propiedad de alineación transversal. Según el criterio 2 de la rúbrica, revisá el uso de `align-items`. No se modificó el archivo"*.

## La Evolución Tecnológica: De la Web al IDE Agentico
Para lograr esta inmersión y poder inyectar *Contexto* y *Skills* reales, debemos dar un salto tecnológico.
1. **Fase 1 (Aislada):** Usar la interfaz web genérica (`gemini.com` o `chatgpt.com`).
2. **Fase 2 (Semi-Aislada):** Crear un "Gem" o "GPT Personalizado" pegando instrucciones en la descripción. Es un avance, pero la IA sigue "ciega" respecto a los archivos reales de nuestra computadora.
3. **Fase 3 (Integración con MCP):** Complementar el chatbot web con **Entornos de Desarrollo Integrados (IDEs) Agénticos** o extensiones modernas capaces de acceder, bajo permisos controlados, a materiales, archivos y herramientas locales mediante el protocolo MCP. El chatbot web sigue siendo muy útil para explorar ideas, resumir textos o diseñar borradores rápidos; sin embargo, el entorno agéntico es indispensable cuando la tarea requiere trabajar sobre múltiples archivos o sistemas externos.
   - *Alternativas del mercado:* Existen excelentes opciones como **Cursor**, **Windsurf**, o extensiones para VSCode como **Cline** y **Roo Code**.
   - *El caso de esta investigación:* En esta experiencia se utilizó **Antigravity IDE** por su compatibilidad con MCP al momento de desarrollar los prototipos. No obstante, es fundamental comprender que **los conceptos metodológicos sobreviven a la herramienta**. Si en el futuro este IDE desaparece o es superado, la arquitectura basada en agentes, herramientas y protocolos abiertos (MCP) seguirá siendo completamente válida y transferible a cualquier otro entorno.

## Seguridad y Control Operativo (Human-in-the-loop)
Al dotar a un modelo de IA con permisos para leer carpetas, ejecutar scripts o interactuar con repositorios (vía MCP), es imperativo adoptar protocolos de seguridad rigurosos desde el primer día. No debemos ceder el control absoluto a la máquina. Todo despliegue debe contemplar:
1. **Principio de Mínimo Privilegio:** Conectar únicamente servidores MCP confiables y otorgar a la IA solo los permisos estrictamente necesarios (ej. acceso de solo lectura al código fuente del alumno).
2. **Aprobación Humana:** Requerir la confirmación explícita del docente antes de que la IA realice operaciones sensibles, como ejecutar comandos en la terminal, modificar archivos o publicar calificaciones.
3. **Aislamiento y Protección:** Mantener una estricta separación entre el entorno de prueba del código de los alumnos y el sistema operativo anfitrión, previniendo la ejecución de código malicioso o la exposición accidental de credenciales del docente.
4. **Trazabilidad y Registro:** Registrar qué archivos consultó el agente, qué herramientas ejecutó, qué evidencias utilizó y qué acciones propuso o realizó. Esto permite auditar las devoluciones, reconstruir lo ocurrido y resolver eventuales discrepancias con los estudiantes.
