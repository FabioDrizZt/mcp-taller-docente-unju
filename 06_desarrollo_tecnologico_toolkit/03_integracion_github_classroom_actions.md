# Integración con GitHub Classroom, CI/CD, ClassMoji y Automatización de Issues

## 1. Arquitectura de Despliegue Inicial: GitHub Classroom (Fase 1)
Para instrumentalizar la autoevaluación continua sin requerir la instalación de software complejo en las computadoras personales de los alumnos, la fase inicial del proyecto (primer semestre 2026) seleccionó **GitHub Classroom** como plataforma de orquestación.

El ciclo de vida estándar comprendía:
1. El estudiante aceptaba la invitación al assignment mediante un enlace único.
2. Classroom generaba automáticamente un repositorio individual o grupal a partir de una plantilla base (*template repository*).
3. El repositorio incluía configuraciones predefinidas de GitHub Actions (`.github/workflows/`), linters y archivos de configuración base.

---

## 2. El Desafío de los Límites de Cómputo en Repositorios Privados
Durante las primeras semanas de pilotaje surgió una restricción técnica no anticipada:
- **Problema:** Inicialmente se configuraron todos los repositorios de entrega como *privados* para evitar que los alumnos copiaran código de otros compañeros. Sin embargo, GitHub Actions impone un límite estricto de minutos gratuitos mensuales para cuentas educativas en repositorios privados. Al dispararse una acción tras cada commit de decenas de alumnos, la cuota mensual se agotó rápidamente, bloqueando el autograding.
- **Solución Arquitectónica Implementada:**
  - Se modificó la estrategia: las actividades formativas semanales y prácticas de laboratorio operaron sobre **plantillas públicas y repositorios públicos** (donde GitHub Actions ofrece ejecución gratuita e ilimitada para proyectos abiertos).
  - La privacidad se reservó exclusivamente para las instancias de exámenes formales sincrónicos.
  - Como valor pedagógico agregado, el trabajo en repositorios públicos fortaleció la cultura de código abierto, transparencia y portafolio profesional en los estudiantes.

---

## 3. Disparadores Automatizados e Idempotentes: `setup-issues.yml`
- **Problema de Disparo:** Al crearse un repositorio desde Classroom, la acción encargada de sembrar las *issues* formativas iniciales (que actúan como lista de tareas y checklist de autoevaluación) no se ejecutaba de forma confiable sin intervención manual del estudiante (`workflow_dispatch`).
- **Solución Definitiva:** Se desarrolló un flujo en YAML (`setup-issues.yml`) con disparadores asociados al primer `push` y un mecanismo de verificación de idempotencia (comprobación de existencia de issues previas antes de crearlas mediante la GitHub CLI / API), garantizando que todo repositorio nuevo cuente con sus tareas formativas listas desde el primer segundo sin duplicaciones accidentales.

---

## 4. Pivote Arquitectónico: Cierre de GitHub Classroom y Transición a ClassMoji (Fase 2)
El 28 de agosto de 2026, GitHub Classroom suspendió definitivamente sus operaciones y soporte para nuevas asignaciones, lo que representó una contingencia externa de máxima criticidad para el proyecto de investigación.

### 4.1 Análisis de Alternativas y Decisión
Frente a la contingencia, se evaluaron tres caminos posibles:
1. *Regresión a LMS tradicional (Moodle/Campus Virtual):* Descartada por romper el paradigma de autoevaluación continua mediante commits y exigir entregas de archivos estáticos ZIP, desarticulando los objetivos de investigación.
2. *Automatización manual mediante scripts de GitHub API:* Descartada por sobrecarga operativa y dificultad de mantenimiento para los docentes no desarrolladores del proyecto.
3. *Adopción de ClassMoji (Traore & Tregubov, 2026):* Seleccionada como la **solución óptima y definitiva**. 

### 4.2 Arquitectura y Mapeo en ClassMoji
[ClassMoji](file:///c:/Universidad/Agentes%20de%20IA%20y%20Protocolo%20MCP%20para%20evaluaci%C3%B3n%20continua%20y%20autoevaluaci%C3%B3n%20en%20materias%20de%20Ingenier%C3%ADa%20en%20Inform%C3%A1tica%20-%202025/10_bibliografia/fuentes_primarias/Classmoji%20A%20GitHub-Native%20LMS%20for%20Flexible%20CS%20Education.pdf) es un LMS nativo de GitHub presentado en ACM SIGCSE 2026 que traduce la infraestructura pedagógica a primitivas nativas de Git:
- **Organización de GitHub:** Funciona como el aula institucional (*Classroom*).
- **Repositorios de GitHub:** Representan los módulos de la materia (e.g. `Frontend-Estatico`, `React-SPA`, `Backend-Node`).
- **GitHub Issues:** Representan las tareas o trabajos prácticos individuales. La acción de cerrar el issue (`Close issue`) actúa como el sello temporal de entrega oficial por parte del estudiante.

```text
┌─────────────────────────────────────────────────────────────────┐
│                     Plataforma ClassMoji                        │
│            (LMS Nativo sobre API y Webhooks de GitHub)          │
└───────────────┬───────────────────────────────┬─────────────────┘
                │                               │
                ▼                               ▼
  ┌───────────────────────────┐   ┌───────────────────────────┐
  │   Gestión de Repositorios │   │   Sistema de Evaluación   │
  │ • Forks desde templates   │   │ • Emojis Cualitativos     │
  │ • Issues como TPs         │   │   (Feedback Formativo)    │
  │ • Cierre de issue = Subm. │   │ • Tokens de Tiempo        │
  └─────────────┬─────────────┘   │   (Puntos de Ritmo)       │
                │                 └───────────────────────────┘
                ▼
  ┌───────────────────────────────────────────────────────────┐
  │                   Infraestructura GitHub                  │
  │  • GitHub Actions (Linters, Vitest, Clang-format, MCP)   │
  │  • Repositorios Públicos Educativos                       │
  └───────────────────────────────────────────────────────────┘
```

### 4.3 Sinergia con los "Puntos de Ritmo" y la Evaluación Formativa
La integración de ClassMoji no solo resolvió la discontinuación de Classroom sino que potenció los pilares pedagógicos de la investigación:
1. **Economía de Tokens y Puntos de Ritmo:** ClassMoji introduce un sistema de tokens donde el estudiante puede solicitar prórrogas flexibles sin necesidad de justificación burocrática, sincronizándose de manera exacta con el modelo de autorregulación (Zimmerman, 2002) y la telemetría de Puntos de Ritmo de la cátedra.
2. **Evaluación basada en Emojis (Alternative Grading):** Permite categorizar cualitativamente el estado del código mediante símbolos expresivos asociados a criterios de rúbrica, reduciendo la ansiedad por la nota numérica y priorizando el feedback formativo de mejora iterativa (Nicol & Macfarlane-Dick, 2006).
3. **Preservación del Andamiaje MCP:** Dado que ClassMoji opera sobre repositorios estándar de GitHub, todos los flujos de GitHub Actions, linters (`Configuration-Files`) y servidores evaluadores MCP desarrollados durante la primera fase se mantuvieron 100% compatibles sin requerir reescritura.
