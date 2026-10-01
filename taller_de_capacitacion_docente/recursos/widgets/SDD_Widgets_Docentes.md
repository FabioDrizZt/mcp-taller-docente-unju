# Especificación de Diseño (SDD) - Widgets Interactivos para Taller Docente

## 1. Propósito General
Diseñar y desarrollar un conjunto de **Widgets Web Interactivos** de Nivel 1 (Modelos Conceptuales) que se incrustarán o utilizarán durante las presentaciones del taller docente. Su objetivo es tangibilizar visualmente los conceptos teóricos más abstractos del **Día 1** (Carga Cognitiva, Flujo SDD y Puntos de Ritmo) para persuadir y educar a los docentes participantes mediante la interacción directa.

## 2. Pila Tecnológica (Stack)
Para demostrar el "verdadero poder" de los laboratorios web, abandonaremos el CSS/JS vainilla básico y utilizaremos herramientas estándar de la industria mediante CDN (sin necesidad de compilación local pesada, ideal para distribuir a docentes):
- **Estilos:** `TailwindCSS` (vía CDN script) para un diseño *glassmorphism* moderno, paletas de colores vibrantes y utilidades tipográficas.
- **Animaciones Complejas:** `GSAP (GreenSock)` para orquestar líneas de tiempo (timelines) complejas, movimiento de datos y transiciones fluidas.
- **Simulación de IA:** `TypeIt.js` para simular de forma realista la generación de texto (efecto máquina de escribir de los LLM).
- **Visualización de Datos:** `Chart.js` para renderizar gráficos analíticos interactivos.
- **Iconografía:** `Lucide Icons` o `FontAwesome` para representaciones visuales de repositorios, IDEs y agentes.

---

## 3. Especificación de los Widgets (Catálogo)

### Widget 1: "La Tubería MCP" (Para Unidad 1: Chatbot vs Agente)
**Objetivo:** Demostrar físicamente la reducción de la **Carga Cognitiva Docente** al pasar del "Copy-Paste" manual a un Agente conectado vía MCP.
- **Interfaz Visual:**
  - Pantalla dividida. Arriba: "Modo Chatbot Tradicional". Abajo: "Modo Agente con MCP".
  - **Medidores en tiempo real:** Barras de progreso circulares para "Carga Cognitiva" y "Tiempo Invertido".
- **Interactividad & Animación (GSAP):**
  - *Modo Chatbot:* El docente debe arrastrar manualmente (Drag & Drop) íconos de "Código del Alumno" hacia una ventana de "ChatGPT", y luego arrastrar el "Feedback" de vuelta al "Repositorio". Cada acción manual dispara el medidor de Carga Cognitiva hacia el rojo.
  - *Modo Agente MCP:* El docente hace clic en un único botón *"Luz Verde (Evaluar)"*. GSAP anima un flujo de datos continuo (partículas de luz) viajando por una tubería desde el Repositorio -> Herramientas -> Agente -> Feedback, todo en 2 segundos. La Carga Cognitiva se mantiene en verde.

### Widget 2: "El Colapso Zero-Shot vs. Flujo SDD" (Para Unidad 4: SDD)
**Objetivo:** Evidenciar por qué pedirle a la IA que "genere un examen" en un solo prompt (Zero-Shot) genera alucinaciones, y cómo el SDD lo soluciona.
- **Interfaz Visual:**
  - Dos terminales tipo consola (estética hacker/IDE oscuro con Tailwind).
- **Interactividad & Animación (TypeIt.js):**
  - *Boton "Generar Zero-Shot":* TypeIt.js simula un prompt apresurado (*"Hacé un lab de arreglos"*). Inmediatamente, la consola escupe un código masivo y desordenado. Se marcan en rojo 3 "Alucinaciones" (ej. "Usa punteros cuando la cátedra no lo permite").
  - *Botón "Flujo SDD":* Se activa un *Wizard* interactivo de 3 pasos:
    1. Especificar Contexto (Se ingresa un bloque verde).
    2. Establecer Reglas/Skill (Se ingresa un bloque azul).
    3. Luz Verde (Botón de Aprobación).
    Tras la aprobación, TypeIt.js genera un código limpio, estructurado y sin errores rojos.

### Widget 3: "La Anatomía del Ritmo" (Para Unidad 6: Ética y Ritmo)
**Objetivo:** Diferenciar visualmente la "evaluación del producto final" de la "evaluación del proceso" (Puntos de Ritmo).
- **Interfaz Visual:**
  - Un dashboard analítico moderno utilizando `Chart.js` con curvas suavizadas (tension) y tooltips interactivos.
- **Interactividad & Animación:**
  - El usuario puede alternar entre dos perfiles de estudiantes:
    - **Perfil A (El Procrastinador):** Línea de actividad plana durante 14 días y un pico vertical gigante a las 3:00 AM del día de entrega. El sistema calcula: *Nota Final: 10/10 | Puntos de Ritmo: 0/100 (Alerta de Riesgo)*.
    - **Perfil B (El Iterativo):** Curva de actividad en escalera (pequeños commits cada 3 días), integrando feedback de la IA. El sistema calcula: *Nota Final: 10/10 | Puntos de Ritmo: 95/100*.
  - Al pasar el ratón por los nodos de la gráfica, tooltips de Tailwind muestran los "Emojis de ClassMoji" recibidos en cada etapa.

---

## 4. Criterios de Aceptación (Definición of Done)
1. Los tres widgets deben funcionar como archivos `HTML` independientes (para fácil distribución a los docentes).
2. Deben ser 100% responsivos y no requerir dependencias locales de Node.js (todo vía CDN).
3. La interfaz de usuario debe tener una estética *premium* (Glassmorphism, sombras suaves, transiciones de estado) estrictamente construida con TailwindCSS.
4. No deben requerir un servidor backend; toda la lógica de simulación vivirá en el cliente (JavaScript puro).
