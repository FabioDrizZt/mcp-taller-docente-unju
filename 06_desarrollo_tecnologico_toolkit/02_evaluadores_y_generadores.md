# Evaluadores Especializados, Generadores de Exámenes y Andamiaje Técnico

Durante el desarrollo del proyecto (cumplimiento del 60% en el OE1 y avance sostenido en el OE2), se estructuró un ecosistema de herramientas desacopladas compuestas por evaluadores deterministas, generadores basados en LLMs bajo contratos MCP, y un andamiaje técnico de soporte al estudiante:

---

## 1. Evaluador de Maquetación HTML + CSS
- **Objetivo Pedagógico:** Evaluar en *Programación II* la adopción de HTML semántico, diseño responsivo (Flexbox / CSS Grid), accesibilidad (a11y) y orden de reglas CSS sin intervención humana inicial.
- **Mecanismo Operativo:**
  - El servidor MCP inspecciona el árbol DOM y el CSS computado mediante un motor headless Chromium.
  - Verifica reglas explícitas de la consigna: jerarquía de encabezados `<h1>` a `<h6>`, etiquetas semánticas (`<header>`, `<main>`, `<article>`, `<footer>`), contraste cromático WCAG y breakpoints `@media`.
  - Emite un reporte de sugerencias de optimización estructurado en Markdown (feedforward), sin penalizar variaciones estéticas menores válidas.

---

## 2. Andamiaje Estructural y "Muletas" de Código (`Configuration-Files`)
Para evitar que los estudiantes de los primeros años tropiecen con dificultades de sintaxis o configuración de bajo nivel y garantizar que sus producciones ingresen al evaluador en un estado predecible:
- **Estandarización de Archivos de Configuración:** Se crearon plantillas fijas con `.editorconfig`, `.prettierrc`, `.stylelintrc`, `tsconfig.json` y `vite.config.js`.
- **Efecto Pedagógico:** Estas "muletas" (*scaffolding*) orientan al estudiante en la tabulación uniforme, cierre de etiquetas, orden de propiedades CSS y tipado estricto, transformando las advertencias del linter en micro-retroalimentación formativa en tiempo real mientras programa en su propio entorno.

---

## 3. Generador de Exámenes Prácticos de React
- **Objetivo Pedagógico:** Dinamizar la creación de enunciados y rúbricas auténticas y diferenciadas para instancias de evaluación sumativa y simulacros prácticos.
- **Capacidades Integradas mediante MCP:**
  - **Generación Multi-Tema:** Capaz de producir variantes equilibradas en complejidad algorítmica (manejo de estado, props, hooks personalizados, consumo de APIs REST).
  - **Inyección de Suites de Pruebas Automáticas:** Cada examen generado incluye automáticamente sus casos de prueba unitarios (Vitest / Testing Library) listos para integrarse al runner de evaluación.
  - **Rúbrica Matricial:** Genera la matriz de corrección con puntajes ponderados por competencia técnica demostrada según los estándares CONFEDI.

---

## 4. Evolución y Ecosistema de Skills para Algoritmos y Programación (C++)
Para la asignatura anual de 1° año *Algoritmos y Programación*, el sistema experimentó una evolución metodológica significativa en la automatización de evaluación:

### 4.1. Historia Evolutiva de la Generación de Desafíos
1. **Fase 1: Prompts Simples (El problema de la automatización):** Inicialmente, se utilizaron *prompts* simples sin documentar para generar enunciados de ejercicios en PSeInt, obteniendo resultados en formato Markdown estático. Esto demostró ser un error metodológico, ya que la falta de estandarización impedía la automatización a escala.
2. **Fase 2: Plantillas HTML y Generadores Base:** Posteriormente, los Trabajos Prácticos (TPs) evolucionaron hacia enunciados en formato HTML, acompañados de la creación de un `generadorDesafios.md` para dotar de mayor estructura al proceso iterativo.
3. **Fase 3: Refuerzo y Autoevaluación:** Se incorporó el `skill_creador_clases_quizizz.md`, permitiendo generar andamiaje remedial automático para que los alumnos repasaran errores conceptuales comunes, sin la sobrecarga de crear ejercicios de código completos para cada falencia.
4. **Fase 4: Spec-Driven Development (SDD):** El descubrimiento crítico fue la necesidad de un paso previo antes de la generación: la creación de un documento de Especificación (SDD.md). El agente ahora debe presentar y confirmar esta especificación con el docente antes de avanzar a generar todo el paquete (código, rúbricas, pruebas de escritorio y HTML).

### 4.2. Ecosistema Actual de Generadores SDD
Con base en esta evolución, el ecosistema se compone actualmente de skills especializados:
1. **Generadores SDD de 3 Temas Equilibrados:**
   - `ayp-examenes-sdd`: Generador de especificaciones Spec-Driven Development para el Módulo 2.
   - `ayp-examenes-m3-sdd` y `ayp-examenes-m4-sdd`: Generadores de paquetes completos de exámenes para Arreglos Unidimensionales, Búsqueda, Ordenamiento y Structs (100% código en C++, modernos, sin vectores paralelos obsoletos).
2. **Generador Psicométrico de Clases y Cuestionarios:**
   - `ayp-clases-quizizz`: Herramienta que genera contenidos teóricos y cuestionarios psicométricos sin sesgo para plataformas formativas.
3. **Validación Estática de Código C++:**
   - Reglas de verificación con `clang-format` y `cppcheck` expuestas como herramientas MCP para comprobar la modularización en funciones, paso adecuado de parámetros (valor vs referencia) y prevención de desbordamiento de memoria (*buffer overflow*).

---

## 5. Generadores para Entornos Masivos y Conceptos Abstractos (UNJu e Informática UCSE)
La investigación se expandió para abarcar entornos de evaluación no centrados exclusivamente en la validación de código fuente tradicional:
1. **Informática (UCSE):** Se implementó un `generador_examenes.md` como aproximación inicial a la automatización en materias de perfil técnico-mecatrónico.
2. **Sistemas Operativos II y Teoría de los Sistemas Operativos (UNJu):** Frente al desafío de la masividad (más de 100 alumnos por cohorte) y la naturaleza abstracta de los contenidos teóricos, se diseñó un enfoque innovador utilizando `skill_creador_TPs.md`:
   - **Laboratorios Interactivos:** Creación de interfaces y simuladores web para que los estudiantes interioricen conceptos abstractos de arquitectura y gestión de sistemas operativos.
   - **Evaluación Autoguiada (Quizizz):** Generación de cuestionarios de repaso dinámicos ejecutables antes de las clases prácticas para afianzar la teoría dictada por la Jefatura de Cátedra.
   - **Prácticas de Terminal y Concurrencia:** Para *Sistemas Operativos II*, se automatizó la generación de consignas prácticas de comandos Linux en entornos WSL. Para *Teoría de los Sistemas Operativos*, se generaron laboratorios guiados con código en Python para demostrar escenarios de sincronización de procesos.

---

## 6. Integración con el Bus MCP y Ejecución en CI/CD (GitHub Actions / ClassMoji)
La interoperabilidad se logra mediante el desacoplamiento:
- Los **agentes cognitivos** (en Antigravity IDE o Claude Desktop) consultan las herramientas a través de JSON-RPC estándar del protocolo MCP.
- Los **runners automatizados** en los repositorios de los estudiantes (orquestados inicialmente por GitHub Actions y gestionados actualmente por ClassMoji) ejecutan los mismos linters y pruebas unitarias de forma desasistida, garantizando total consistencia entre lo que el agente recomienda localmente y lo que la plataforma evalúa remotamente.
