# Diseño Metodológico: Enfoque de Investigación-Acción Educativa y Métodos Mixtos

## 1. Justificación del Paradigma: Investigación-Acción (Educational Action Research)
El proyecto adopta un diseño de **Investigación-Acción Educativa** (Kemmis & McTaggart; Elliott) articulado con un enfoque de **métodos mixtos** (Creswell). La investigación-acción resulta óptima dado que:
- El investigador principal es a la vez docente a cargo de las cátedras de intervención, permitiendo una observación participante directa.
- El objetivo no es meramente descriptivo, sino transformador: introducir innovaciones tecnológicas en el aula, monitorear sus efectos en tiempo real y refinar los instrumentos pedagógicos durante el propio ciclo lectivo.

El proceso se estructura en espirales de cuatro momentos iterativos:
1. **Planificar:** Co-diseñar competencias, rúbricas analíticas y plantillas de trabajo.
2. **Actuar:** Desplegar los agentes MCP, GitHub Classroom y workflows de autograding.
3. **Observar:** Registrar la telemetría de commits, issues, calificaciones de ritmo y respuestas estudiantiles.
4. **Reflexionar:** Analizar incidencias técnicas (e.g. cuotas de Actions) o de adopción (resistencia de recursantes) e implementar ajustes inmediatos.

---

## 2. Fases de Ejecución del Proyecto

### Fase 1: Análisis y Co-Diseño Curricular (Noviembre 2025 – Marzo 2026)
- Desglose de competencias según CONFEDI y RM 1557/2021 para *Programación II* y *Algoritmos y Programación*.
- Construcción de matrices de rúbricas analíticas estructuradas.
- Definición de tareas auténticas y criterios de aceptación funcional y no funcional.

### Fase 2: Desarrollo Tecnológico e Integración MCP (Febrero 2026 – Mayo 2026)
- Desarrollo de servidores MCP para validación y generación evaluativa (Evaluador HTML+CSS, Generador de Prácticos de React).
- Configuración de pipelines en GitHub Actions y resolución de flujos idempotentes (`setup-issues.yml`).
- Adaptación a restricciones de infraestructura (migración de assignments formativos a plantillas públicas).

### Fase 3: Pilotaje de Campo en Cursadas (Marzo 2026 – Octubre 2026)
- **1er Semestre (Marzo – Junio 2026):** Pilotaje intensivo en *Programación II* y despliegue modular en *Algoritmos y Programación* a partir del segundo examen y simulacros.
- **2do Semestre (Agosto – Octubre 2026):** Consolidación en *Algoritmos y Programación* e *Informática*, acompañada del dictado del taller docente de transferencia.

### Fase 4: Evaluación de Impacto, Sistematización y Transferencia (Julio – Octubre 2026)
- Triangulación de datos cuantitativos (Puntos de Ritmo, planillas de entregas) y cualitativos (análisis de Pull Requests, encuestas de percepción estudiantil y docente).
- Redacción del informe final, elaboración de publicaciones científicas y liberación del Toolkit institucional.
