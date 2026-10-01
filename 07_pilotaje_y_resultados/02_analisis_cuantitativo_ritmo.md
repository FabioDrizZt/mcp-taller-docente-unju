# Análisis Cuantitativo Preliminar: El Sistema de Puntos de Ritmo

## 1. El Indicador de Ritmo como Medida de Autorregulación
El **Sistema de Puntos de Ritmo** fue concebido como un indicador cuantitativo objetivo para desincentivar la conducta de procrastinación académica ("dejar todo para la noche previa a la entrega") y premiar la constancia formativa.

### Parámetros de Ponderación:
- **Entrega Temprana / Primer Commit Significativo:** Bonificación de puntos si el alumno registra avance funcional 5 o más días antes de la fecha límite.
- **Ciclo Iterativo de Commits:** Registro de evolución incremental del proyecto (distribución temporal de commits a lo largo de varias jornadas de trabajo).
- **Resolución de Fallos de Autograding:** Frecuencia con la que el estudiante modifica su código tras una corrida fallida de pruebas hasta alcanzar el 100% de éxito.

---

## 2. Hallazgos Cuantitativos Preliminares (Avance 20% del OE3)
A través de la planilla de cálculo de seguimiento de entregas (Excel) durante el primer semestre en *Programación II*, se observaron las siguientes tendencias iniciales:

1. **Aumento en la Constancia de Entregas:** Más del 65% de los estudiantes regulares acumularon puntaje positivo de ritmo, evidenciando un inicio temprano de las tareas.
2. **Reducción de Entregas Vacías o Incompletas:** La disponibilidad del autograding redujo prácticamente a cero la entrega de proyectos con errores fatales de compilación o sintaxis que antes insumían tiempo docente considerable.
3. **Curva de Iteración:** Un promedio de 3 a 5 ciclos de `commit -> push -> autograding -> corrección` por estudiante antes de la entrega final formal en GitHub Classroom.

*Nota:* La consolidación estadística inferencial definitiva (correlación entre Puntos de Ritmo y calificación final en exámenes parciales) se procesará al cierre del ciclo lectivo anual (Julio – Octubre 2026).
