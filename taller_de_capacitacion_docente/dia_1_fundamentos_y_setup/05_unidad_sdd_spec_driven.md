# Unidad 4: Metodología SDD (Spec-Driven Development) y Diseño Inverso

## El Peligro de la Generación Directa sin Especificación
Un error frecuente al utilizar IA generativa es pedirle que genere un trabajo práctico, examen o proyecto completo en una única etapa, sin explicitar primero los objetivos, contenidos, restricciones, dificultad y criterios de aceptación. Frecuentemente, esta generación directa (flujo *prompt-to-output* sin validación intermedia) resulta en actividades desbalanceadas o consignas ambiguas que obligan a rehacer todo de cero. Aunque en ingeniería de prompts podamos usar técnicas como *zero-shot* (solicitar una tarea sin proveer ejemplos previos), ceder el control total del diseño a la máquina en un solo paso atenta contra la **Agencia Docente**, un principio fundamental defendido por la **UNESCO (2023)** sobre el uso de IA en educación.

## SDD: Especificación antes que Implementación
En las experiencias desarrolladas para diseñar este taller, la adopción de un flujo inspirado en el **Spec-Driven Development (SDD)** permitió separar la definición pedagógica de la generación de materiales.
En este taller utilizamos una **adaptación didáctica** de SDD. En el desarrollo de software, la especificación describe los requisitos, restricciones, comportamientos esperados y criterios de aceptación de un producto o sistema. En esta adaptación didáctica, la especificación describe además los objetivos, contenidos, evidencias y criterios pedagógicos del recurso educativo.
En el flujo propuesto para el taller, la *Skill* instruye al Agente para que no genere la evaluación ni el código final antes de producir una especificación y recibir la aprobación explícita del docente.
**Fundamento Pedagógico:** El flujo SDD guarda una analogía útil con el **Diseño Inverso (Backward Design de Wiggins & McTighe, 2005)**: ambos procuran definir primero los resultados esperados y los criterios de calidad antes de construir las actividades o artefactos finales. En lugar de generar las actividades al azar, se fuerza a definir primero las metas:
1. **Fase de Especificación:** El Agente redacta un documento formal (`SDD.md`). Lejos de ser un simple punteo, una especificación didáctica robusta debe contener:
   - **Contexto:** Materia, año, unidad y conocimientos previos.
   - **Resultados de aprendizaje:** Qué deberá demostrar el estudiante.
   - **Contenidos habilitados:** Qué conceptos fueron enseñados y pueden utilizarse.
   - **Contenidos excluidos:** Qué recursos todavía *no* deben aparecer (vital para evitar evaluar temas futuros).
   - **Tipo de actividad:** Práctica, formativa, sumativa o diagnóstica.
   - **Evidencias esperadas:** Qué producción demostrará el aprendizaje.
   - **Restricciones:** Tiempo, lenguaje, bibliotecas, entorno y modalidad.
   - **Nivel de dificultad:** Complejidad conceptual y técnica esperada.
   - **Variantes:** Qué puede cambiar sin alterar la equivalencia temática.
   - **Criterios de evaluación:** Rúbrica y ponderaciones.
   - **Criterios de aceptación:** Condiciones verificables que debe cumplir el material generado.
   - **Casos límite:** Errores previsibles, ambigüedades y situaciones excepcionales.
   - **Artefactos finales:** Consigna, solución docente, pruebas, rúbrica y guía de devolución.
2. **Fase de Validación:** El Agente se detiene y pide "Luz verde" (aprobación humana), preservando la Agencia Docente (Human-in-the-loop).
3. **Fase de Generación:** Solo tras el ajuste y revisión humana de la especificación, la IA procede a construir los artefactos finales.

## 💡 El Impacto en el Aula (Ejemplo: Algoritmos y Programación - UCSE)
En las primeras pruebas realizadas para *Algoritmos y Programación (C++)*, la generación directa de enunciados produjo resultados inadecuados, porque la IA introducía con frecuencia el uso de arreglos o funciones antes de que esos contenidos fueran enseñados.
Al adoptar un enfoque guiado por especificaciones (SDD), el flujo reduce la generación prematura y facilita que el docente detecte desbalances antes de producir todo el paquete. Por ejemplo, al solicitar una evaluación para el Módulo 3 con 3 variantes temáticas (A, B y C), el Agente debe proponer primero una **matriz de equivalencia** que detalle:
- Contenidos evaluados.
- Cantidad de decisiones algorítmicas.
- Niveles cognitivos.
- Casos límite y dificultad de las pruebas.
- Tiempo estimado de resolución.

**Resultado:** La revisión humana de esta matriz conserva la responsabilidad académica y permite corregir objetivos y criterios antes de la implementación. Una vez que el docente aprueba la especificación, el Agente procede a generar el paquete de artefactos: código fuente, rúbricas y pruebas de escritorio.
