# Instrumentos de Medición y Recolección de Datos

Para asegurar una triangulación metodológica robusta, se combinan instrumentos cuantitativos de base operativa con instrumentos cualitativos de percepción:

## 1. Instrumentos Cuantitativos

### A. Sistema de Puntos de Ritmo (Gestión Temporal y Continuidad)
- **Definición:** Mecanismo cuantitativo diseñado para operacionalizar la evaluación formativa procesual. Evalúa la constancia temporal, la frecuencia de commits significativos y el cumplimiento temprano de hitos intermedios antes del cierre definitivo de la actividad.
- **Registro:** Planilla de cálculo centralizada (Excel) donde se consolidan semanalmente:
  - Fecha del primer commit vs. fecha límite (*anticipación*).
  - Tasa de aprobación de suites de pruebas automáticas en el primer intento vs. reintentos (*iteración correctiva*).
  - Puntos de ritmo acumulados por entrega y por alumno.

### B. Telemetría de GitHub Classroom y GitHub Actions
- **Tiempos de feedback:** Medición de latencia desde el `git push` hasta la publicación de resultados de las pruebas o apertura de issues formativas.
- **Rendimiento de builds:** Tasa de éxito/fracaso de las ejecuciones de Actions.

---

## 2. Instrumentos Cualitativos

### A. Rúbricas Analíticas en Pull Requests
- Instrumento docente para la revisión cualitativa de código. A diferencia de las pruebas unitarias que verifican requerimientos funcionales (`assert`), la rúbrica evalúa:
  - Legibilidad y nomenclatura estandarizada.
  - Modularización y cohesión de componentes.
  - Manejo de excepciones y casos de borde no contemplados en los tests automáticos.

### B. Cuestionarios de Percepción Estudiantil (Encuestas de Salida)
- Diseñado sobre una escala Likert de 5 puntos complementada con preguntas abiertas:
  - Grado de utilidad de las devoluciones automáticas.
  - Percepción de reducción de la ansiedad ante la entrega.
  - Nivel de confianza depositado en las observaciones de los agentes.
  - Dificultades experimentadas con la herramienta Git/Classroom.

### C. Registro Reflexivo del Equipo Docente (Diario de Campo)
- Bitácora sistemática del Director de proyecto y colaboradores que documenta incidencias técnicas imprevistas, preguntas recurrentes en horarios de consulta y observaciones directas durante las clases prácticas.
