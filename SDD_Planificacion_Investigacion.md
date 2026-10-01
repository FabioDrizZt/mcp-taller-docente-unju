# Documento de Planificación SDD (Spec-Driven Development) para la Investigación 2025-2026

**Proyecto:** Agentes de IA y Protocolo MCP para evaluación continua y autoevaluación en materias de Ingeniería en Informática.

Este documento formaliza la planificación metodológica y tecnológica del proyecto de investigación. Toma como base fundacional la experiencia y la infraestructura desplegada exitosamente en la asignatura [Programación II](file:///c:/Universidad/Programaci%C3%B3n%20II) durante su iteración más reciente.

---

## 1. Contexto y Punto de Partida: El Caso *Programación II*

El enfoque pedagógico y tecnológico validado consta de las siguientes fases y herramientas, que servirán como especificación base (Spec) para la investigación:

### 1.1. Contexto Documental y Normativo
Se ha consolidado todo el material teórico y las guías de planificación (ej. [Planificación 2026 - Programación II](file:///c:/Universidad/Agentes%20de%20IA%20y%20Protocolo%20MCP%20para%20evaluaci%C3%B3n%20continua%20y%20autoevaluaci%C3%B3n%20en%20materias%20de%20Ingenier%C3%ADa%20en%20Inform%C3%A1tica%20-%202025/10_bibliografia/fuentes_primarias/Planificaci%C3%B3n%202026%20-%20Programaci%C3%B3n%20II.md)), proponiendo el **sistema de puntos de ritmo** para gamificar y medir la constancia de los estudiantes. 
Todo el enfoque se sustenta empíricamente en un marco pedagógico riguroso que incluye el **Alineamiento Constructivo (Biggs, 1996)** para los evaluadores (Skills), el **Diseño Inverso (Wiggins & McTighe, 2005)** para la generación formal de consignas (SDD), y las **Teorías de Aprendizaje Experiencial (Kolb, 1984)** y **Codificación Dual (Paivio, 1971)** para la generación de laboratorios interactivos.

### 1.2. Andamiaje y Estandarización
Para estructurar correctamente el código de los alumnos en todos los módulos, se creó un repositorio base de configuración:
- **[Configuration-Files](file:///c:/Universidad/Programaci%C3%B3n%20II/Configuration-Files):** Estandariza ESLint, Prettier, dependencias y scripts de validación, garantizando que el feedback automático actúe sobre un código con un formato base predecible.

### 1.3. Modularización y Flujo de Trabajo
El aprendizaje se separó en 4 módulos, cada uno respaldado por instrucciones operativas y "Skills" evaluadores que alimentan a los Agentes de IA:

1. **Frontend Estático:**
   - Instrucciones docentes y workflows (issues automáticos, tests): [instructions_frontend_estatico.md](file:///c:/Universidad/Programaci%C3%B3n%20II/Frontend-Estatico/instructions_frontend_estatico.md)
   - Evaluador IA: [skill-evaluador-frontend-estatico.md](file:///c:/Universidad/Programaci%C3%B3n%20II/Frontend-Estatico/skill-evaluador-frontend-estatico.md)
2. **Backend:**
   - Instrucciones de despliegue y workflows: [instructions_backend.md](file:///c:/Universidad/Programaci%C3%B3n%20II/Backend/instructions_backend.md)
   - Evaluador IA: [skill_evaluador.md](file:///c:/Universidad/Programaci%C3%B3n%20II/Backend/skill_evaluador.md)
3. **Frontend JS:**
   - Evaluador IA: [skill_evaluador.md](file:///c:/Universidad/Programaci%C3%B3n%20II/Frontend-JS/skill_evaluador.md)
4. **React:**
   - Evaluador IA: [skill_evaluador.md](file:///c:/Universidad/Programaci%C3%B3n%20II/React/skill_evaluador.md)

### 1.4. Pivote Arquitectónico (Migración a ClassMoji)
La experiencia inicial en *Programación II* se orquestó íntegramente sobre **GitHub Classroom**. Sin embargo, ante el cierre definitivo de dicha plataforma el 28 de agosto de 2026, la investigación efectúa un pivote metodológico hacia la adopción de **[ClassMoji](file:///c:/Universidad/Agentes%20de%20IA%20y%20Protocolo%20MCP%20para%20evaluaci%C3%B3n%20continua%20y%20autoevaluaci%C3%B3n%20en%20materias%20de%20Ingenier%C3%ADa%20en%20Inform%C3%A1tica%20-%202025/10_bibliografia/fuentes_primarias/Classmoji%20A%20GitHub-Native%20LMS%20for%20Flexible%20CS%20Education.pdf)**. Este LMS nativo de GitHub permite sostener el mismo paradigma (repositorios por alumno, automatización con Actions, issues formativos) y suma soporte nativo para evaluación cualitativa (emojis) y fechas de entrega flexibles (tokens), alineándose aún mejor con el "Sistema de Puntos de Ritmo" propuesto.

---

## 2. Especificaciones de la Investigación (SDD)

Para trasladar este modelo de éxito a las nuevas asignaturas (*Algoritmos y Programación* e *Informática*), la investigación debe desarrollar e implementar las siguientes especificaciones:

### ⚙️ Spec 1: Abstracción del Andamiaje (Scaffolding)
- **Objetivo:** Generalizar `Configuration-Files` para soportar lenguajes fuera del ecosistema Node.js (ej. C++ y Python).
- **Entregables:**
  - Repositorios de plantillas base para C++ (con validadores como `clang-format` o `cpplint`) adaptables a la nueva plataforma ClassMoji (sustituyendo a GitHub Classroom).
  - Repositorios para Python (con `flake8` o `black`).

### 🤖 Spec 2: Estandarización de Skills de Evaluación Continua
- **Objetivo:** Convertir los archivos `skill_evaluador.md` específicos de Programación II en un **Protocolo MCP unificado**.
- **Entregables:**
  - Desarrollar un set de prompts parametrizables (Skills Universales) capaces de conectarse a entornos de prueba en cualquier lenguaje.
  - Implementar capacidades MCP para que la IA lea la consola, ejecute tests locales en el entorno del estudiante y provea feedback formativo.

### 🔄 Spec 3: CI/CD y Disparo Idempotente de Issues
- **Objetivo:** Mantener el concepto de *babysitting* automatizado documentado en `instructions_frontend_estatico.md`.
- **Entregables:**
  - Estandarización del script `setup-issues.yml` para evitar cuellos de botella con la creación duplicada de issues de guía.
  - Estrategia unificada de "Idempotencia por etiqueta o título" para todas las materias.

### 📊 Spec 4: Telemetría de los "Puntos de Ritmo"
- **Objetivo:** Validar la eficacia del sistema (reducción de deserción y aumento de calidad de código).
- **Entregables:**
  - Automatizar la recolección de métricas desde GitHub (frecuencia de commits, resolución de issues automáticos).
  - Cruce de datos con la planilla de Excel actual para el cierre estadístico (Hito de Octubre 2026).

---

## 3. Hoja de Ruta de Migración (Segundo Semestre 2026)

1. **Agosto:** Tomar las bases de CI/CD desarrolladas para GitHub Classroom en el primer semestre, y refactorizarlas/exponerlas en el Taller Docente Interno para capacitar en la nueva infraestructura basada en **ClassMoji** y plantillas con validación automática.
2. **Agosto-Septiembre:** Diseñar las `Configuration-Files` específicas para C++ adaptadas al nuevo flujo. Integrar los "Puntos de Ritmo" al segundo parcial de *Algoritmos y Programación*.
3. **Septiembre:** Ajustar los "Skills Evaluadores" para procesar C++ sin degradación de contexto.
4. **Octubre:** Análisis de datos comparativos y escritura del informe final de investigación.

---
*Este documento SDD regirá el desarrollo de las herramientas MCP y la adaptación metodológica. Cualquier actualización en la arquitectura debe reflejarse en los repositorios de plantillas y en `MEMORY.md`.*
