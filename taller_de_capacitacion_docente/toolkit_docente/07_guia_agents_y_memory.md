# 7. Guía y Plantillas: `AGENTS.md` y `MEMORY.md`

Cuando trabajas con Agentes de IA en entornos de desarrollo modernos (como Cursor, Windsurf o Antigravity), depender exclusivamente de prompts manuales o de cargar Skills en cada chat puede volverse repetitivo para configurar el comportamiento global de un proyecto.

Para solucionar esto, utilizamos **archivos de configuración persistente**. Los dos más importantes son `AGENTS.md` y `MEMORY.md`.

---

## 1. ¿Qué son y para qué sirven?

### A. `AGENTS.md` (La Constitución del Proyecto)
*También conocido en algunos IDEs como `.cursorrules` o `GEMINI.md`.*
- **Propósito:** Definir las reglas globales de comportamiento, el tono, las herramientas permitidas y el contexto general del proyecto.
- **¿Cuándo actúa?** La IA lo lee de forma invisible y automática cada vez que inicias un nuevo chat dentro de esa carpeta.
- **Uso Docente:** Se usa para decirle al Agente: *"Estás en el repositorio de la materia Sistemas Operativos. Siempre responde como docente, nunca des código resuelto y avísame si el alumno usa librerías prohibidas"*.

### B. `MEMORY.md` (El Diario de a Bordo)
- **Propósito:** Mantener el estado actual del proyecto, el historial de decisiones, las convenciones adoptadas y las tareas pendientes (TODOs).
- **¿Cuándo actúa?** La IA lo lee para entender en qué punto se quedó el trabajo anterior, y tú (o la propia IA) lo actualizan al finalizar una sesión.
- **Uso Docente:** Sirve para que la IA recuerde: *"Ya corregimos los TP1 y TP2. Estamos armando el TP3. El estándar de base de datos que usamos este cuatrimestre es PostgreSQL, no MySQL"*.

---

## 2. Plantilla de Ejemplo: `AGENTS.md`

Guarda este contenido en un archivo llamado `AGENTS.md` en la raíz del repositorio de tu materia:

```markdown
# Contexto Global del Agente
Eres el Agente Asistente de la cátedra de [Nombre de la Materia] ([Año]).
Tu objetivo es asistir al equipo docente en la creación de material y auditoría de entregas.

## Reglas de Comportamiento (Safety Rails)
1. **Rol Estricto:** Siempre asume un rol académico y formativo. Usa un tono profesional y respetuoso (Método Socrático).
2. **Cero Código Resuelto:** NUNCA proporciones la solución directa a un problema de código de un estudiante. En su lugar, sugiere pistas, señala la línea del error o explica el concepto teórico subyacente.
3. **Tecnologías Permitidas:** En esta materia solo utilizamos [Ej: HTML, CSS puro y JavaScript Vanilla]. Si detectas dependencias externas (React, Tailwind, jQuery), detén el análisis e informa la infracción.
4. **Validación de Evidencia:** No asumas el funcionamiento de un código sin simularlo o revisarlo paso a paso.

## Flujo de Trabajo
- Antes de crear un Trabajo Práctico, revisa siempre la carpeta `/bibliografia` para alinear los ejercicios.
- Cuando evalúes un examen, exporta siempre el resultado a la carpeta `/reportes_borrador/`.
- Antes de proponer un cambio drástico en la arquitectura del material, consulta el archivo `MEMORY.md` para respetar las convenciones previas.
```

---

## 3. Plantilla de Ejemplo: `MEMORY.md`

Guarda este contenido en un archivo llamado `MEMORY.md` y actualízalo periódicamente:

```markdown
# Memoria del Proyecto y Estado de la Cátedra

## 📌 Contexto Actual
- **Fase del Cuatrimestre:** Preparación de exámenes de mitad de cursada (Unidades 1 a 4).
- **Última Acción:** Se finalizó el generador de TPs interactivos.

## 📐 Convenciones Acordadas (No modificar sin permiso docente)
- **Framework de Testing:** Usamos `pytest` para Python y `Jest` para JS.
- **Estructura de Repositorios:**
  - `TP<N>-demo/` -> Código docente (intocable).
  - `TP<N>/` -> Plantilla para alumnos.
- **Regla Psicométrica:** Todos los cuestionarios teóricos usan el estándar estricto anti-sesgo (Anti-Length, Anti-Letter).

## 📝 Tareas Pendientes (TODO)
- [x] Migrar TP1 y TP2 al nuevo formato autoevaluable.
- [x] Crear el `skill-evaluador-maquetacion.md`.
- [ ] (PRIORIDAD) Generar el repositorio base del Parcial 1 (Tema: E-commerce).
- [ ] Revisar si los tiempos de los tests en GitHub Actions superan los 30 segundos y optimizar.

## 🛑 Problemas Conocidos (Troubleshooting)
- Los alumnos de Windows tienen problemas con el salto de línea (`CRLF` vs `LF`). **Recordatorio a la IA:** Siempre agregar `.gitattributes` con `* text=auto eol=lf` al generar repositorios.
```

---
> **💡 Tip para el Taller:** Explica a los docentes que `AGENTS.md` es el "cómo nos comportamos siempre" y `MEMORY.md` es el "en qué andamos hoy y qué decidimos ayer". Al combinar ambos, logran que la IA se convierta en un miembro permanente del equipo de cátedra, con memoria a largo plazo.
