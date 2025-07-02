import pandas as pd

# Leer archivo CSV
file_path = 'modelos_evaluados.csv'
df = pd.read_csv(file_path)

# Asegurar que la columna 'Similitud Promedio' esté en formato numérico
df['Similitud Promedio'] = pd.to_numeric(df['Similitud Promedio'], errors='coerce')

# Calcular el promedio de similitud por modelo
model_avg_similarity = df.groupby('Modelo')['Similitud Promedio'].mean()

# Ordenar de mayor a menor
model_avg_similarity_sorted = model_avg_similarity.sort_values(ascending=False)

# Mostrar el modelo con el promedio más alto
print("Promedio de similitud por modelo:")
print(model_avg_similarity_sorted)

print("\nModelo con mejor promedio de similitud:")
best_model = model_avg_similarity_sorted.idxmax()
best_avg = model_avg_similarity_sorted.max()
print(f"{best_model}: {best_avg:.4f}")
