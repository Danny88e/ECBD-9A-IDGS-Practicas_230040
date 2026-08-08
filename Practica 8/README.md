# 🎮 Práctica 08: 3D Scatter Plot con Sprites de Pokémons

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

Construir un **Scatter Plot 3D interactivo** con Plotly que visualice las estadísticas de los Pokémon distribuidas por generación y tipo principal, integrando los **sprites oficiales** de cada Pokémon como elementos visuales en el tooltip, aplicando filtros interactivos por tipo y generación, y exportando la visualización final en formato HTML conservando toda su interactividad.

---

## 📁 Estructura del Proyecto

```
Practica 8/
├── Practica08.ipynb                        # Notebook principal con toda la práctica
├── pokemon_scatter3d_sprites.html          # Visualización 3D interactiva (sprites embebidos en Base64)
├── README.md                               # Este archivo
└── Repositorio Dataset de Pokemones/
    ├── Pokemon.csv                         # Dataset principal (1,216 registros)
    ├── Pokemon Images/                     # Dataset de imágenes locales para la visualización
    ├── Pokemon.xlsx
    ├── gen01.csv ... gen09.csv             # Datasets por generación
    ├── PokemonData.zip
    └── README.md
```

---

## 🛠️ Tecnologías y Librerías Utilizadas

| Librería | Versión | Uso |
|---|---|---|
| **Python** | 3.13.x | Lenguaje base |
| **Pandas** | ≥ 2.0 | Manipulación y análisis de datos |
| **NumPy** | ≥ 1.24 | Operaciones numéricas |
| **Plotly** | ≥ 5.15 | Visualizaciones interactivas 3D |
| **Plotly Express** | ≥ 5.15 | API de alto nivel para gráficas |

---

## 🚀 Cómo Ejecutar

### Prerrequisitos
```bash
pip install pandas numpy plotly openpyxl
```

### Ejecución
1. Abrir **Jupyter Notebook** o **JupyterLab**
2. Navegar a la carpeta `Practica 8/`
3. Abrir `Practica08.ipynb`
4. Seleccionar **Kernel → Restart & Run All**
5. La visualización HTML se generará como `pokemon_scatter3d_sprites.html`

---

## 📊 Dataset

- **Fuente**: `Pokemon.csv` del repositorio interno del curso (origen: Kaggle - *"The Complete Pokemon Dataset"* por Rounak Banik)
- **Registros**: 1,216 filas (incluye formas alternativas y Mega Evoluciones)
- **Columnas**: ID, Name, Form, Type1, Type2, Total, HP, Attack, Defense, Sp. Atk, Sp. Def, Speed, Generation
- **Generaciones**: 1 a 9

---

## 📝 Actividades Completadas (50 Firmas)

| # | Actividad | Firmas | Estado |
|---|---|---|---|
| 1 | Portada con datos del estudiante, grupo, fecha, título y objetivo | 2 | ✅ |
| 2 | Importación de librerías (Pandas, NumPy, Plotly) | 2 | ✅ |
| 3 | Carga del dataset con descripción de origen y contenido | 3 | ✅ |
| 4 | Inspección inicial: head(), shape, info(), describe() | 2 | ✅ |
| 5 | Limpieza y normalización de columnas y tipos | 3 | ✅ |
| 6 | Tratamiento de nulos, duplicados e incorrectos (antes/después) | 2 | ✅ |
| 7 | Selección y justificación de variables estadísticas | 3 | ✅ |
| 8 | Creación de columna `promedio_estadisticas` | 2 | ✅ |
| 9 | Análisis estadístico descriptivo (media, mediana, min, max, std) | 4 | ✅ |
| 10 | Preparación de variables de generación y tipo | 3 | ✅ |
| 11 | Obtención y validación de URLs de sprites (PokeAPI CDN) | 2 | ✅ |
| 12 | Primera versión del Scatter Plot 3D interactivo | 3 | ✅ |
| 13 | Diferenciación visual por tipo principal (colores) | 3 | ✅ |
| 14 | Configuración de hover: nombre, tipo, generación, promedio | 2 | ✅ |
| 15 | Integración de sprites en el hover tooltip | 3 | ✅ |
| 16 | Filtros interactivos por generación y tipo | 2 | ✅ |
| 17 | Personalización: título, ejes, leyenda, cámara, opacidad | 3 | ✅ |
| 18 | Identificación de patrones, agrupaciones y outliers (≥ 3 hallazgos) | 2 | ✅ |
| 19 | Exportación a HTML con funciones interactivas conservadas | 2 | ✅ |
| 20 | Conclusiones finales + notebook ordenado sin errores | 2 | ✅ |
| **TOTAL** | | **50** | ✅ |

---

## 🗺️ Visualización 3D

La gráfica interactiva presenta:

- **Eje X**: Generación (1–9)
- **Eje Y**: Tipo principal del Pokémon (18 tipos)
- **Eje Z**: Promedio de estadísticas (HP, Ataque, Defensa, Atk. Especial, Def. Especial, Velocidad)
- **Color**: Diferenciado por tipo principal (paleta de colores oficial)
- **Hover**: Sprite del Pokémon + nombre, tipo, generación y promedio
- **Filtros**: Botones interactivos por generación + leyenda clicable por tipo
- **Funciones**: Rotación 3D, zoom, desplazamiento, exportar imagen

---

## 🧠 Hallazgos Principales

1. **Outliers Legendarios**: Pokémon como Mewtwo, Arceus y Rayquaza superan en 2+ σ el promedio global (~72 pts), con promedios > 120 puntos.

2. **Tipos más poderosos**: Dragon, Psychic y Steel presentan los promedios estadísticos más altos consistentemente en todas las generaciones.

3. **Tendencia creciente**: Las generaciones más recientes muestran mayor dispersión estadística (mayor varianza en eje Z), introduciendo tanto Pokémon muy poderosos como muy débiles.

4. **Bug y Normal**: A pesar de ser los tipos con más representantes, son los que presentan los promedios estadísticos más bajos.

---

## 🖼️ Sprites

Los sprites se obtienen de la **PokeAPI CDN** de forma dinámica:

```
https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png
```

Se construye la URL en base al ID de la Pokédex Nacional de cada Pokémon. Los sprites se muestran en el tooltip al hacer hover sobre cada punto de la gráfica.

---

## 📤 Exportación HTML

El archivo `pokemon_scatter3d_sprites.html` se genera al ejecutar la celda de exportación. Este archivo:
- Es **autocontenido** (incrusta sprites locales en Base64)
- Pesa aproximadamente **1.5 MB**
- Funciona en cualquier navegador moderno sin instalación adicional
- Conserva todas las funciones interactivas: rotación 3D, zoom, hover, filtros y exportación de imagen

---

*Práctica 08 completada — Luis Daniel Suárez Escamilla — Matrícula 230040 — ECBD 9A-IDGS — Agosto 2026*
