# Unidad 9: Orquestación (Uniendo Skills con MCPs)

## 1. El Cerebro y Las Manos
En la Unidad 8 construimos el "cerebro" (la Skill). Sin embargo, la Skill define cómo actuar, pero no garantiza por sí misma el acceso a archivos, repositorios o entornos de ejecución. Para obtener evidencias externas necesita las herramientas y permisos apropiados.

Aquí es donde entran las herramientas del Agente y el **Protocolo de Contexto de Modelos (MCP)** que conocimos en el Día 1. En el entorno configurado para este taller, el acceso controlado al sistema de archivos y a la terminal se proporciona mediante servidores MCP (o herramientas nativas, según la plataforma). Estos actúan como las "manos" y los "ojos" de tu Skill.

## 2. Tipos de Orquestación Docente

### A. Orquestación Estática (FileSystem + Skill)
**Caso de uso:** Corregir un examen teórico o un diagrama.
- **El Docente pide:** *"Ejecuta la skill `Evaluador_Maquetacion` sobre la carpeta del alumno Pérez."*
- **El Agente actúa:** Usa el MCP de `FileSystem` para abrir la carpeta de Pérez, lee el `index.html`, aplica las reglas cognitivas de la Skill, y genera el Markdown de feedback.

### B. Orquestación Dinámica (Bash + FileSystem + Skill)
**Caso de uso:** Evaluar código ejecutable (Python, C++, Java).
- **El Docente pide:** *"Ejecuta la skill `Corrector_Algoritmos` sobre la entrega de Gómez en un entorno aislado con un timeout de 30 segundos."*
- **El Agente actúa:** 
  1. Usa `FileSystem` para encontrar el código.
  2. Usa `Bash` para compilar el código (`g++ main.cpp -o app`), respetando las restricciones de seguridad (ejecución sin privilegios de red y en carpeta temporal).
  3. Usa `Bash` para ejecutar los tests unitarios dentro del tiempo límite.
  4. Lee la salida por consola, aplica los criterios de la Skill, reúne evidencias y **propone** un puntaje justificado para revisión docente.

### C. Orquestación Histórica (GitHub + Skill)
**Caso de uso:** Calcular los *Puntos de Ritmo* (Unidad 6).
- **El Docente pide:** *"Aplica la skill `Auditor_de_Ritmo` al repositorio del alumno López."*
- **El Agente actúa:** Usa el MCP de `GitHub` para leer el historial de commits. El agente detecta un patrón de baja distribución temporal en el historial disponible: la mayor parte de los cambios aparece concentrada en un único commit cercano al vencimiento. La Skill registra el indicador como evidencia parcial, advierte que no permite inferir por sí solo cómo trabajó el estudiante (problemas de zona horaria, falta de red local), y solicita revisión docente antes de sugerir los puntos de ritmo.

## 3. El Paradigma "Human-in-the-Loop" (HITL)
Por muy poderosa que sea la orquestación, recordamos nuestro pilar ético: **La IA propone, el docente dispone**.
El flujo ideal de orquestación nunca termina enviando la nota automáticamente al sistema de la Universidad. Termina generando un reporte (ej. un borrador de Issue en GitHub o un PDF) que el docente revisa, aprueba o modifica antes de hacerlo oficial.

> **Preparación para el Laboratorio:** En la siguiente sección, pondremos esto a prueba. Dejarán la teoría atrás y se convertirán en orquestadores en tiempo real, evaluando a un alumno ficticio.
