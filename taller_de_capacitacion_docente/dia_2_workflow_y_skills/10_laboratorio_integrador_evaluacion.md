# Laboratorio Integrador: Creación del TP1 y Skill Evaluador Docente

## 🎯 Objetivo del Laboratorio
Consolidar todo lo aprendido durante el Día 1 y el Día 2 configurando el primer módulo de evaluación de tu propia materia. Diseñarás la consigna/rúbrica del **Trabajo Práctico 1** y construirás la **Skill de Evaluación Asistida**, logrando el **100% de aprobación** en el sistema de corrección continua (GitHub Actions / Autograder) y dejando tu cátedra lista para evaluar entregas reales.

## 🛠️ Entorno de Trabajo
- **Materia:** Tu propia materia estructurada en el repositorio.
- **Contexto Base:** La `planificacion.md`, `AGENTS.md` y `MEMORY.md` creados en el Día 1.
- **Herramientas:** Tu IDE con IA (Antigravity / VS Code / Cursor) y tu repositorio clonado de [`plantilla-taller-docente-mcp`](https://github.com/Taller-de-Agentes-de-IA-en-docencia/plantilla-taller-docente-mcp).
- **Recursos de Apoyo:** Las plantillas de `/toolkit_docente` y los ejemplos reales de `/ejemplos_labs_interactivos`.

---

## 📊 Sistema de Puntuación (GitHub Actions & Autograder)

El autograder oficial (`autograder_taller.py`) valida automáticamente la completitud de tu repositorio:

| Fase | Requisito / Artefacto | Puntos | Estado |
| :--- | :--- | :---: | :---: |
| **Día 1** | Laboratorio Web Teórico (`index.html` → `respuestas_taller.json`) | 20 pts | ✅ Completado |
| **Día 1** | `AGENTS.md` (Reglas de comportamiento y tono docente) | 10 pts | ✅ Completado |
| **Día 1** | `MEMORY.md` (Memoria de contexto y convenciones de cátedra) | 10 pts | ✅ Completado |
| **Día 1** | `planificacion.md` (Programa analítico de la materia) | 10 pts | ✅ Completado |
| **Día 1** | Carpeta `/bibliografia` con al menos un archivo de referencia | 10 pts | ✅ Completado |
| **Día 2** | `Trabajo_Practico_1/rubrica.md` (Rúbrica analítica y criterios) | **20 pts** | ⏳ **Objetivo 1** |
| **Día 2** | `Trabajo_Practico_1/skill_evaluador.md` (Skill de evaluación con MCP) | **20 pts** | ⏳ **Objetivo 2** |
| **Total** | **Meta Final del Taller de Capacitación Docente** | **100 pts** | 🏆 |

---

## 🚀 Misión: Paso a Paso

### Paso 1: Generación de la Rúbrica del TP1 (`Trabajo_Practico_1/rubrica.md`)
El primer paso es definir qué y cómo se evalúa en el primer trabajo práctico de tu asignatura.

1. Abre tu IDE en la raíz de tu repositorio `plantilla-taller-docente-mcp`.
2. Solicita a tu agente que proponga la estructura y rúbrica del TP1 en base a la planificación de tu materia:
   > *"Actúa como mi asistente de cátedra. Tomando como base nuestra `planificacion.md` y las pautas docentes de `AGENTS.md`, crea la carpeta `Trabajo_Practico_1/`. Dentro de ella, redacta el archivo `rubrica.md` con: la consigna del TP1, 3 o 4 criterios analíticos claros y una escala de niveles de logro (Excelente, Aceptable, Requiere Ajuste). Muestra la propuesta y espera mi aprobación antes de escribir el archivo."*
3. **Validación Docente (HITL):** Revisa que los criterios sean pertinentes, medibles y ajustados al nivel de tus estudiantes. Pide los ajustes que consideres necesarios antes de confirmar.

---

### Paso 2: Creación de la Skill de Evaluación (`Trabajo_Practico_1/skill_evaluador.md`)
Ahora encapsularemos la rúbrica y las reglas pedagógicas en una **Skill reutilizable** que gobernará al agente cuando deba auditar las entregas de los estudiantes.

1. Puedes consultar la plantilla de referencia en tu carpeta local:
   - `toolkit_docente/plantillas_avanzadas/A_plantilla_evaluador_tecnico.md`
   - O la estructura estándar en `toolkit_docente/03_plantilla_skill.md`
2. Pídele al agente que genere el archivo de la skill:
   > *"Ahora genera el archivo `Trabajo_Practico_1/skill_evaluador.md` basándote en la plantilla `toolkit_docente/plantillas_avanzadas/A_plantilla_evaluador_tecnico.md`. La skill debe: incluir el frontmatter YAML, adoptar nuestra `rubrica.md`, incorporar restricciones éticas anti-alucinación, exigir el uso del protocolo MCP FileSystem para inspeccionar evidencias en archivos locales y devolver un feedback constructivo con preguntas socráticas sin dar nunca la solución directa."*
3. **Supervisión Docente:** Asegúrate de que la skill no sea un simple prompt genérico, sino una herramienta formal con delimitadores claros, procedimiento paso a paso y formato de salida estructurado.

---

### Paso 3: Verificación con Autograder y Publicación
Una vez creados ambos archivos, vamos a comprobar que el sistema automatizado valide tu cátedra con puntaje perfecto.

1. **Prueba Local:** Abre una terminal en la raíz de tu repositorio y ejecuta:
   ```bash
   python autograder_taller.py
   ```
   Deberás ver en pantalla los checks verdes correspondientes al Día 1 y Día 2, con un resultado final de **100 / 100 pts**.
2. **Publicación y CI en GitHub:**
   Envía los cambios a tu repositorio remoto:
   ```bash
   git add .
   git commit -m "Completar Día 2: rubrica y skill evaluador para TP1"
   git push
   ```
3. **Verificación en GitHub Actions:** Entra a tu repositorio en GitHub y abre la pestaña **Actions**. Comprueba que el workflow se ejecute en verde con el reporte de aprobación total.

---

## 🎉 Cierre y Futura Aplicación en Clases
¡Felicitaciones! Has completado el ciclo integral del taller:
- Has estructurado una cátedra transparente gobernada por archivos markdown (`AGENTS.md`, `MEMORY.md`, `planificacion.md`).
- Has creado una **Skill especializada** vinculada a criterios analíticos oficiales.
- Has comprobado cómo la evaluación continua y los pipelines de GitHub Actions automatizan el control de calidad formativo.

A partir de este momento, cuando en el ciclo lectivo real tus estudiantes entreguen sus soluciones, bastará con indicarle a tu Agente:
> *"Activa tu skill `Trabajo_Practico_1/skill_evaluador.md`, lee los archivos de entrega del alumno con MCP y prepárame un borrador de devolución basado en la rúbrica para mi revisión."*

La IA se encargará del análisis de evidencias y el borrador técnico; **tú mantendrás siempre la decisión y el juicio pedagógico final.**
