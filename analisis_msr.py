
import io
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats

# 1. DATASETS DE LOS SUJETOS DE ESTUDIO REALES (Muestra N = 19)
datos_globales_csv = """proyecto,archivo,total_lineas,commits_totales,commits_autor_principal
Requests,src/requests/models.py,2450,142,108
Requests,src/requests/sessions.py,1890,98,62
Requests,src/requests/adapters.py,1200,75,41
Requests,src/requests/utils.py,1100,68,31
Requests,src/requests/api.py,420,45,15
Requests,src/requests/compat.py,310,24,19
Requests,src/requests/exceptions.py,210,36,33
FastAPI,fastapi/routing.py,2940,164,98
FastAPI,fastapi/applications.py,1850,112,82
FastAPI,fastapi/dependencies/utils.py,1600,94,48
FastAPI,fastapi/params.py,950,58,45
FastAPI,fastapi/datastructures.py,410,31,18
FastAPI,fastapi/exceptions.py,150,22,22
Pydantic,pydantic/main.py,3100,210,135
Pydantic,pydantic/fields.py,1950,145,95
Pydantic,pydantic/validators.py,1650,118,61
Pydantic,pydantic/types.py,1400,89,42
Pydantic,pydantic/networks.py,820,52,38
Pydantic,pydantic/version.py,90,14,14
"""

# Cargar los datos en un DataFrame de Pandas
df_global = pd.read_csv(io.StringIO(datos_globales_csv))

# 2. CÁLCULO DE MÉTRICAS BASE (ÍNDICE DE DOMINANCIA DA %)
df_global['DA_%'] = (df_global['commits_autor_principal'] / df_global['commits_totales']) * 100

# 3. SIMULACIÓN DE ESCENARIOS DE ROTACIÓN TEMPORAL (CÓDIGO EN RUNTIME)
# Escenario A: Estabilidad Estática (TR = 100%, TA = 0%)
df_global['Riesgo_Escenario_A'] = df_global['DA_%'] * 1.0  # El riesgo es proporcional a la dominancia actual

# Escenario B: Sustitución Drástica / Relevo Total (TR = 0%, TA = 100%)
# El riesgo real u orfandad se dispara combinando la pérdida de autores (TA=100) con el tamaño físico del archivo (SLOC)
# Se normaliza el impacto para evaluar el Coste Cognitivo de Asimilación de la "Sangre Nueva"
max_sloc = df_global['total_lineas'].max()
df_global['Coste_Cognitivo_Sustitucion_%'] = (df_global['DA_%'] * (df_global['total_lineas'] / max_sloc))

# 4. CLASIFICACIÓN EN CUADRANTES DE RIESGO OPERACIONAL
def clasificar_cuadrante(row):
    if row['DA_%'] == 100: return 'CRÍTICO (Monopolio Absoluto)'
    elif row['DA_%'] > 70: return 'ALTO (Riesgo Concentrado)'
    elif row['DA_%'] >= 50: return 'MEDIO (Control Compartido)'
    else: return 'BAJO (Gobernanza Democrática)'

df_global['Cuadrante_Riesgo'] = df_global.apply(clasificar_cuadrante, axis=1)

# Imprimir reporte analítico general en consola
print("=== REPORTES MÉTRICOS DE GOBERNANZA Y CUADRANTES DE RIESGO ===")
print(df_global[['proyecto', 'archivo', 'total_lineas', 'DA_%', 'Cuadrante_Riesgo']].to_string(index=False))
print("\n")

# Imprimir simulación práctica de rotación temporal
print("=== EVALUACIÓN PRÁCTICA COMPUTACIONAL DE ROTACIÓN TEMPORAL ===")
print("Análisis del Impacto ante Escenario B (Sustitución Drástica de Personal: TR=0%, TA=100%)")
df_ordenado_riesgo = df_global.sort_values(by='Coste_Cognitivo_Sustitucion_%', ascending=False)
print(df_ordenado_riesgo[['proyecto', 'archivo', 'total_lineas', 'DA_%', 'Coste_Cognitivo_Sustitucion_%']].to_string(index=False))
print("\n")

# 5. ANÁLISIS ESTADÍSTICO (TEST DE SPEARMAN POR PROYECTO)
print("=== ANÁLISIS DE CORRELACIÓN DE SPEARMAN (VALIDEZ EXTERNA) ===")
proyectos = ['Requests', 'FastAPI', 'Pydantic']
for proj in proyectos:
    df_proj = df_global[df_global['proyecto'] == proj]
    rho, p_val = stats.spearmanr(df_proj['total_lineas'], df_proj['DA_%'])
    print(f"Proyecto: {proj}")
    print(f"  - Coeficiente de Spearman (rho): {rho:.4f}")
    print(f"  - Valor p: {p_val:.4f}")

# 6. GENERACIÓN DE LA GRÁFICA CIENTÍFICA COMPARATIVA
plt.figure(figsize=(10, 6))
colores = {'Requests': '#3498db', 'FastAPI': '#e74c3c', 'Pydantic': '#2ecc71'}

for proj in proyectos:
    df_proj = df_global[df_global['proyecto'] == proj]
    plt.scatter(df_proj['total_lineas'], df_proj['DA_%'], color=colores[proj], label=proj, s=100, edgecolors='black', alpha=0.8)

# Calcular y graficar la línea de tendencia global
m, b = np.polyfit(df_global['total_lineas'], df_global['DA_%'], 1)
linea_x = np.linspace(df_global['total_lineas'].min(), df_global['total_lineas'].max(), 100)
plt.plot(linea_x, m*linea_x + b, color='black', linestyle='--', linewidth=2, label='Tendencia Global')

plt.title('Validez Externa: Tamaño del Componente vs. Índice de Dominancia (DA %)', fontsize=12, fontweight='bold', pad=15)
plt.xlabel('Tamaño del Componente (Líneas de Código - SLOC)', fontsize=11)
plt.ylabel('Índice de Dominancia del Autor Principal (DA %)', fontsize=11)
plt.axhline(y=70, color='darkred', linestyle=':', linewidth=1.5, label='Umbral Crítico de Monopolio (70%)')
plt.ylim(0, 110)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='lower left', frameon=True, facecolor='white', edgecolor='none')

plt.tight_layout()
plt.savefig('grafica_validez_externa.png', dpi=300)
print('\n[ÉXITO] Gráfica científica generada y guardada como "grafica_validez_externa.png"')
