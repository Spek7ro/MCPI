import numpy as np
from scipy.integrate import quad
import math

def calcular_coeficientes_fourier(f, T, N_max):
    omega_0 = 2 * np.pi / T
    t1 = 0
    t2 = T
    print(f"Calculando coeficientes con T = {T} y ω₀ = {omega_0:.4f}")
    

    integral_a0, error_a0 = quad(f, t1, t2)
    a0 = (1 / T) * integral_a0
    
    an = np.zeros(N_max)
    bn = np.zeros(N_max)
    
    for n in range(1, N_max + 1):
        # Integrando para an
        integrando_an = lambda t: f(t) * np.cos(n * omega_0 * t)
        integral_an, error_an = quad(integrando_an, t1, t2)
        an[n-1] = (2 / T) * integral_an
        
        # Integrando para bn
        integrando_bn = lambda t: f(t) * np.sin(n * omega_0 * t)
        integral_bn, error_bn = quad(integrando_bn, t1, t2)
        bn[n-1] = (2 / T) * integral_bn
        
    return a0, an, bn

# ----------------------------------------------------
# Ejemplo de Uso: Onda Cuadrada Centrada (-1 a 1)
# ----------------------------------------------------

# La onda cuadrada de la serie original (imagen 1) va de -1 a 1
# y tiene Periodo T=2.
# En el intervalo [0, T], la función es:
# f(t) = -1 para 0 <= t < 1
# f(t) = 1  para 1 <= t < 2

def onda_cuadrada_menos1_a_1(t):
    # Usamos la operación módulo para hacer la función periódica
    t_mod = np.fmod(t, 2)
    
    # Si el tiempo es entre 0 y 1 (exclusivo), es -1. Si es entre 1 y 2 (exclusivo), es 1.
    if isinstance(t_mod, np.ndarray):
        # Para numpy arrays (integración)
        return np.where((t_mod >= 0) & (t_mod < 1), -1.0, 1.0)
    else:
        # Para valores individuales (definición)
        if t_mod >= 0 and t_mod < 1:
            return -1.0
        else: # de 1 a 2
            return 1.0

# Ejemplo 
T_ejemplo = 2.0  # Período de la onda cuadrada
N_max_ejemplo = 6 # Calcular hasta el décimo armónico (n=1 a n=6)


a0_res, an_res, bn_res = calcular_coeficientes_fourier(
    onda_cuadrada_menos1_a_1, 
    T_ejemplo, 
    N_max_ejemplo
)

print("\n--- Resultados (Onda Cuadrada, T=2, Rango [-1, 1]) ---")

# Coeficiente a0
print(f"\nCoeficiente a0 (Valor promedio): {a0_res:.4f}")
# Se espera que a0 sea ~0 ya que la función es impar y está centrada.

# Coeficientes an (Coseno)
print("\nCoeficientes an (Coseno):")
for n, val in enumerate(an_res, 1):
    print(f"a_{n} = {val:.4e} (Se espera ~0 por simetría impar)")

# Coeficientes bn (Seno)
print("\nCoeficientes bn (Seno):")
for n, val in enumerate(bn_res, 1):
    if n % 2 != 0:
        valor_esperado = 4 / (n * np.pi)
        print(f"b_{n} = {val:.4f} (Esperado: {valor_esperado:.4f})")
    else:
        print(f"b_{n} = {val:.4e} (Esperado: 0.0)")
        
        