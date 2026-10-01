# Unidad 8: Anatomía Práctica de una Skill Docente

## 1. De la Teoría a la Herramienta (El Salto Cualitativo)
Durante el Día 1 observamos que los prompts breves y sin contexto (Zero-Shot) suelen resultar insuficientes para tareas docentes complejas: pueden omitir requisitos, producir respuestas inconsistentes y aumentar el trabajo de revisión.

En esta unidad, dejaremos de escribir "prompts" y comenzaremos a diseñar y construir **Skills** (Habilidades). 

> **Definición Clave:** Una *Skill* no es solamente un mensaje de chat. Es un artefacto de instrucciones estructuradas y versionables que encapsula criterios, procedimientos y restricciones para su reutilización sistemática por un agente.

## 2. Los Componentes Críticos (Recuperando el Toolkit)
Si abren el artefacto `03_plantilla_skill.md` de su *Toolkit Docente* (o interactúan con el Widget 4 de Anatomía de Skills), verán que en nuestro Toolkit utilizaremos una estructura de 9 bloques. Aunque la implementación puede variar entre plataformas, esta plantilla asegura que no omitamos componentes importantes. Hoy nos centraremos en los tres fundamentales:

### A. El YAML Frontmatter (El Documento de Identidad)
Toda Skill profesional comienza con un bloque de metadatos en la parte superior. Esto le dice al Agente y al IDE cómo debe indexar y presentar esta herramienta.

```yaml
---
name: Evaluador_Maquetacion_Frontend
description: Asistente para pre-evaluar exámenes de HTML/CSS sin dar código resuelto.
version: 2.1.0
---
```

### B. Restricciones Críticas (Safety Rails)
El bloque más importante de tu Skill no es decirle a la IA qué hacer, sino **qué NO hacer bajo ninguna circunstancia**. Inspirándonos en la Skill oficial de Sistemas Operativos (TSO), conviene clasificar estas restricciones para que el Agente comprenda la naturaleza del límite:

> **Restricciones (CRÍTICO):**
> 
> **Restricciones Pedagógicas:**
> - **NUNCA** proporciones el código fuente corregido. Tu rol es formativo.
> - Formula pistas progresivas (Método Socrático).
> 
> **Restricciones Técnicas:**
> - Si detectas que el alumno utilizó librerías prohibidas en el contexto (ej. Tailwind cuando se pedía CSS puro), detén la corrección inmediatamente.
> 
> **Restricciones de Salida:**
> - **PROHIBIDO** utilizar negritas en la generación de opciones múltiples.
> - Utiliza estrictamente la plantilla Markdown definida en el 'Formato de Salida'.
### C. Manejo de Incertidumbre
¿Qué pasa si la entrega del alumno está corrupta o incompleta? Sin instrucciones explícitas, un modelo podría intentar completar la tarea aun cuando falten evidencias suficientes, produciendo una valoración injustificada. Una Skill docente debe tener directivas claras de aborto:

> **Incertidumbre:** Si no encuentras el archivo `index.html` en la carpeta indicada mediante el MCP, responde exclusivamente: *"Error: Estructura de entrega inválida"* y detén la evaluación.

## 3. Dinámica de la Unidad
1. Abran su *Toolkit* y seleccionen un problema repetitivo de su propia materia (ej. corregir informes de laboratorio, generar casos de prueba, evaluar código SQL).
2. Tienen 15 minutos para completar un primer borrador centrado en propósito, entradas esperadas, restricciones y manejo de incertidumbre. El resto de los bloques podrá refinarse durante el laboratorio integrador.
3. Compartiremos las *Restricciones* más creativas y necesarias que hayan diseñado para sus alumnos.
