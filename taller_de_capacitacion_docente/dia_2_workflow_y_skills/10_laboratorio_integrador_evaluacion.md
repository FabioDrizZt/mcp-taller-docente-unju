# Laboratorio Integrador: Evaluación Asistida y Supervisada

## 🎯 Objetivo del Laboratorio
Este es el "Jefe Final" del taller. Aplicarás todo lo aprendido en el Día 1 y el Día 2 para evaluar la entrega de una estudiante ficticia dentro de un entorno controlado, utilizando una Skill profesional y MCPs para asistir en la revisión técnica y preparar evidencias para la decisión docente.

## 🛠️ Entorno de Simulación
- **Materia:** Tu propia materia estructurada en el repositorio.
- **Tema:** Contenido genérico basado en la `planificacion.md` que creaste.
- **Estudiante (Caso Simulado):** "Estudiante_Ejemplo_01" (Entrega del Trabajo Práctico 1).
- **Herramientas a usar:** Tu IDE con IA, MCP FileSystem activado, y los archivos de tu repositorio `plantilla-taller-docente-mcp`.

---

## 🚀 Misión: Paso a Paso

### Paso 1: Creación del Evaluador (Tareas del Día 2)
Ayer configuraste la estructura base en tu repositorio clonado (`plantilla-taller-docente-mcp`). Hoy vamos a crear el evaluador automatizado para obtener los 50 puntos restantes en GitHub Actions.

1. Abre el chat de tu Agente en el repositorio del taller.
2. Ingresa el siguiente comando para generar la estructura del TP1:
   > *"Basado en la materia que estamos estructurando, crea una carpeta `Trabajo_Practico_1/`. Dentro de ella, redacta una `rubrica.md` con 3 criterios de evaluación, y luego genera un archivo `skill_evaluador.md` basándote en la plantilla avanzada de evaluadores. Espera mi autorización antes de crear los archivos."*
3. **Observa:** El agente no debe simplemente dar un "OK" genérico. Como docente, verificarás que el agente haya interpretado correctamente la rúbrica y las restricciones antes de avanzar. Al finalizar, haz un `git push` y verifica que tu puntaje en GitHub Actions alcance el 100%.

### Paso 2: Ejecución del MCP (Lectura de la Entrega)
Ahora que el agente sabe *cómo* corregir, vamos a indicarle *qué* corregir utilizando las herramientas del sistema operativo, requiriendo un paso de comprobación previa.
1. Instruye al agente en lenguaje natural:
   > *"Asume tu rol y simula la entrega de 'Estudiante_Ejemplo_01' creando algunos archivos de código dentro de la carpeta `Trabajo_Practico_1/entregas/`. Antes de comenzar a evaluar en base a la rúbrica que diseñamos, enumera los archivos relevantes que encontraste y confirma que están presentes las evidencias mínimas. No propongas un puntaje si falta información indispensable."*
2. **Observa:** Verás en la interfaz cómo el agente activa sus herramientas, navega los directorios e informa su descubrimiento. Si todo está correcto, autorízalo a continuar.

### Paso 3: Verificación Docente (HITL Activo)
El agente generará un reporte preliminar con fortalezas y áreas de mejora.
1. **Comprobación de Evidencia:** Selecciona dos afirmaciones técnicas del reporte del agente (ej. "uso excesivo de selectores universales") y verifica manualmente en el código fuente que estén respaldadas. Si una observación no tiene evidencia clara, ordénale al agente que la elimine.
2. **Ajuste Pedagógico Contextual:** Pídele un ajuste basado en la etapa formativa del estudiante:
   > *"El análisis técnico es correcto, pero la estudiante se encuentra en una etapa inicial del curso y todavía está desarrollando estrategias para revisar CSS. Reescribe el feedback con un tono respetuoso y constructivo. Utiliza preguntas socráticas para orientar la revisión sin proporcionar directamente la solución, y comienza reconociendo evidencias concretas de lo que sí logró."*

### Paso 4: Finalización y Exportación Segura
Para conservar la evidencia original intacta, el reporte generado nunca debe sobrescribir ni mezclarse con la entrega del alumno.
1. Pide al agente que guarde el feedback final en un directorio independiente:
   > *"Usa tus herramientas para guardar este reporte final en un archivo llamado `feedback_NicolMar.md` dentro de la carpeta `/reportes_borrador/`."*

---

## 🎉 Cierre del Taller
Si has llegado hasta aquí, has completado exitosamente la orquestación. Has utilizado automatización supervisada para recopilar evidencias y preparar un borrador de devolución de forma escalable. El criterio académico, la contextualización pedagógica y la decisión final continúan, de principio a fin, bajo tu total responsabilidad docente.
