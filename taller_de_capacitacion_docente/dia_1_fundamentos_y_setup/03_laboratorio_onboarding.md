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

## Paso 2: Ejecución del Agente en el IDE
Para este taller, interactuaremos con el agente directamente desde nuestro Entorno de Desarrollo (IDE).

1. Abre el repositorio del taller en tu IDE configurado con MCP (ej. Antigravity o VSCode).
2. Localiza la ventana de chat o panel del Agente.
3. **Tu primer prompt:** Escribe un saludo simple, por ejemplo:
   > *"Hola, soy [Tu Nombre], docente de la materia. Estoy listo para iniciar el taller."*

## Paso 3: Interacción Guiada (Especificación antes de ejecución)
Vamos a poner a prueba la regla fundamental del taller: el Agente no debe generar un artefacto final sin tu aprobación previa.

1. **Instrucción de diseño:** Pídele al Agente que redacte un `Issue` de bienvenida para los estudiantes de tu cátedra.
   > *"Redacta un Issue de bienvenida para los estudiantes detallando los pasos de esta capacitación. No lo publiques todavía."*

2. **Pausa Obligada (Human-in-the-loop):** 
   - El Agente generará el borrador del texto y deberá **detenerse** para pedirte aprobación (luz verde) antes de ejecutar la acción (publicar el Issue mediante la herramienta MCP de GitHub).
   - *Observación reflexiva:* Nota cómo el sistema respeta tu Agencia Docente. La IA propone, pero tú decides.

3. **Aprobación y Trazabilidad:**
   - Revisa el texto propuesto. Si estás de acuerdo, responde: *"Aprobado, procede a publicarlo."*
   - Una vez publicado, ingresa a tu repositorio en GitHub y verifica que el Issue fue creado correctamente.
   - Observa los registros (logs) del sistema para comprobar qué herramienta ejecutó el agente y qué parámetros utilizó.
