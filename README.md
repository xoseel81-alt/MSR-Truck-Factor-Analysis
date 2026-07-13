# MSR-Truck-Factor-Analysis

# Evaluación Multifactorial del Truck Factor mediante Minería de Repositorios (MSR)

Este repositorio contiene el motor analítico y el conjunto de datos empíricos utilizados en el artículo científico titulado: *"Evaluación multifactorial del Truck Factor: Un enfoque basado en la dominancia por archivo y la rotación temporal del equipo de desarrollo"*.

## 📊 Descripción del Proyecto
El script implementa un marco analítico basado en la Minería de Repositorios de Software (MSR) para evaluar la relación entre el tamaño de los componentes de software (SLOC) y el Índice de Dominancia (DA %) del autor principal. El modelo ha sido validado bajo un enfoque de *Data Freeze* (congelamiento de datos) utilizando los historiales transaccionales reales de tres ecosistemas maduros: **Requests, FastAPI y Pydantic** (N = 19 archivos clave).

## 🗂️ Estructura del Repositorio
* `analisis_msr.py`: Script principal en Python que procesa la matriz de datos, clasifica los componentes en cuadrantes de riesgo, ejecuta el test estadístico de correlación de Spearman y genera la visualización científica.
* `grafica_validez_externa.png`: Gráfica de dispersión comparativa y línea de tendencia global generada por el algoritmo.

## 🚀 Cómo Ejecutar el Análisis
El script es completamente autónomo y no requiere bases de datos externas. Para replicar los resultados del artículo:

1. Asegúrate de tener instalado Python 3 y las librerías necesarias:
   ```bash
   pip install pandas matplotlib numpy scipy
   ```
2. Ejecuta el script desde tu terminal:
   ```bash
   python analisis_msr.py
   ```

## 📈 Resultados Verificados en el Script
* **Requests:** Coeficiente de Spearman $\rho = -0.5042$
* **FastAPI:** Coeficiente de Spearman $\rho = -0.9429$
* **Pydantic:** Coeficiente de Spearman $\rho = -0.9856$

