# Anexo 1: Matrices de Rúbricas Analíticas para Evaluación Continua

A continuación se presentan los modelos de rúbricas analíticas estructuradas utilizadas para parametrizar las evaluaciones formativas y la revisión de Pull Requests en las cátedras:

## Rúbrica 1: Maquetación Frontend (HTML Semántico & CSS Responsivo)

| Criterio / Nivel | Excelente (100%) | Satisfactorio (75%) | En Proceso (50%) | Insuficiente (0-25%) |
| :--- | :--- | :--- | :--- | :--- |
| **Semántica HTML5** | Uso estricto de elementos semánticos (`<main>`, `<section>`, `<nav>`, `<article>`). Jerarquía `<h1>-<h6>` coherente y única. | Uso mayoritario de etiquetas semánticas con pequeñas omisiones menores. | Abuso excesivo de `<div>` y `<span>`. Jerarquía de títulos desordenada. | Código carente de semántica. Errores graves de estructura o anidamiento. |
| **Responsividad y Layout** | Implementación fluida de Flexbox y CSS Grid. Breakpoints limpios en `@media` sin desbordes horizontales. | Diseño responsivo funcional en pantallas estándar pero con pequeños desajustes visuales. | Desbordes horizontales o colapso de elementos en dispositivos móviles. | Diseño rígido no responsivo. Uso de anchos fijos en píxeles. |
| **Accesibilidad (a11y)** | Atributos `alt` descriptivos, contraste de color acorde a WCAG AA, navegación completa por teclado. | Contraste adecuado y la mayoría de elementos con etiquetas de accesibilidad. | Falta de contraste o imágenes sin atributos alternativos. | Elementos interactivos inaccesibles o contraste deficiente. |

---

## Rúbrica 2: Componentes y Estado en React

| Criterio / Nivel | Excelente (100%) | Satisfactorio (75%) | En Proceso (50%) | Insuficiente (0-25%) |
| :--- | :--- | :--- | :--- | :--- |
| **Modularización** | Componentes pequeños, reutilizables y con una única responsabilidad clara (Single Responsibility). | Buena modularización, aunque algún componente concentra lógica excesiva. | Componentes monolíticos con mezcla de responsabilidades. | Todo el código concentrado en un único componente gigante. |
| **Manejo de Estado (Hooks)** | Uso idóneo de `useState` y `useEffect`. Inmutabilidad preservada en arreglos y objetos. Limpieza de efectos. | Estado funcional pero con mutaciones indirectas o dependencias innecesarias en efectos. | Problemas de sincronización de estado, bucles de re-renderizado. | Manejo erróneo del estado que causa fallos de ejecución. |
| **Consumo de APIs y Errores** | Manejo integral de estados de carga (`loading`), éxito y captura de errores (`try/catch` con UI informativa). | Consumo exitoso de API pero sin feedback visual explícito ante fallos de red. | Errores de red no controlados que congelan la aplicación. | No conecta con la API o falla en el parsing JSON. |
