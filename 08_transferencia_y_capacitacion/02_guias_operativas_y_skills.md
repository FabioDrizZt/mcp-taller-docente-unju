# Guías Operativas, Andamiaje Técnico y Ecosistema de Skills Reutilizables

Como productos tangibles de transferencia generados durante el desarrollo del proyecto, se construyeron artefactos de andamiaje, documentos operativos y módulos de instrucciones estandarizados para su adopción inmediata por parte de los docentes:

---

## 1. Paquete Universal de Andamiaje Técnico (`Configuration-Files`)
Para que las distintas materias puedan adoptar la evaluación continua sin lidiar con fricciones de configuración inicial, se consolidó un repositorio y paquete de *scaffolding*:
- **Herramientas Estandarizadas:** Archivos preconfigurados de `.editorconfig` (normalización de saltos de línea y tabulación), `.prettierrc` (formateo automático de código), `.stylelintrc` (ordenamiento y especificidad CSS), `tsconfig.json` (chequeo estático de tipos) y `vite.config.js` (bundling rápido y runner de tests).
- **Mecanismo de Transferencia:** El docente solo debe clonar o vincular estos archivos a la plantilla de su módulo en GitHub/ClassMoji, garantizando que los alumnos cuenten con retroalimentación inmediata desde el primer día de cursada.

---

## 2. Guías Arquitectónicas y Operativas
- **`instructions_frontend_estatico.md`:**
  - Guía orientada a estudiantes y docentes de desarrollo web inicial.
  - Detalla la convención de carpetas, requisitos de HTML semántico, estructuración de hojas de estilo CSS modular, principios de diseño responsivo y pautas de accesibilidad auditadas por el evaluador headless.
- **`instructions_backend.md`:**
  - Pautas para la construcción de servicios RESTful en Node.js/Express, arquitectura por capas (controladores, rutas, servicios, repositorios), validación de variables de entorno y ejecución de pruebas de integración con Supertest/Vitest.
- **Guía de Migración a ClassMoji:**
  - Manual paso a paso para configurar organizaciones educativas en GitHub, vincular el listado de alumnos mediante CSV, publicar módulos formativos y gestionar la economía de tokens para entregas flexibles.

---

## 3. Ecosistema de Skills de IA para Docentes (Antigravity / Claude)
En el marco de la extensibilidad con agentes inteligentes asistidos por MCP:
1. **Generación Curricular SDD (Spec-Driven Development):**
   - `ayp-examenes-sdd`: Generador integral de exámenes con especificaciones rigurosas para Módulo 2.
   - `ayp-examenes-m3-sdd` y `ayp-examenes-m4-sdd`: Generadores de exámenes de 3 temas paralelos en C++ (arreglos unidimensionales, ordenamiento, búsqueda y registros estructurados) con 100% de código y suites de pruebas asociadas.
2. **Generación Psicométrica de Contenidos:**
   - `ayp-clases-quizizz`: Asistente para la elaboración de clases teóricas interactivas y cuestionarios de autoevaluación psicométrica libres de sesgo cultural o lingüístico.
3. **Evaluadores MCP Especializados:**
   - Evaluador estático de sintaxis y arquitectura DOM/CSS.
   - Evaluador de código C++ con chequeo de desbordamientos de memoria y paso de referencias.

---

## 4. Impacto Institucional en la Transferencia
La disponibilidad de este kit integrado reduce drásticamente la barrera de entrada técnica: un docente no especialista en IA o DevOps puede desplegar un módulo de autoevaluación continua en su cátedra en menos de una hora, garantizando rigor pedagógico y soberanía sobre sus criterios de corrección.
