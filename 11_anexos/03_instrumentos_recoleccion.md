# Anexo 3: Modelos de Instrumentos de Recolección y Consentimiento

## 1. Modelo de Consentimiento Informado Estudiantil
```text
UNIVERSIDAD CATÓLICA DE SANTIAGO DEL ESTERO - DEPARTAMENTO ACADÉMICO SAN SALVADOR
PROSECRETARÍA DE INVESTIGACIÓN - PROYECTO CONVOCATORIA DASS 2025
"Agentes de IA y Protocolo MCP para evaluación continua y autoevaluación en materias de Ingeniería en Informática"

FORMULARIO DE CONSENTIMIENTO INFORMADO
Yo, _______________________________________, DNI __________________________, estudiante de la asignatura ___________________________, declaro haber sido informado/a sobre los propósitos del proyecto de investigación arriba mencionado.

Comprendo que:
1. El uso de las herramientas de autograding y retroalimentación con agentes de IA es una actividad pedagógica regular orientada a mejorar mi aprendizaje.
2. Mis métricas operativas (fechas de commits, respuestas a cuestionarios) serán analizadas de forma estrictamente anónima y agregada para publicaciones científicas.
3. Mi consentimiento es voluntario y no incidirá en mis calificaciones ni condición de regularidad.

Firma: ___________________________    Fecha: ____/____/2026
```

---

## 2. Estructura de la Planilla Excel del Sistema de Puntos de Ritmo

| Columna | Nombre del Campo | Descripción |
| :---: | :--- | :--- |
| **A** | `ID_Alumno` | Código anónimo (e.g. `EST_P2_01`) |
| **B** | `Comision` | Regular / Recursante |
| **C** | `TP_Numero` | Identificador de la actividad |
| **D** | `Fecha_Asignacion` | Fecha de publicación del assignment |
| **E** | `Fecha_Primer_Commit` | Fecha y hora del primer push registrado |
| **F** | `Fecha_Deadline` | Límite formal de entrega |
| **G** | `Dias_Anticipacion` | `Fecha_Deadline - Fecha_Primer_Commit` |
| **H** | `Total_Commits` | Cantidad total de commits en la rama |
| **I** | `Reintentos_Autograding` | Veces que corrió el test suite |
| **J** | `Puntos_Ritmo` | Puntaje calculado (escala 0 a 100) |
| **K** | `Nota_Cualitativa_PR` | Evaluación docente del código final |
