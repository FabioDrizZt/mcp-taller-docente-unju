# Laboratorio Integrador: Evaluación Asistida y Supervisada

## 🎯 Objetivo del Laboratorio
Este es el "Jefe Final" del taller. Aplicarás todo lo aprendido en el Día 1 y el Día 2 para evaluar la entrega de una estudiante ficticia dentro de un entorno controlado, utilizando una Skill profesional y MCPs para asistir en la revisión técnica y preparar evidencias para la decisión docente.

## 🛠️ Entorno de Simulación
- **Materia:** Programación Web.
- **Tema:** Maquetación Frontend Estática (HTML + CSS).
- **Alumna (Caso Simulado):** "NicolMar" (Examen Tienda de Ropa).
- **Herramientas a usar:** Tu IDE con IA (Cursor / Windsurf / Antigravity), MCP FileSystem activado, y la Skill pre-cargada `skill-evaluador-maquetacion.md`.

---

## 🚀 Misión: Paso a Paso

### Paso 1: Carga de la Inteligencia (Inyectar la Skill)
No le hables a la IA en Zero-Shot. Primero debes configurarlo temporalmente como evaluador de tu cátedra mediante la Skill.
1. Abre el chat de tu Agente.
2. Ingresa el siguiente comando para invocar la habilidad:
   > *"Lee la Skill ubicada en `@skill-evaluador-maquetacion.md`, identifica sus criterios, restricciones y condiciones de aborto. Resume brevemente cómo la aplicarás y espera mi autorización antes de evaluar."*
3. **Observa:** El agente no debe simplemente dar un "OK" genérico. Como docente, verificarás que el agente haya interpretado correctamente la rúbrica y las restricciones antes de avanzar.

### Paso 2: Ejecución del MCP (Lectura de la Entrega)
Ahora que el agente sabe *cómo* corregir, vamos a indicarle *qué* corregir utilizando las herramientas del sistema operativo, requiriendo un paso de comprobación previa.
1. Instruye al agente en lenguaje natural:
   > *"Asume tu rol y busca la entrega de la alumna NicolMar en la carpeta `examen-tienda-de-ropa-NicolMar`. Antes de comenzar a evaluar, enumera los archivos relevantes que encontraste, confirma que están presentes las evidencias mínimas (HTML y CSS) y comunica cualquier limitación. No propongas un puntaje si falta información indispensable."*
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
