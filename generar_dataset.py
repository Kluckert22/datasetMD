# ==========================================
# Generador de Dataset Sintético - Deserción Estudiantil
# ==========================================

import pandas as pd
import numpy as np

# 1. Número de registros
n = 500  # mínimo

# 2. Variables sintéticas
# Demográficas
edad = np.random.randint(16, 30, n)
genero = np.random.choice(['Masculino', 'Femenino'], n)
origen = np.random.choice(['Urbano', 'Rural'], n)

# Académicas
promedio_secundaria = np.random.uniform(1.0, 5.0, n).round(2)
examen_admision = np.random.randint(0, 100, n)
notas_semestre1 = np.random.uniform(1.0, 5.0, n).round(2)

# Financieras
nivel_socioeco = np.random.choice(['Bajo', 'Medio', 'Alto'], n)
beca = np.random.choice(['Sí', 'No'], n)
prestamo = np.random.choice(['Sí', 'No'], n)

# Variable objetivo
desercion = np.random.choice(['Sí', 'No'], n, p=[0.3, 0.7])

# 3. Crear DataFrame
data = pd.DataFrame({
    'Edad': edad,
    'Genero': genero,
    'Origen': origen,
    'Promedio_Secundaria': promedio_secundaria,
    'Examen_Admision': examen_admision,
    'Notas_Semestre1': notas_semestre1,
    'Nivel_Socioeco': nivel_socioeco,
    'Beca': beca,
    'Prestamo': prestamo,
    'Desercion': desercion
})

# 4. Introducir valores nulos
for col in ['Promedio_Secundaria', 'Notas_Semestre1', 'Examen_Admision']:
    data.loc[data.sample(frac=0.05).index, col] = np.nan

# 5. Introducir outliers
data.loc[data.sample(frac=0.02).index, 'Promedio_Secundaria'] = 7.0
data.loc[data.sample(frac=0.02).index, 'Notas_Semestre1'] = -1.0
data.loc[data.sample(frac=0.02).index, 'Examen_Admision'] = 999

# 6. Guardar dataset
data.to_csv("dataset_desercion.csv", index=False, encoding='utf-8')
print("✅ Dataset generado con éxito: dataset_desercion.csv")
print(data.head())
