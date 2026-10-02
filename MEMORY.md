# Memoria del Proyecto y Estado de Situación (MEMORY.md)

> Este archivo actúa como la memoria persistente del proyecto entre sesiones de trabajo con la IA. Registra el estado actual, las decisiones tomadas, los hitos cumplidos y la hoja de ruta pendiente.

---

## 1. Identificación y Parámetros Inmutables

- **Proyecto:** Agentes de IA y Protocolo MCP para evaluación continua y autoevaluación en materias de Ingeniería en Informática.
- **Marco:** Convocatoria DASS UCSE 2025 – Iniciación a la Investigación (GIyT).
- **Período:** Noviembre 2025 – Octubre 2026.
- **Director:** Ing. Fabio Argañaraz (15 hs/sem).
- **Asesora Metodológica:** Ing. Gabriela Bejarano (6 hs/sem).
- **Estudiantes Investigadores:** Samara Zamar, Mariano Sumbaino, Gino Grosso.
- **Cátedras de Aplicación:**
  1. *Programación II* (3° año – Ing. en Informática).
  2. *Algoritmos y Programación* (1° año – Ing. en Informática).
  3. *Informática* (1° año – Tec. Univ. en Automatización y Robótica).

---

## 2. Hito Actual: 50% de Avance (Cierre del 1er Semestre - Julio 2026)

| Objetivo Específico | % Avance | Situación / Evidencia Principal |
| :--- | :---: | :--- |
| **OE1 (Arquitectura y MCP):** | **60%** | Desarrollados: Evaluador de Maquetación HTML+CSS y Generador de Exámenes React con MCP. |
| **OE2 (Integración Curricular):** | **100% / 50%** | Desplegado en Programación II (1er sem). En Algoritmos y Programación se incorporó a partir del segundo parcial y simulacros. |
| **OE3 (Evaluación de Impacto):** | **20%** | Instrumentado el "Sistema de Puntos de Ritmo" en planilla Excel. Recolección de telemetría en curso. |
| **OE4 (Transferencia y Difusión):** | **50%** | Guías operativas redactadas (`instructions_frontend/backend`). Propuesta de Taller Docente elevada para agosto 2026. |

---

## 3. Decisiones Arquitectónicas y Metodológicas Críticas Tomadas

1. **Bifurcación de Repositorios (Límites de GitHub Actions):**
   - *Decisión:* Actividades regulares operan en plantillas y repositorios **públicos** de GitHub Classroom (minutos ilimitados gratuitos de Actions). Repositorios privados reservados estrictamente a instancias de examen parcial.
2. **Disparo Idempotente de Issues:**
   - *Decisión:* Implementación de `setup-issues.yml` con comprobación de `gh issue list` para evitar fallas manuales de `workflow_dispatch`.
3. **Estrategia con Alumnos Recursantes:**
   - *Decisión:* Acompañamiento presencial y tutoriales paso a paso para neutralizar la resistencia inicial al flujo Git/Classroom frente al viejo modelo de ZIPs en campus virtual.
4. **Consolidación de Fuentes Primarias:**
   - *Estado:* Repositorio de [fuentes_primarias/](file:///c:/Universidad/Agentes%20de%20IA%20y%20Protocolo%20MCP%20para%20evaluaci%C3%B3n%20continua%20y%20autoevaluaci%C3%B3n%20en%20materias%20de%20Ingenier%C3%ADa%20en%20Inform%C3%A1tica%20-%202025/10_bibliografia/fuentes_primarias/) 100% completado con 20 documentos fuente (pedagógicos, metodológicos, normativos y técnicos) indexados en APA 7ª y con fichas de lectura analíticas.
5. **Migración de Plataforma LMS:**
   - *Decisión:* Ante el cierre de GitHub Classroom (28 de agosto de 2026), se migra la orquestación de TPs hacia [ClassMoji](file:///c:/Universidad/Agentes%20de%20IA%20y%20Protocolo%20MCP%20para%20evaluaci%C3%B3n%20continua%20y%20autoevaluaci%C3%B3n%20en%20materias%20de%20Ingenier%C3%ADa%20en%20Inform%C3%A1tica%20-%202025/10_bibliografia/fuentes_primarias/Classmoji%20A%20GitHub-Native%20LMS%20for%20Flexible%20CS%20Education.pdf), un LMS nativo de GitHub que permite mantener flujos de CI/CD basados en repositorios e incorpora evaluación flexible basada en tokens y emojis, alineándose al sistema de Puntos de Ritmo.

---

## 4. Próximos Pasos Inmediatos (Roadmap 2do Semestre 2026)

- [x] **Hito 1 (Agosto – Septiembre 2026):** Expansión del pilotaje a *Algoritmos y Programación* e *Informática* (Robótica).
- [ ] **Hito 2 (02 y 03 de Octubre 2026 - EN CURSO):** Dictado del Taller de Capacitación Docente Interno sobre Agentes de IA y Protocolo MCP (10 hs).
- [ ] **Hito 3 (Octubre - Noviembre 2026):** Consolidación estadística inferencial de los Puntos de Ritmo vs. calificaciones finales.
- [ ] **Hito 4 (Diciembre 2026):** Redacción del Informe Final y preparación del artículo científico para congreso (WICC/CACIC).
