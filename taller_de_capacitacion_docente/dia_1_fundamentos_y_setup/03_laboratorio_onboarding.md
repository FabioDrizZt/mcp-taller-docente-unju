# Laboratorio 1: Onboarding y Primer Contacto

## Objetivo
Configurar el entorno de trabajo y experimentar la metodología *Human-in-the-loop* mediante una interacción inicial con el Agente de IA. En este laboratorio veremos una primera aproximación práctica a lo que más adelante llamaremos SDD (Desarrollo Guiado por Especificaciones) y protegeremos el principio de Agencia Docente.

## Paso 1: Configuración de la Identidad Docente
Antes de interactuar con el agente, es necesario establecer la identidad digital que nos permitirá conectarnos a las plataformas educativas (GitHub y ClassMoji).

1. **Verificación de cuenta de GitHub:**
   - Si no posees una cuenta, regístrate en [github.com](https://github.com).
   - *Recomendación:* Utiliza tu correo institucional para acceder a los beneficios educativos de GitHub.

2. **Ingreso a la organización ClassMoji:**
   - Acepta la invitación enviada a tu correo o accede a través del enlace provisto por el equipo coordinador.
   - Vincula tu cuenta de GitHub con la plataforma ClassMoji para habilitar la trazabilidad de tus interacciones.

## Paso 2: Clonación de la Plantilla Autoevaluativa
Para este taller, interactuaremos con el agente directamente desde nuestro Entorno de Desarrollo (IDE). Hemos preparado una **Plantilla Base** que simula cómo interactuarán tus alumnos con tus Trabajos Prácticos.

1. Ingresa al repositorio de la plantilla del taller provista por la cátedra.
2. Realiza un **Fork** hacia tu cuenta de GitHub y clónalo en tu computadora.
3. Abre la carpeta clonada (`plantilla-taller-docente-mcp`) en tu IDE configurado con MCP (ej. Antigravity, Cursor o VSCode).

## Paso 3: Interacción Guiada (Setup del Día 1)
Vamos a poner a prueba al Agente delegándole la construcción de la estructura base de tu materia. No lo harás a mano; le darás las instrucciones al Agente.

1. Abre el chat de tu Agente en el IDE.
2. **Tu primer prompt (Estructuración):** 
   > *"Actúa como mi asistente docente. Basándote en mi materia [Nombre de tu materia], créame el archivo `AGENTS.md`, `MEMORY.md`, `planificacion.md` y la carpeta `/bibliografia` con al menos un archivo de referencia en formato markdown dentro de ella."*
3. **Pausa Obligada (Human-in-the-loop):** 
   - El Agente propondrá el contenido de los archivos y deberá pedirte **aprobación** antes de crearlos en el disco. Revisa la propuesta y dale luz verde.
4. **Validación (Autograding):**
   - Una vez que la IA haya creado los archivos, abre una terminal y haz un commit y push de tus cambios a GitHub:
     `git add . && git commit -m "feat: estructura base dia 1" && git push`
   - Ve a la pestaña **Actions** en tu repositorio de GitHub. Verás cómo el script `autograder_taller.py` evalúa tu avance y te otorga los primeros 50 puntos del taller.
   - *Observación reflexiva:* Nota cómo el sistema respeta tu Agencia Docente. La IA propone, pero tú decides.

3. **Aprobación y Trazabilidad:**
   - Revisa el texto propuesto. Si estás de acuerdo, responde: *"Aprobado, procede a publicarlo."*
   - Una vez publicado, ingresa a tu repositorio en GitHub y verifica que el Issue fue creado correctamente.
   - Observa los registros (logs) del sistema para comprobar qué herramienta ejecutó el agente y qué parámetros utilizó.
