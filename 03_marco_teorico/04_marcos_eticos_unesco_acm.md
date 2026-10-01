# Marcos Éticos, Integridad Académica y Directrices UNESCO / ACM

## 1. Directrices Internacionales: UNESCO (2023)
La *Guía para el uso de IA Generativa en Educación e Investigación* de la UNESCO establece directrices mandatorias adoptadas por este proyecto:
- **Protección de la privacidad y minimización de datos:** Los datos de los estudiantes (código fuente, correos, registros de actividad) no deben ser utilizados para reentrenar modelos comerciales cerrados sin consentimiento explícito. Se minimiza la transmisión de datos personales identificables (PII).
- **Inclusión y Equidad:** El acceso a los agentes de evaluación debe ser universal dentro de la cohorte, garantizando que ningún estudiante quede en desventaja por cuestiones de conectividad o capacidad de pago (uso de infraestructura provista por la universidad o cuotas gratuitas abiertas).
- **Desarrollo del Pensamiento Crítico:** El sistema debe evitar crear una relación de dependencia pasiva, promoviendo en todo momento la metacognición y el cuestionamiento activo de las sugerencias del agente.

---

## 2. Código de Ética y Conducta Profesional de la ACM (2018)
La Association for Computing Machinery (ACM) define responsabilidades éticas fundamentales para los profesionales y educadores en computación:
- **Sección 1.2 (Evitar el daño):** Mitigar consecuencias negativas imprevistas de los sistemas automáticos, como el estrés por evaluaciones punitivas automatizadas o fallos falsos positivos en suites de tests.
- **Sección 1.4 (Ser justo y actuar sin discriminar):** Evitar sesgos algorítmicos que beneficien o perjudiquen a ciertos estilos de programación válidos.
- **Sección 2.5 (Otorgar evaluaciones comprensivas y exhaustivas de los sistemas):** Auditar los agentes para evaluar sus limitaciones de razonamiento, alucinaciones y consistencia interna.

---

## 3. Protocolos Operacionales de Integridad y Transparencia en el Proyecto
1. **Transparencia en el Origen del Feedback:** Toda retroalimentación generada total o parcialmente por un modelo de IA se rotula explícitamente como tal ante el alumno, informando qué agente intervino y con qué criterios.
2. **Registro de Auditoría (*Audit Trail*):** Se mantiene trazabilidad de las interacciones entre los agentes evaluadores y los repositorios de los estudiantes para eventuales revisiones pedagógicas o reclamos.
3. **Mecanismos de Contingencia ante Fallos Críticos:** En caso de que un flujo de Actions o un agente MCP experimente una degradación o error de servicio, se activan de inmediato canales alternativos tradicionales de entrega y corrección docente sin penalización temporal para el alumnado.
