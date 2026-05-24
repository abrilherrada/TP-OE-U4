
# Análisis de datos climáticos

## Descripción del proyecto

Este proyecto se desarrolló con el objetivo de aplicar herramientas básicas de análisis de datos utilizando Python, GitHub, Google Colab y Jira dentro de un entorno de trabajo colaborativo.

El trabajo se realizó como parte de la materia Organización Empresarial de la Tecnicatura Universitaria en Programación a Distancia de la Universidad Tecnológica Nacional.

---

## Integrantes

- Abril Herrada
- Erik Riberi

---

## Roles de trabajo

Debido a que el equipo estuvo conformado por dos integrantes y la consigna contemplaba tres roles de trabajo (P1, P2 y P3), las responsabilidades se distribuyeron de la siguiente manera:

- Abril Herrada: roles P1 y P3
- Erik Riberi: rol P2

---

## Escenario elegido

El proyecto se desarrolló sobre un escenario de análisis de datos climáticos históricos utilizando Python para procesar información meteorológica y generar visualizaciones estadísticas a partir de un dataset de temperaturas globales.

---

## Objetivos

- Procesar un archivo CSV con datos meteorológicos.
- Calcular indicadores estadísticos básicos.
- Generar al menos un gráfico de temperatura.
- Exportar resultados obtenidos.
- Aplicar herramientas de trabajo colaborativo utilizando Git, GitHub y Jira.

---

## Dataset utilizado

Se utilizó un dataset climático histórico con registros de temperatura media global por año. El archivo fue almacenado en formato CSV y posteriormente sanitizado para garantizar la correcta interpretación de valores numéricos dentro del análisis realizado en Python.

El dataset contiene principalmente:

- Año del registro
- Temperatura media
- Variaciones térmicas históricas

Los datos se utilizaron para calcular indicadores estadísticos y generar un gráfico de evolución temporal.

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

## Requisitos y dependencias

Para ejecutar de forma correcta el script de análisis, es necesario contar con un entorno de Python 3 y tener instaladas las siguientes librerías de ciencia de datos:

- **Pandas**: Para la manipulación, sanitización y análisis de las estructuras de datos.
- **Matplotlib**: Para la generación y exportación del gráfico de evolución térmica.

_Instalación de dependencias mediante pip:_

```bash
pip install pandas matplotlib
```

---

## Instrucciones de ejecución

El proyecto utiliza rutas relativas, por lo que el script debe ejecutarse posicionándose en la raíz del repositorio:

1. Coloque el archivo fuente `dataset.csv` dentro del directorio `datos/`.
2. Ejecute el script de análisis estadístico desde la terminal:
   ```bash
   python scripts/analisis.py
   ```
3. Los indicadores estadísticos se imprimirán en la consola y el gráfico se exportará a la carpeta `resultados/evolucion_temperatura.png`.

---

## Decisiones de diseño y análisis crítico

Durante la fase de desarrollo técnico e ingeniería de datos, se tomaron dos decisiones de diseño fundamentales para garantizar el éxito del script:

1. **Sanitización del separador decimal:** Se detectó que el archivo fuente `dataset.csv` provisto presentaba las anomalías térmicas utilizando la coma (`,`) como separador de decimales. Se implementó una lógica de conversión dinámica en el script (`.str.replace(',', '.')`) para transformar el formato a punto decimal antes de realizar las operaciones estadísticas, evitando errores de ejecución (_TypeError_).
2. **Uso de rutas relativas para reproducibilidad:** Se descartó el uso de rutas absolutas locales del entorno de Colab. Al definir rutas relativas estrictas, se asegura la total reproducibilidad del código, garantizando que cualquier integrante del equipo o la cátedra pueda clonar el repositorio y correr el flujo de punta a punta sin necesidad de reconfigurar rutas de archivos.
