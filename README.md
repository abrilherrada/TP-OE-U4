# Análisis de datos climáticos

## Descripción del proyecto
Este proyecto tiene como objetivo analizar datos meteorológicos históricos mediante el uso de Python. A partir de un dataset climático, se calculan distintos indicadores estadísticos y se generan gráficos para visualizar la evolución de la temperatura en el tiempo.

El trabajo fue desarrollado como parte de la materia Organización Empresarial de la Tecnicatura Universitaria en Programación a Distancia de la Universidad Tecnológica Nacional.

---

## Integrantes

- Abril Herrada
- Erik Riberi

---

## Escenario elegido
Análisis de datos climáticos.

---

## Objetivos
- Procesar un archivo CSV con datos meteorológicos.
- Calcular indicadores estadísticos básicos.
- Generar gráficos de temperatura.
- Exportar resultados obtenidos.
- Aplicar herramientas de trabajo colaborativo utilizando Git, GitHub y Jira.

---

## Estructura del proyecto

```text
TP-OE-U4/
├── datos/
│   └── dataset.csv
├── scripts/
│   └── analisis.py
├── resultados/
│   └── evolucion_temperatura.png
├── README.md
└── .gitignore
```

---

## Requisitos y Dependencias
Para ejecutar de forma correcta el script de análisis, es necesario contar con un entorno de Python 3 y tener instaladas las siguientes librerías de ciencia de datos:
- **Pandas**: Para la manipulación, sanitización y análisis de las estructuras de datos.
- **Matplotlib**: Para la generación y exportación del gráfico de evolución térmica.

*Instalación de dependencias mediante pip:*
```bash
pip install pandas matplotlib
```

---

## Instrucciones de Ejecución
El proyecto utiliza rutas relativas, por lo que el script debe ejecutarse posicionándose en la raíz del repositorio:

1. Coloque el archivo fuente `dataset.csv` dentro del directorio `datos/`.
2. Ejecute el script de análisis estadístico desde la terminal:
   ```bash
   python scripts/analisis.py
   ```
3. Los indicadores estadísticos se imprimirán en la consola y el gráfico se exportará a la carpeta `resultados/evolucion_temperatura.png`.

---

## Decisiones de Diseño y Análisis Crítico
Durante la fase de desarrollo técnico e ingeniería de datos, se tomaron dos decisiones de diseño fundamentales para garantizar el éxito del script:

1. **Sanitización del Separador Decimal:** Se detectó que el archivo fuente `dataset.csv` provisto presentaba las anomalías térmicas utilizando la coma (`,`) como separador de decimales. Se implementó una lógica de conversión dinámica en el script (`.str.replace(',', '.')`) para transformar el formato a punto decimal antes de realizar las operaciones estadísticas, evitando errores de ejecución (*TypeError*).
2. **Uso de Rutas Relativas para Reproducibilidad:** Se descartó el uso de rutas absolutas locales del entorno de Colab. Al definir rutas relativas estrictas, se asegura la total reproducibilidad del código, garantizando que cualquier integrante del equipo o la cátedra pueda clonar el repositorio y correr el flujo de punta a punta sin necesidad de reconfigurar rutas de archivos.
