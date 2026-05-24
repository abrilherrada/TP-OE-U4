
import pandas as pd
import matplotlib.pyplot as plt

# 1. Importar el CSV usando rutas relativas
try:
    df = pd.read_csv('datos/dataset.csv', sep=';')
except:
    df = pd.read_csv('datos/dataset.csv')

# --- REQUERIMIENTO TÉCNICO: Conversión de coma a punto decimal ---
# El dataset utiliza comas como separador decimal. Convertimos las comas a puntos para permitir el procesamiento numérico correcto mediante Pandas.
if df['Mean'].dtype == 'object':
    df['Mean'] = df['Mean'].astype(str).str.replace(',', '.')

df['Mean'] = pd.to_numeric(df['Mean'])

# 2. Calcular los indicadores estadísticos reales
temp_promedio = df['Mean'].mean()
temp_maxima = df['Mean'].max()
temp_minima = df['Mean'].min()

print("--- RESULTADOS DEL ANÁLISIS CLIMÁTICO ---")
print(f"Temperatura Media Promedio: {temp_promedio:.4f}°C")
print(f"Temperatura Media Máxima: {temp_maxima:.4f}°C")
print(f"Temperatura Media Mínima: {temp_minima:.4f}°C")
print()

# 3. Generar el gráfico de evolución temporal (Fuente: GCAG)
plt.figure(figsize=(12, 6))
df_filtrado = df[df['Source'] == 'GCAG'].sort_values('Year')

plt.plot(df_filtrado['Year'], df_filtrado['Mean'], marker='.', color='darkred', linestyle='-', linewidth=1)
plt.title('Evolución de la Temperatura Media Global (Dataset Sanitizado)')
plt.xlabel('Año')
plt.ylabel('Anomalía Térmica (°C)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# 4. Guardar el gráfico en la carpeta de resultados
plt.savefig('resultados/evolucion_temperatura.png')
print("¡Gráfico guardado con éxito en 'resultados/evolucion_temperatura.png'!")
