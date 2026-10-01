# Justificación Curricular, Institucional y Profesional

## 1. Alineación con las Políticas Institucionales de UCSE-DASS
El Plan de Estudios vigente para la carrera de Ingeniería en Informática de la Universidad Católica de Santiago del Estero (UCSE) explicita formalmente la necesidad de implementar un **"régimen continuo de evaluación"**, complementado por el fortalecimiento de las prácticas formativas en laboratorios y talleres de computación. 

Operacionalizar este mandato a escala, en materias con alta carga horaria y masividad, se vuelve inviable mediante corrección exclusivamente analógica y manual. El presente proyecto proporciona el andamiaje tecnológico y procedimental indispensable para materializar dicho mandato estatutario.

---

## 2. Marco Normativo Nacional: RM 1557/2021 y CONFEDI (Libro Rojo)
A nivel nacional, el sistema universitario argentino se rige por:

- **Resolución Ministerial N° 1557/2021 (Ministerio de Educación de la Nación):**
  Establece los estándares de acreditación para los títulos de Ingeniería en Informática y Ciencias de la Computación, exigiendo una formación orientada a resultados de aprendizaje, capacidad de autoaprendizaje, trabajo en equipo y uso de metodologías profesionales de desarrollo y pruebas de software.
- **Libro Rojo de CONFEDI (Estándares de Segunda Generación):**
  Promueve la transición desde una enseñanza basada en contenidos enciclopédicos hacia un **modelo formativo centrado en competencias genéricas y específicas**. Entre ellas destacan:
  - *Competencia Específica:* Desarrollar, probar y mantener software seguro y eficiente.
  - *Competencia Genérica:* Aprendizaje continuo y autónomo (autorregulación).
  - *Evaluación Formativa:* Exigencia de evidencias e instrumentos de evaluación auténtica y continua.

---

## 3. Justificación Tecnológica y Disciplinar
La integración de tecnologías de la información en el proceso evaluativo ha transitado por diversas etapas:
1. **Autograders clásicos basados en regex o asserts rígidos:** Eficientes pero inflexibles, propensos a calificar negativamente soluciones algorítmicamente válidas pero con variaciones estilísticas no contempladas.
2. **Asistentes conversacionales opacos:** Aunque ofrecen explicaciones en lenguaje natural, operan como "cajas negras" desconectadas del entorno de ejecución, incapaces de validar ejecución real de pruebas o inspeccionar artefactos con trazabilidad.
3. **El paradigma emergente de Agentes orquestados con Model Context Protocol (MCP):**
   - El protocolo MCP permite a los agentes de IA comunicarse de forma estandarizada y segura con herramientas deterministas: ejecutores de pruebas unitarias, linter estáticos, repositorios Git y bancos de preguntas.
   - Esto combina lo mejor de ambos mundos: la **precisión determinista del código ejecutable** con la **empatía pedagógica y riqueza explicativa de los modelos de lenguaje**.

---

## 4. Relevancia y Aporte Social
- **Para los estudiantes:** Acceso a devoluciones 24/7, reducción de la ansiedad de entrega, adquisición de hábitos profesionales de integración continua (CI/CD) y control de versiones con Git desde el primer año.
- **Para el cuerpo docente:** Descompresión de tareas mecánicas de corrección de sintaxis y estilos, liberando tiempo pedagógico para tutoría personalizada y análisis de dificultades conceptuales profundas.
- **Para la institución:** Modelo transferible y escalable a otras carreras tecnológicas del DASS y una base de evidencia empírica local para la regulación del uso responsable de IA en la educación superior.
