# Registro de Incidentes Críticos, Fricciones y Lecciones Aprendidas

La metodología de investigación-acción demanda documentar con total transparencia tanto las dificultades técnicas como las pedagógicas acontecidas y el modo riguroso en que fueron superadas:

## 1. Incidente 1: Agotamiento de Cuotas de GitHub Actions en Repositorios Privados
- **Descripción del Problema:** Inicialmente, para resguardar la autoría individual y evitar plagio entre pares, cada assignment de GitHub Classroom se creaba como repositorio privado. Debido a que GitHub impone una cuota limitada de minutos gratuitos de Actions en repositorios privados educativos, el uso masivo por decenas de alumnos disparando builds recurrentes agotó la cuota mensual en menos de dos semanas, suspendiendo el autograding.
- **Modo de Resolución:** Se rediseñó la política de repositorios: las actividades formativas semanales y prácticas de laboratorio se migraron a **plantillas públicas y repositorios públicos** (con minutos de Actions ilimitados y gratuitos). Se restringió el uso de repositorios privados exclusivamente a las evaluaciones parciales formales sincrónicas.
- **Impacto Metodológico:** Favoreció la cultura de colaboración abierta e impulsó el portafolio profesional público de los estudiantes en GitHub.

---

## 2. Incidente 2: Falla en el Disparo de Issues Formativas Automáticas
- **Descripción del Problema:** Al aceptar el assignment desde el enlace de Classroom, la acción encargada de poblar las *issues* formativas (`setup-issues`) no se disparaba automáticamente de forma confiable, requiriendo que el estudiante ejecutara manualmente un *workflow_dispatch*, lo que causaba confusión y demoras.
- **Modo de Resolución:** Se investigó la secuencia de eventos de GitHub Actions y se diseñó una solución definitiva mediante una configuración en los YAML (`setup-issues.yml`) con disparador en el primer push y verificación idempotente (evita duplicación de issues si ya existen), automatizando el 100% del proceso sin intervención manual.

---

## 3. Incidente 3: Fricción Cultural y Resistencia en Alumnos Recursantes
- **Descripción del Problema:** Estudiantes que habían cursado la materia en años anteriores bajo la modalidad tradicional (descargar enunciados en PDF y subir archivos ZIP sueltos a la plataforma Moodle) manifestaron resistencia y confusión frente al flujo automatizado de GitHub Classroom. En varios casos, en lugar de aceptar formalmente el assignment oficial, optaban por clonar, descargar el ZIP o crear repositorios personales aislados, perdiendo la vinculación con las Actions de autoevaluación continua.
- **Modo de Resolución:** El equipo docente detectó rápidamente la anomalía y desplegó una estrategia de intervención focalizada:
  1. Diálogo explicativo personalizado demostrando el beneficio directo del feedback en tiempo real.
  2. Acompañamiento guiado en el laboratorio para realizar el ciclo completo (`Aceptar Assignment -> git clone -> git commit -> git push -> Autograding`).
  3. Redacción de tutoriales visuales paso a paso.
- **Resultado:** Tras las dos primeras semanas de adaptación, la totalidad de los recursantes se integró de forma exitosa al flujo oficial de la cátedra.

---

## 4. Incidente 4: Cierre del Servicio GitHub Classroom y Transición Resiliente a ClassMoji
- **Descripción del Problema:** El 28 de agosto de 2026, GitHub cesó formalmente las operaciones y el soporte de nuevas asignaciones en **GitHub Classroom**, amenazando la continuidad operativa del ecosistema de autoevaluación continua y entregas por repositorio para el segundo tramo de la cursada y el inicio del nuevo ciclo lectivo.
- **Modo de Resolución:**
  1. *Evaluación de Impacto en la Arquitectura:* Se verificó que el diseño desacoplado del proyecto (basado en Git nativo, GitHub Actions independientes y agentes orquestados por Model Context Protocol) evitó el *vendor lock-in*. Las plantillas de código, rúbricas y suites de test no dependían intrínsecamente del backend de Classroom.
  2. *Adopción de ClassMoji:* Se seleccionó la plataforma [ClassMoji](file:///c:/Universidad/Agentes%20de%20IA%20y%20Protocolo%20MCP%20para%20evaluaci%C3%B3n%20continua%20y%20autoevaluaci%C3%B3n%20en%20materias%20de%20Ingenier%C3%ADa%20en%20Inform%C3%A1tica%20-%202025/10_bibliografia/fuentes_primarias/Classmoji%20A%20GitHub-Native%20LMS%20for%20Flexible%20CS%20Education.pdf) (Traore & Tregubov, ACM SIGCSE 2026), un LMS de código abierto 100% nativo de GitHub que reproduce el aula sobre organizaciones de GitHub, mapea módulos a repositorios y convierte las entregas en issues que el estudiante cierra al finalizar.
  3. *Migración y Potenciación:* Se migraron los enunciados y plantillas al esquema de ClassMoji, habilitando además dos componentes altamente sinérgicos con el proyecto: el grading cualitativo basado en emojis (reforzando el feedback formativo) y el sistema de tokens para gestión flexible de tiempos (acoplándose naturalmente a la telemetría del Sistema de Puntos de Ritmo).
- **Lección Aprendida:** En el marco de la investigación-acción (Elliott, 1991), los imprevistos externos de infraestructura validan la robustez de las decisiones de diseño. Construir sobre protocolos abiertos (MCP, Git, estándares web) protege a las instituciones educativas frente a la discontinuación imprevista de servicios comerciales en la nube.

