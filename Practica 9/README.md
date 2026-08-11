# 🧠 Práctica 09: Algoritmos de Análisis No Supervisado

## 📋 Información General

| Campo | Detalle |
|---|---|
| **Asignatura** | Extracción de Conocimiento en Bases de Datos |
| **Alumno** | Luis Daniel Suárez Escamilla |
| **Matrícula** | 230040 |
| **Grupo** | 9A - IDGS |
| **Docente** | M.T.I. Marco A. Ramírez Hernández |
| **Periodo** | Mayo – Agosto 2026 |
| **Valor** | 50 Firmas |

---

## 🎯 Objetivo

Replicar, traducir, analizar y documentar el notebook “Unsupervised Learning: 3-6 Clusters | K-Means | EDA”, con la finalidad de aplicar las etapas fundamentales de un proceso de aprendizaje no supervisado para la segmentación de clientes. El estudiante realizará la exploración, limpieza, transformación y normalización del conjunto de datos `Mall_Customers.csv`; aplicará el algoritmo K-Means sobre diferentes combinaciones de variables; determinará el número adecuado de clústeres mediante el método del codo y el coeficiente de silueta; visualizará e interpretará los grupos encontrados y comparará los resultados obtenidos con datos originales y normalizados.

---

## 📁 Estructura del Proyecto

```
Practica09/
├── README.md                               # Este archivo
└── Practica09/
    ├── practica09.ipynb                    # Notebook principal con toda la práctica
    └── Mall_Customers.csv                  # Dataset principal (200 registros)
```

---

## 🛠️ Tecnologías y Librerías Utilizadas

| Librería | Versión | Uso |
|---|---|---|
| **Python** | 3.13.x | Lenguaje base |
| **Pandas** | ≥ 2.0 | Manipulación y análisis de datos |
| **NumPy** | ≥ 1.24 | Operaciones numéricas |
| **Matplotlib** | ≥ 3.7 | Visualizaciones estáticas y gráficas |
| **Seaborn** | ≥ 0.12 | Visualizaciones estadísticas avanzadas |
| **Scikit-learn**| ≥ 1.2 | Modelos de Machine Learning (K-Means, LabelEncoder, StandardScaler) |

---

## 🚀 Cómo Ejecutar

### Prerrequisitos
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### Ejecución
1. Abrir **Jupyter Notebook** o **JupyterLab**
2. Navegar a la carpeta `Practica09/Practica09/`
3. Abrir `practica09.ipynb`
4. Seleccionar **Kernel → Restart & Run All**
5. Observar los resultados de la limpieza, EDA y modelado.

---

## 📊 Dataset

- **Fuente**: [Kaggle - Mall Customer Segmentation Data](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)
- **Registros**: 200 filas.
- **Columnas**: CustomerID, Gender, Age, Annual Income (k$), Spending Score (1-100).
- **Descripción**: Datos de clientes de un supermercado, creados con fines educativos para enseñar conceptos de segmentación.

---

## 📝 Actividades Completadas (50 Firmas)

| # | Actividad | Firmas | Estado |
|---|---|---|---|
| 1 | Portada con datos del estudiante, grupo, fecha, título, y objetivo | 2 | ✅ |
| 2 | Importación de librerías y dependencias necesarias | 2 | ✅ |
| 3 | Carga del dataset y validación de su estructura | 3 | ✅ |
| 4 | Revisión de estructura (tipos de datos, describe, info) | 2 | ✅ |
| 5 | Análisis de calidad de datos (nulos, duplicados, tipos correctos) | 3 | ✅ |
| 6 | Análisis de estadísticas descriptivas con interpretaciones | 3 | ✅ |
| 7 | Análisis exploratorio univariado (Age, Income, Spending Score) | 4 | ✅ |
| 8 | Análisis de valores atípicos mediante boxplots | 3 | ✅ |
| 9 | Análisis bivariado y multivariado (Scatter plots, Pair plot, Mapa de correlación) | 4 | ✅ |
| 10 | Codificación de variable Gender con LabelEncoder | 2 | ✅ |
| 11 | Estandarización de variables numéricas con StandardScaler | 3 | ✅ |
| 12 | Creación de matrices de características con datos originales y estandarizados | 3 | ✅ |
| 13 | Uso del Método del Codo para determinar k óptimo | 3 | ✅ |
| 14 | Uso del Coeficiente de Silueta para confirmar k óptimo | 3 | ✅ |
| 15 | Modelado K-Means (Age + Annual Income) Original y Normalizado | 2 | ✅ |
| 16 | Modelado K-Means (Age + Spending Score) Original y Normalizado | 2 | ✅ |
| 17 | Modelado K-Means (Annual Income + Spending Score) Original y Normalizado | 2 | ✅ |
| 18 | Comparativa gráfica final y definición de perfiles de los clústeres | 2 | ✅ |
| 19 | Redacción de conclusiones finales personales por cada sección clave | 2 | ✅ |
| **TOTAL** | | **50** | ✅ |

---

## 🧠 Hallazgos Principales

1. **El Mejor K-Means**: La mejor segmentación se logró utilizando las variables *Annual Income* y *Spending Score* con **k=5 clústeres**, dando como resultado el mayor Silhouette Score y una agrupación lógica.
2. **Perfiles de Clientes**: 
    - Alto Ingreso / Alto Gasto (Clientes Premium).
    - Alto Ingreso / Bajo Gasto (Clientes Conservadores).
    - Bajo Ingreso / Alto Gasto (Clientes Impulsivos).
    - Bajo Ingreso / Bajo Gasto.
    - Ingreso Medio / Gasto Medio.
3. **Escalamiento de Datos**: La estandarización (Z-score) fue indispensable en combinaciones donde la edad tiene un rango muy bajo (18-70) y el ingreso uno mayor. K-Means es altamente dependiente de las distancias.
4. **Relación Débil de Edad**: La edad no presentó una fuerte correlación con los ingresos ni con el score, lo que indicó que comportamientos como el gasto son independientes de esta variable.

---

*Práctica 09 completada — Luis Daniel Suárez Escamilla — Matrícula 230040 — ECBD 9A-IDGS — Agosto 2026*
