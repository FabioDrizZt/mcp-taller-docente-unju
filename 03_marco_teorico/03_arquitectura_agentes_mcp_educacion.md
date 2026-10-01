# El Agente MCP como Andamiaje Evaluativo y Mediador Pedagógico

## 1. El Concepto de Andamiaje Cognitivo (Scaffolding) Asistido por IA
El andamiaje (Bruner, Wood & Ross) refiere al soporte temporal proporcionado por un tutor experto para permitir a un aprendiz resolver problemas que exceden sus capacidades actuales de forma autónoma (Zona de Desarrollo Próximo de Vygotsky).

En este marco, el **Agente de IA orquestado con MCP** no sustituye al docente ni realiza el trabajo del estudiante: opera como un **mediador de andamiaje evaluativo**. Sus características fundamentales son:
- **Disponibilidad Permanente:** Ofrece orientación en el momento exacto en que el estudiante se encuentra bloqueado en su sesión de desarrollo.
- **Gradación del Soporte:** Adapta la granularidad de la ayuda (desde pistas conceptuales de alto nivel hasta la señalización de un error sintáctico o lógico concreto).
- **Retiro Progresivo del Apoyo:** Conforme el estudiante avanza en la cursada y domina las competencias base, los requerimientos de autoevaluación aumentan y la intervención del agente se orienta a estándares más rigurosos (modularidad, eficiencia temporal/espacial, patrones de diseño).

---

## 2. Soberanía del Juicio Pedagógico Docente
Un axioma epistemológico y normativo de este proyecto es que **la IA no califica de forma definitiva ni toma decisiones académicas de acreditación**. 
- Los agentes MCP generan *informes de evaluación formativa*, analizan métricas estáticas y reportan resultados de pruebas automáticas.
- La valoración final de la competencia, la revisión de los *Pull Requests*, el análisis de la originalidad del proceso y la asignación de notas sumativas permanecen bajo la potestad exclusiva de los docentes a cargo de las cátedras.

---

## 3. Modelo Arquitectónico de Interacción Pedagógica
```text
┌─────────────────┐       git push       ┌────────────────────────┐
│   Estudiante    │ ───────────────────> │ Repositorio GitHub     │
│   (VS Code /    │                      │ (Classroom Template)   │
│   Local Git)    │ <─────────────────── │                        │
└─────────────────┘      Feedback PR     └───────────┬────────────┘
         │                                           │ Dispara
         │ Consulta interactiva                      ▼
         ▼                               ┌────────────────────────┐
┌─────────────────┐    Protocolo MCP     │  GitHub Actions /      │
│  Agente MCP     │ <──────────────────> │  Runner de Pruebas     │
│  (Evaluador/    │   Herramientas       │  (Autograding)         │
│   Generador)    │   de inspección      └───────────┬────────────┘
└─────────────────┘                                  │
         │ Reportes y analíticas                     ▼
         └─────────────────────────────> ┌────────────────────────┐
                                         │ Equipo Docente (UCSE)  │
                                         │ Revisión & Acreditación│
                                         └────────────────────────┘
```
