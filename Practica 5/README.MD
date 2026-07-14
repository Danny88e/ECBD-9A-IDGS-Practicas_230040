# PRÁCTICA 05: Generación de Dataset de Pacientes con indicadores para el cálculo de riesgo de Infarto Cardíaco en Puebla

---

## 📋 Información General

| Campo | Detalle |
|---|---|
| **Asignatura** | Extracción de Conocimiento en Bases de Datos |
| **Programa** | Ingeniería en Desarrollo y Gestión de Software |
| **Docente** | M.T.I. Marco A. Ramírez Hernández |
| **Periodo** | Mayo – Agosto 2026 |
| **Alumno** | Luis Daniel Suárez Escamilla |
| **Número de Control** | 230040 |
| **Práctica** | 05 (25 Firmas) |

---

## 🎯 Objetivo General

Generar de manera individual un dataset clínico **simulado** con información de **5,000 pacientes generales del estado de Puebla**. El propósito es construir una base de datos que servirá como punto de partida para prácticas posteriores relacionadas con la clasificación de pacientes, visualización de datos y aplicación de algoritmos de análisis supervisado.

> ⚠️ **Aviso:** Los datos son completamente ficticios y tienen únicamente fines académicos. No se utilizaron datos reales de pacientes ni información personal sensible.

---

## 📁 Estructura del Proyecto

```
Practica 5/
├── data/
│   └── pacientes_puebla.csv       # Dataset simulado con 5,000 registros
├── notebooks/
│   └── Practica05.ipynb           # Notebook con validación, EDA y análisis
├── docs/
│   └── descripcion_dataset.md     # Documentación detallada del dataset
├── src/
│   └── generar_dataset.py         # Script de generación del dataset
├── outputs/
│   └── (gráficas y resultados del EDA)
└── README.md                      # Este archivo
```

---

## 📊 Descripción del Dataset

El dataset `pacientes_puebla.csv` es un archivo simulado con **5,000 registros** de pacientes ficticios del estado de Puebla. Fue generado con el propósito de modelar indicadores clínicos y socioeconómicos para el cálculo de riesgo cardiovascular.

### Contexto
- **Tipo:** Simulado / Académico
- **Registros:** 5,000 pacientes
- **Cobertura Geográfica:** Municipios del estado de Puebla, México
- **Propósito:** Clasificación de riesgo de infarto cardíaco (bajo, medio, alto)

---

## 📑 Atributos del Dataset

| # | Columna | Tipo | Descripción |
|---|---|---|---|
| 1 | `ID_Paciente` | Texto | Identificador único del paciente (PAC_0001 – PAC_5000) |
| 2 | `Municipio` | Texto | Municipio de Puebla donde reside el paciente |
| 3 | `CVE_MUN` | Numérico | Clave INEGI del municipio |
| 4 | `Latitude` | Flotante | Latitud geográfica del municipio |
| 5 | `Longitude` | Flotante | Longitud geográfica del municipio |
| 6 | `Edad` | Entero | Edad del paciente en años (18–90) |
| 7 | `Genero` | Categórico | Género del paciente: `Masculino` / `Femenino` |
| 8 | `Nivel_Socioeconomico` | Categórico | Nivel socioeconómico: `Bajo`, `Medio`, `Alto` |
| 9 | `Acceso_Salud` | Categórico | Tipo de acceso a salud: `IMSS`, `ISSSTE`, `Privado`, `Ninguno` |
| 10 | `Presion_Sistolica` | Entero | Presión arterial sistólica en mmHg (80–200) |
| 11 | `Presion_Diastolica` | Entero | Presión arterial diastólica en mmHg (50–120) |
| 12 | `Colesterol_Total` | Entero | Colesterol total en mg/dL (100–300) |
| 13 | `Glucosa` | Entero | Nivel de glucosa en mg/dL (70–300) |
| 14 | `IMC` | Flotante | Índice de Masa Corporal (15.0–45.0) |
| 15 | `Fumador` | Categórico | Indica si el paciente fuma: `Sí` / `No` |
| 16 | `Historial_Familiar` | Categórico | Antecedentes familiares de infarto: `Sí` / `No` |
| 17 | `Riesgo_Score` | Entero | Puntuación de riesgo calculada (0–100) |
| 18 | `Diagnostico_Infarto` | Entero | Variable objetivo: `1` = Infarto, `0` = Sin infarto |

