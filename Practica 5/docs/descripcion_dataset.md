# Descripción Detallada del Dataset — Práctica 05

## Nombre del Dataset
`pacientes_puebla.csv`

## Contexto
Dataset clínico **simulado y académico** que representa 5,000 pacientes ficticios del estado de Puebla, México. No contiene información real ni datos personales sensibles. Fue creado con el propósito de servir como base para prácticas de clasificación de riesgo cardiovascular.

## Atributos y Reglas de Generación

| Atributo | Tipo | Rango / Valores | Descripción |
|---|---|---|---|
| ID_Paciente | String | PAC_0001–PAC_5000 | Identificador único |
| Municipio | String | Municipios INEGI Puebla | Municipio de residencia |
| CVE_MUN | Integer | Claves INEGI | Clave del municipio |
| Latitude | Float | 17.8° – 21.0° N | Latitud dentro de Puebla |
| Longitude | Float | -99.0° – -96.7° O | Longitud dentro de Puebla |
| Edad | Integer | 18 – 90 | Años del paciente |
| Genero | Category | Masculino, Femenino | Género biológico |
| Nivel_Socioeconomico | Category | Bajo, Medio, Alto | Nivel NSE |
| Acceso_Salud | Category | IMSS, ISSSTE, Privado, Ninguno | Servicio médico |
| Presion_Sistolica | Integer | 80 – 200 mmHg | PA sistólica |
| Presion_Diastolica | Integer | 50 – 120 mmHg | PA diastólica |
| Colesterol_Total | Integer | 100 – 300 mg/dL | Colesterol total |
| Glucosa | Integer | 70 – 300 mg/dL | Glucosa en sangre |
| IMC | Float | 15.0 – 45.0 kg/m² | Índice de Masa Corporal |
| Fumador | Category | Sí, No | Hábito de fumar |
| Historial_Familiar | Category | Sí, No | Antecedentes familiares |
| Riesgo_Score | Integer | 0 – 100 | Puntuación de riesgo calculada |
| Diagnostico_Infarto | Integer | 0, 1 | Variable objetivo binaria |

## Criterio de Variable Objetivo
- `Riesgo_Score > 50` → `Diagnostico_Infarto = 1` (riesgo de infarto)
- `Riesgo_Score ≤ 50` → `Diagnostico_Infarto = 0` (sin riesgo de infarto)
