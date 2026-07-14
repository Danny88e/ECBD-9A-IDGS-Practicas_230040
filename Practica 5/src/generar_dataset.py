#!/usr/bin/env python3
"""
Script de generacion del dataset de pacientes de Puebla.
Referencia para documentar el proceso de creacion en src/.
"""
import pandas as pd
import numpy as np
import random

# Semilla para reproducibilidad
np.random.seed(42)
random.seed(42)

# Municipios de Puebla (muestra representativa)
municipios = [
    ("Puebla", 114, 19.043, -98.198),
    ("Tehuacan", 156, 18.461, -97.392),
    ("San Martin Texmelucan", 132, 19.283, -98.433),
    ("Atlixco", 19, 18.908, -98.438),
    ("San Pedro Cholula", 140, 19.064, -98.308),
    ("Acatzingo", 2, 18.978, -97.781),
    ("Amozoc", 15, 19.046, -98.048),
    ("Izucar de Matamoros", 79, 18.598, -98.467),
    ("Chignahuapan", 39, 19.840, -98.028),
    ("Zacatlan", 205, 19.926, -97.961),
]

# Generacion de registros
records = []
for i in range(1, 5001):
    mun = random.choice(municipios)
    edad = np.random.randint(18, 91)
    genero = random.choice(["Masculino", "Femenino"])
    nivel_socio = random.choice(["Bajo", "Medio", "Alto"])
    acceso = random.choice(["IMSS", "ISSSTE", "Privado", "Ninguno"])
    presion_s = np.random.randint(80, 201)
    presion_d = np.random.randint(50, 121)
    colesterol = np.random.randint(100, 301)
    glucosa = np.random.randint(70, 301)
    imc = round(np.random.uniform(15.0, 45.0), 2)
    fumador = random.choice(["Si", "No"])
    hist_fam = random.choice(["Si", "No"])
    riesgo_score = np.random.randint(0, 101)
    diagnostico = int(riesgo_score > 50)

    records.append({
        "ID_Paciente": f"PAC_{i:04d}",
        "Municipio": mun[0], "CVE_MUN": mun[1],
        "Latitude": round(mun[2] + np.random.uniform(-0.1, 0.1), 6),
        "Longitude": round(mun[3] + np.random.uniform(-0.1, 0.1), 6),
        "Edad": edad, "Genero": genero,
        "Nivel_Socioeconomico": nivel_socio, "Acceso_Salud": acceso,
        "Presion_Sistolica": presion_s, "Presion_Diastolica": presion_d,
        "Colesterol_Total": colesterol, "Glucosa": glucosa, "IMC": imc,
        "Fumador": fumador, "Historial_Familiar": hist_fam,
        "Riesgo_Score": riesgo_score, "Diagnostico_Infarto": diagnostico,
    })

df = pd.DataFrame(records)
df.to_csv("../data/pacientes_puebla.csv", index=False)
print(f"Dataset generado: {df.shape[0]} registros, {df.shape[1]} columnas")