---

## ⚙️ Reglas de Generación de Datos

| Variable | Rango / Valores Válidos |
|---|---|
| Edad | 18 – 90 años |
| Presión Sistólica | 80 – 200 mmHg |
| Presión Diastólica | 50 – 120 mmHg |
| Colesterol Total | 100 – 300 mg/dL |
| Glucosa | 70 – 300 mg/dL |
| IMC | 15.0 – 45.0 kg/m² |
| Riesgo_Score | 0 – 100 puntos |
| Municipios | Solo municipios del estado de Puebla (INEGI) |
| Coordenadas | Dentro de los límites geográficos de Puebla |

---

## 🎯 Variable Objetivo

El campo `Diagnostico_Infarto` es la variable objetivo binaria:
- `0` → El paciente **no** tuvo diagnóstico de infarto
- `1` → El paciente **sí** tuvo diagnóstico de infarto

El campo `Nivel_Socioeconomico` representa la clasificación de riesgo socioeconómico: `Bajo`, `Medio` o `Alto`.

---

## 🔍 Observaciones de Validación

- ✅ El dataset contiene exactamente **5,000 registros** y **18 columnas**.
- ✅ No se encontraron **valores nulos** en ninguna columna.
- ✅ No existen **registros duplicados** (ID_Paciente únicos).
- ✅ Todos los valores clínicos están dentro de **rangos fisiológicamente válidos**.
- ✅ Las **coordenadas geográficas** corresponden al estado de Puebla.
- ✅ Los **municipios** pertenecen al catálogo oficial de INEGI para Puebla.
- ✅ La distribución del diagnóstico de infarto presenta balance adecuado para análisis supervisado.

---

## 📈 Resumen Estadístico (Variables Numéricas)

| Variable | Media | Mín | Máx | Desv. Estándar |
|---|---|---|---|---|
| Edad | ~54 años | 18 | 90 | ~21 |
| Presión Sistólica | ~140 mmHg | 80 | 200 | ~35 |
| Presión Diastólica | ~85 mmHg | 50 | 120 | ~20 |
| Colesterol Total | ~200 mg/dL | 100 | 300 | ~58 |
| Glucosa | ~185 mg/dL | 70 | 300 | ~66 |
| IMC | ~30 kg/m² | 15 | 45 | ~8.6 |
| Riesgo_Score | ~50 puntos | 0 | 100 | ~29 |

*(Valores aproximados — ver notebook para estadísticas exactas)*

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- **Pandas** — Manipulación y análisis de datos
- **NumPy** — Generación de datos aleatorios
- **Matplotlib / Seaborn** — Visualizaciones EDA
- **Jupyter Notebook** — Entorno de desarrollo
- **GitHub** — Control de versiones

---

## 📌 Commits Progresivos

| Commit | Descripción |
|---|---|
| `Practica 05` | Estructura inicial del proyecto y dataset generado |
| `Verificacion` | Verificación de estructura y primeros análisis |
| *(siguiente)* | Notebook completo con validación, limpieza y EDA |

---

## 📎 Referencias

- INEGI. (2020). *Marco Geoestadístico de Puebla*. Instituto Nacional de Estadística y Geografía.
- Secretaría de Salud. (2023). *Indicadores de salud cardiovascular en México*. SSA.
- Organización Mundial de la Salud. (2021). *Cardiovascular diseases (CVDs)*. OMS.