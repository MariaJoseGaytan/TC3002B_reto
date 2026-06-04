# Python Code Plagiarism Detector

Proyecto de Machine Learning enfocado en la detección automatizada de plagio académico en entregas de código Python. El sistema utiliza análisis estructural mediante Árboles de Sintaxis Abstracta (AST) y Feature Engineering para evitar ser engañado por tácticas comunes de ofuscación como el renombramiento de variables o el movimiento de funciones.

---

## Objetivo del Proyecto

El objetivo principal de este proyecto es construir un modelo de clasificación binaria capaz de determinar si dos archivos de código fuente de Python son sospechosamente similares (plagio) o son lógicamente independientes. 

A diferencia de los comparadores de texto tradicionales que fallan cuando un estudiante cambia el nombre de las variables o agrega espacios, este enfoque evalúa la **arquitectura lógica y estructural** del código, haciendo que sea casi imposible ocultar el plagio.

---

## Dataset Utilizado

**Dataset utilizado:**
- [Student Code Similarity & Plagiarism Labels (Kaggle)](https://www.kaggle.com/datasets/ehsankhani/student-code-similarity-and-plagiarism-labels)

Este dataset contiene:
- Un directorio con múltiples archivos `.py` en bruto que simulan entregas de estudiantes.
- Un archivo `cheating_dataset.csv` con pares etiquetados indicando si hubo trampa (`1`) o no (`0`).

---

## Limpieza y Preparación de Datos (AST Parsing)

Antes de entrenar cualquier modelo, fue necesario normalizar el código fuente. Para lograrlo, implementamos un pipeline nativo utilizando la librería `ast` de Python.

**Proceso de normalización:**
1. **Ignorado nativo de comentarios:** Al parsear el código directamente a AST, los comentarios y espacios en blanco se eliminan automáticamente de la estructura lógica.
2. **Eliminación de Docstrings:** Se programó un recolector que elimina nodos `Constant` de tipo string aislados.
3. **Anonimización de Variables y Funciones:** Mediante la clase `ast.NodeTransformer`, se recorrió el árbol para reemplazar todos los identificadores creados por el usuario (nombres de variables y funciones) por identificadores secuenciales estándar (`var_1`, `var_2`, `func_1`).

**Resultado:**
Se generó un dataset intermedio (`ast_dataset.csv`) donde cada fila contiene un par de archivos y sus representaciones estructurales anónimas en formato de string aplanado.

---

##  Feature Engineering

Dado que los algoritmos de Machine Learning requieren entradas numéricas, el núcleo analítico de este proyecto fue la extracción de métricas matemáticas que comparen las dos cadenas AST de cada par. 

Se extrajeron dos grupos de métricas:

### 1. Features Base (Métricas Generales)
| Feature | Descripción Técnica |
|---|---|
| `length_ratio` | Proporción entre el tamaño del AST más corto y el más largo. |
| `seq_similarity` | Ratio del algoritmo Gestalt Pattern Matching (`difflib`). Evalúa qué tanto se conserva la topología secuencial bloque por bloque. |
| `cosine_similarity` | Similitud del coseno aplicada sobre una vectorización TF-IDF (1-3 n-gramas) de las estructuras del AST. Evalúa proporciones lógicas independientes del tamaño. |

### 2. Features Avanzadas (Métricas Estructurales Específicas)
| Feature | Descripción Técnica |
|---|---|
| `jaccard_similarity` | Intersección sobre Unión (IoU) de los **tipos** de nodos utilizados. Determina si ambos códigos usan la misma "variedad" de herramientas (ej. ambos usan While, ListComp, Dict). |
| `depth_difference` | Diferencia absoluta en la profundidad máxima de anidación del árbol lógico (ej. bucles dentro de if dentro de funciones). |


**Archivos Generados:**
> El proceso culminó con la creación del dataset final listo para modelado: `fixed_dataset.csv`.

---

## Variable Objetivo

La variable a predecir (`Label`) representa el *ground truth* del dataset original:

| Valor | Significado |
|:---:|---|
| **1** | Plagio Detectado (Trampa) |
| **0** | Código Original (Sin trampa) |

---

# Autores
María José Gaytán Gil A01706616

Maxime Vilcocq Parra A01710550

Salvador Rodríguez Paredes A01704562
