import pandas as pd
import matplotlib.pyplot as plt

# 1. Importar el CSV usando rutas relativas
try:
    df = pd.read_csv('datos/dataset.csv', sep=';')
except:
    df = pd.read_csv('datos/dataset.csv')

# --- SANITIZACIÓN DEL SEPARADOR DECIMAL ---
if df['Mean'].dtype == 'object':
    df['Mean'] = df['Mean'].astype(str).str.replace(',', '.')

df['Mean'] = pd.to_numeric(df['Mean'])

# --- REQUERIMIENTO TÉCNICO: Sumar Ordenada al Origen ---
# Definimos la temperatura media promedio histórica como base de referencia (14.0°C)
ordenada_origen = 14.0
df['Mean_Real'] = df['Mean'] + ordenada_origen

# 2. Calcular los indicadores estadísticos en base a los valores reales
temp_promedio = df['Mean_Real'].mean()
temp_maxima = df['Mean_Real'].max()
temp_minima = df['Mean_Real'].min()

print("--- RESULTADOS CON VALORES REALES (ORDENADA: 14.0°C) ---")
print(f"Temperatura Real Promedio Histórica: {temp_promedio:.4f}°C")
print(f"Temperatura Real Máxima Registrada: {temp_maxima:.4f}°C")
print(f"Temperatura Real Mínima Registrada: {temp_minima:.4f}°C\n")

# 3. Generar el gráfico de evolución temporal con valores reales (Fuente: GCAG)
plt.figure(figsize=(12, 6))
df_filtrado = df[df['Source'] == 'GCAG'].sort_values('Year')

# Graficamos la nueva columna de valores reales
plt.plot(df_filtrado['Year'], df_filtrado['Mean_Real'], marker='.', color='darkblue', linestyle='-', linewidth=1)
plt.title('Evolución de la Temperatura Media Global Absoluta (Valores Reales)')
plt.xlabel('Año')
plt.ylabel('Temperatura Global Real (°C)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# 4. Guardar el gráfico en la carpeta de resultados
plt.savefig('resultados/evolucion_temperatura.png')
print("¡Gráfico de valores reales guardado con éxito en 'resultados/evolucion_temperatura.png'!")
