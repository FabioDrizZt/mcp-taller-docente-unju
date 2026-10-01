# Arquitectura Técnica del Toolkit de Evaluación Continua con MCP

## 1. Visión General de la Arquitectura
El *Toolkit de Evaluación Continua con IA* está diseñado bajo una arquitectura orientada a servicios desacoplados, adoptando el estándar abierto **Model Context Protocol (MCP)** como bus de comunicación entre los agentes cognitivos y el entorno informático de ejecución.

```text
┌────────────────────────────────────────────────────────┐
│                   Cliente de IA / LLM                  │
│       (Claude Desktop, Antigravity IDE, Extensiones)   │
└───────────────────────────┬────────────────────────────┘
                            │ Protocolo MCP (JSON-RPC)
                            │ Transport: stdio / SSE
┌───────────────────────────▼────────────────────────────┐
│                    Servidor MCP Central                │
│                 (Capa de Orquestación)                 │
├───────────────────────────┬────────────────────────────┤
│ Herramientas Expuestas:   │ Recursos Expuestos:        │
│ • evaluate_html_css       │ • repo://assignments/*     │
│ • generate_react_exam     │ • rubric://p2/frontend     │
│ • run_code_linter         │ • stats://student/metrics  │
│ • generate_feedback_issue │                            │
└─────────────┬───────────────────────────┬──────────────┘
              │                           │
              ▼                           ▼
┌───────────────────────────┐ ┌──────────────────────────┐
│ Evaluadores Especializados│ │ Plataformas Educativas   │
│ • Headless Chromium / DOM │ │ • GitHub Classroom API   │
│ • Jest / Vitest Runner    │ │ • Git Engine (Local/CLI) │
│ • Clang-format / cppcheck │ │ • Planilla Excel/DB Sync │
└───────────────────────────┘ └──────────────────────────┘
```

---

## 2. Componentes Nucleares

1. **Capa de Abstracción MCP:**
   - Define contratos estrictos mediante esquemas JSON Schema para cada herramienta (`tools`) y recurso (`resources`).
   - Garantiza que cualquier agente compatible con MCP pueda invocar los evaluadores de forma agnóstica al modelo de lenguaje subyacente.

2. **Capa de Ejecución Determinista:**
   - Contenedores o entornos aislados donde se compila el código del estudiante y se ejecutan pruebas automáticas sin acceso a red no autorizada.
   - Prevención de ejecuciones maliciosas o bucles infinitos mediante timeouts estrictos.

3. **Capa de Síntesis Pedagógica:**
   - Transforma los diagnósticos técnicos en comentarios formateados en Markdown estructurado, vinculándolos a las rúbricas y criterios de la cátedra.
