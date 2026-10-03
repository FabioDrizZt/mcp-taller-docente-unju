# Laboratorio Integrador: Evaluación Asistida y Supervisada

## 🎯 Objetivo del Laboratorio
Este es el "Jefe Final" del taller. Aplicarás todo lo aprendido en el Día 1 y el Día 2 para evaluar la entrega de un/a estudiante ficticio/a dentro de un entorno controlado, utilizando una Skill profesional y MCPs para asistir en la revisión técnica y preparar evidencias para la decisión docente.

## 🛠️ Entorno de Simulación
- **Materia:** Tu propia materia estructurada en el repositorio.
- **Tema:** Contenido práctico basado en la `planificacion.md` que creaste en el Día 1.
- **Estudiante (Caso Simulado):** `Estudiante_Ejemplo_01` (Entrega del Trabajo Práctico 1).
- **Herramientas a usar:** Tu IDE con IA (Antigravity / VS Code / Claude Dev / Cursor), MCP FileSystem activado, y tu repositorio de trabajo clonado a partir de [`plantilla-taller-docente-mcp`](https://github.com/Taller-de-Agentes-de-IA-en-docencia/plantilla-taller-docente-mcp).

---

## 📊 Sistema de Puntuación (GitHub Actions & Autograder)

El autograder oficial (`autograder_taller.py`) evalúa automáticamente la completitud de tu cátedra:

| Fase | Requisito / Artefacto | Puntos | Estado |
| :--- | :--- | :---: | :---: |
| **Día 1** | Laboratorio Web Teórico (`index.html` → `respuestas_taller.json`) | 20 pts | Completado |
| **Día 1** | `AGENTS.md` (Reglas de comportamiento y tono docente) | 10 pts | Completado |
| **Día 1** | `MEMORY.md` (Memoria de contexto y convenciones de cátedra) | 10 pts | Completado |
| **Día 1** | `planificacion.md` (Programa analítico de la materia) | 10 pts | Completado |
| **Día 1** | Carpeta `/bibliografia` con al menos un archivo de referencia | 10 pts | Completado |
| **Día 2** | `Trabajo_Practico_1/rubrica.md` (Criterios y niveles de desempeño) | **20 pts** | **Por realizar** |
| **Día 2** | `Trabajo_Practico_1/skill_evaluador.md` (Skill de evaluación docente) | **20 pts** | **Por realizar** |
| **Total** | **Meta del Taller de Capacitación Docente** | **100 pts** | 🏆 |

---

## 🚀 Misión: Paso a Paso

### Paso 1: Creación del Evaluador (Tareas del Día 2)
Ayer configuraste la estructura base (60 puntos). Hoy vamos a construir el evaluador asistido para sumar los **40 puntos restantes** y alcanzar el 100%.

1. Abre tu IDE en la raíz de tu repositorio `plantilla-taller-docente-mcp`.
2. Puedes consultar las plantillas base en tu carpeta local `/toolkit_docente`:
   - `toolkit_docente/03_plantilla_skill.md` (estructura básica).
   - `toolkit_docente/plantillas_avanzadas/A_plantilla_evaluador_tecnico.md` (evaluador especializado).
   - *(Opcional)* Revisa `/ejemplos_labs_interactivos` para inspirarte en rúbricas y ejercicios reales de otras cátedras.
3. Ingresa el siguiente prompt en el chat de tu Agente:
   > *"Basado en la materia que estructuramos en `planificacion.md` y las pautas de `AGENTS.md`, crea la carpeta `Trabajo_Practico_1/`. Dentro de ella, redacta una `rubrica.md` con 3 criterios analíticos claros y niveles de logro, y luego genera el archivo `skill_evaluador.md` basándote en la plantilla `toolkit_docente/plantillas_avanzadas/A_plantilla_evaluador_tecnico.md`. Muestra la propuesta y espera mi aprobación antes de guardar los archivos."*
4. **Verificación Docente (HITL):** Revisa que los criterios sean coherentes con tu disciplina y que la skill incluya las restricciones éticas (no dar respuestas directas, tono constructivo, método socrático).
5. **Comprobación del puntaje:**
   - En tu terminal puedes ejecutar: `python autograder_taller.py`
   - O realiza un `git push` a tu repositorio y verifica en la pestaña **Actions** de GitHub que alcanzaste los **100/100 pts**.

---

### Paso 2: Ejecución del MCP (Lectura de la Entrega)
Ahora que el agente cuenta con la Skill para evaluar, vamos a pedirle que inspeccione una entrega utilizando el protocolo MCP (FileSystem).

1. Pídele al agente que cree un caso de prueba para simular la entrega:
   > *"Simula la entrega de 'Estudiante_Ejemplo_01' creando una carpeta `Trabajo_Practico_1/entregas/Estudiante_Ejemplo_01/` con 2 o 3 archivos representativos de código o resolución acordes a nuestra consigna. Luego, utilizando tus herramientas de lectura de archivos (MCP), lista y verifica las evidencias presentes antes de emitir cualquier dictamen."*
2. **Observa:** El agente activará sus herramientas MCP para explorar el sistema de archivos local y listar las evidencias encontradas.

---

### Paso 3: Supervisión y Ajuste Pedagógico (Human-in-the-Loop)
El agente presentará un pre-diagnóstico técnico basado en la rúbrica.

1. **Auditoría de Evidencia:** Elige dos observaciones del agente y corrobora que efectivamente existan en el código entregado. Si una afirmación no está respaldada o es una alucinación, ordénale corregirla.
2. **Ajuste Pedagógico Contextual:**
   > *"El análisis técnico de las fallas es correcto, pero el/la estudiante está en sus primeras semanas y necesita guía metodológica. Reescribe la devolución: adopta un tono empático y constructivo, comienza destacando lo que resolvió correctamente y formula dos preguntas orientadoras (socráticas) para que descubra y corrija por sí mismo/a los errores detectados."*

---

### Paso 4: Exportación Segura de la Devolución
Para preservar la integridad de la entrega original, el feedback nunca debe sobrescribir los archivos del estudiante.

1. Pide al agente exportar la devolución en una carpeta separada de reportes:
   > *"Guarda este feedback final aprobado en `Trabajo_Practico_1/reportes/feedback_Estudiante_Ejemplo_01.md`. No modifiques ningún archivo dentro de la carpeta de entregas."*

---

## 🎉 Cierre del Taller
¡Felicitaciones! Has completado el flujo completo de:
1. **Configuración de Contexto Docente:** `AGENTS.md` + `MEMORY.md`.
2. **Estructuración Asistida:** Rúbrica y Skill personalizada con el Toolkit.
3. **Protocolo MCP:** Inspección segura de entregas en el entorno local.
4. **Supervisión Activa (HITL):** La IA propone análisis de evidencias, pero el criterio pedagógico, el tono formativo y la decisión final son siempre del docente.
