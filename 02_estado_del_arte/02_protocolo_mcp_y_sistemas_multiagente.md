# Sistemas Multi-Agente y el Protocolo MCP (Model Context Protocol)

## 1. El Surgimiento del Model Context Protocol (MCP)
Hasta finales de 2024, la integración de modelos de lenguaje con herramientas externas requería la construcción de conectores propietarios ad-hoc (Function Calling específico de cada proveedor, plugins monolíticos o frameworks pesados con alto acoplamiento).

El lanzamiento del **Model Context Protocol (MCP)** como estándar abierto de código abierto introdujo un cambio de paradigma equivalente al impacto del protocolo HTTP en la web o del *Language Server Protocol (LSP)* en los entornos de desarrollo (IDEs):
- **Desacoplamiento:** Separa de forma estricta el cliente de IA (el modelo de lenguaje o entorno de usuario) del servidor de contexto/herramientas (servidores MCP especializados).
- **Seguridad y Control de Acceso:** Permite exponer recursos locales (archivos, repositorios Git, bases de datos SQLite) y herramientas ejecutables (compiladores, evaluadores de maquetación, generadores de rúbricas) con permisos explícitos y trazables.
- **Portabilidad:** Un servidor MCP evaluador desarrollado para un entorno puede conectarse de forma transparente a Claude Desktop, VS Code, Gemini CLI u orquestadores en la nube.

---

## 2. Paradigma de Sistemas Multi-Agente en Educación
A diferencia de un único agente genérico ("asistente todoterreno"), un sistema multi-agente distribuye responsabilidades especializadas:
1. **Agente Evaluador Estático:** Analiza estructura de código, convenciones de estilo y calidad de maquetación/diseño.
2. **Agente de Pruebas Dinámicas:** Ejecuta suites de tests, analiza tiempos de ejecución y verifica casos de borde.
3. **Agente Pedagógico / Retroalimentador:** Transforma los resultados técnicos crudos en devoluciones formativas estructuradas conforme a rúbricas pedagógicas, cuidando el tono discursivo y evitando la resolución automática de la tarea.
4. **Agente Auditor:** Monitorea la consistencia de las devoluciones, detecta posibles sesgos y registra métricas operativas.

---

## 3. Estado de la Adopción Académica
A la fecha de desarrollo del proyecto (2025–2026), la literatura sobre MCP en educación superior es incipiente. La gran mayoría de implementaciones previas se basaban en APIs cerradas o chatbots sin conexión determinista a herramientas de aula virtual. Asimismo, si bien han surgido avances recientes en plataformas de gestión nativas sobre GitHub orientadas a la evaluación alternativa y flexible como **ClassMoji** (Traore & Tregubov, ACM SIGCSE 2026), la articulación sinérgica entre un LMS nativo de Git y un bus desacoplado de agentes inteligentes bajo Model Context Protocol (MCP) constituye una contribución de frontera. Este proyecto sitúa a la UCSE-DASS a la vanguardia de la investigación aplicada en esta convergencia técnica y pedagógica.
