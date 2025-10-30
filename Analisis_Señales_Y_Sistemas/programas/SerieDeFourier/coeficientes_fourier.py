import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt


def calcular_coeficientes_fourier(f, T, N_max, t1=0):
    
    # Frecuencia angular fundamental omega_0 = 2*pi / T
    omega_0 = 2 * np.pi / T
    # Límites de integración: [t1, t2]
    t2 = t1 + T
    
    print(f"--- Iniciando Cálculo Numérico ---")
    print(f"Período T = {T}, Límite de integración = [{t1}, {t2}]")
    
    # 1. Coeficiente a0 (Valor DC o promedio)
    # Fórmula: a0 = (1 / T) * integral[f(t) dt]
    integral_a0, error_a0 = quad(f, t1, t2)
    a0 = (1 / T) * integral_a0
    
    # 2. Coeficientes an y bn (Armónicos)
    an = np.zeros(N_max)
    bn = np.zeros(N_max)
    
    # Factor de escala (2 / T)
    escala = 2 / T
    
    for n in range(1, N_max + 1):
        # Integrando para an: f(t) * cos(n * w0 * t)
        integrando_an = lambda t: f(t) * np.cos(n * omega_0 * t)
        integral_an, error_an = quad(integrando_an, t1, t2)
        an[n-1] = escala * integral_an
        
        # Integrando para bn: f(t) * sin(n * w0 * t)
        integrando_bn = lambda t: f(t) * np.sin(n * omega_0 * t)
        integral_bn, error_bn = quad(integrando_bn, t1, t2)
        bn[n-1] = escala * integral_bn
        
    return a0, an, bn

# Definición de la función por tramos
def onda_cuadrada_menos1_a_1(t):
    # Se usa np.fmod para mapear t a su posición dentro del periodo [0, 2)
    t_mod = np.fmod(t, 2)
    
    if t_mod >= 0 and t_mod < 1:
        return -1.0
    else:
        return 1.0

# Parámetros del cálculo
T_ejemplo = 2.0
N_max_ejemplo = 10 # Calcular hasta el décimo armónico


a0_res, an_res, bn_res = calcular_coeficientes_fourier(
    onda_cuadrada_menos1_a_1, 
    T_ejemplo, 
    N_max_ejemplo
)


print("\n--- Resultados Numéricos Obtenidos ---")

# Coeficiente a0
print(f"\n1. Coeficiente a0 (Valor promedio): {a0_res:.6f} (Esperado: ~0)")

# Coeficientes an (Coseno)
print("\n2. Coeficientes an (Coseno):")
for n, val in enumerate(an_res, 1):
    print(f"a_{n} = {val:.6e}") # Se espera que todos sean ~0

# Coeficientes bn (Seno)
print("\n3. Coeficientes bn (Seno):")
for n, val in enumerate(bn_res, 1):
    valor_esperado = 0.0
    # La solución analítica es 4/(n*pi) para n impar, y 0 para n par.
    if n % 2 != 0:
        valor_esperado = 4 / (n * np.pi)
        diferencia = np.abs(val - valor_esperado)
        print(f"b_{n} = {val:.6f} (Esperado: {valor_esperado:.6f}, Diferencia: {diferencia:.2e})")
    else:
        print(f"b_{n} = {val:.6e} (Esperado: 0.0)")


def serie_fourier_aproximacion(t, a0, an, bn, T):
    omega_0 = 2 * np.pi / T
    f_t = a0 * np.ones_like(t) # Inicializa con el término a0/2 si se usara el otro formato, aquí solo a0
    
    # En la fórmula de la imagen (a0 como valor promedio), la serie es:
    # f(t) = a0/2 + Sum[an*cos + bn*sen]
    # Pero si usamos la fórmula de la imagen a0 = (1/T) * integral, la serie es:
    # f(t) = a0 + Sum[an*cos + bn*sen]
    # Usaremos f(t) = a0 + Sum[an*cos + bn*sen] para ser consistentes con la definición de a0.
    
    # NOTA: En la práctica de señales, a0 se divide entre 2 en la serie: f(t) = a0/2 + ...
    # Ajustamos f_t para ser la serie que converge: f(t) = a0 + sum
    
    f_t = f_t # El valor promedio ya está incluido si a0 es la media.

    # Suma de armónicos
    for n in range(1, len(an) + 1):
        # Término par de la serie (an*cos + bn*sen)
        f_t += an[n-1] * np.cos(n * omega_0 * t) + bn[n-1] * np.sin(n * omega_0 * t)
        
    return f_t

# Dominio del tiempo para la gráfica
t_plot = np.linspace(-3 * T_ejemplo, 3 * T_ejemplo, 1000)

# Reconstruir la aproximación
aproximacion = serie_fourier_aproximacion(t_plot, a0_res, an_res, bn_res, T_ejemplo)

# Reconstruir la función original periódica para la gráfica
def funcion_original_periodica_plot(t, T, func):
    """Mapea la función original para graficarla periódicamente."""
    t_periodo = np.fmod(t, T)
    # Ajustar para números negativos
    t_periodo = np.where(t_periodo < 0, t_periodo + T, t_periodo)
    
    # Crear un array con los valores de la función original
    original_valores = np.vectorize(func)(t_periodo)
    return original_valores

original_plot = funcion_original_periodica_plot(t_plot, T_ejemplo, onda_cuadrada_menos1_a_1)

# Crear la figura
plt.figure(figsize=(10, 6))
plt.plot(t_plot, original_plot, 'b', linewidth=3, label='Onda Cuadrada Original')
plt.plot(t_plot, aproximacion, 'r--', linewidth=1.5, label=f'Aproximación de Fourier ({N_max_ejemplo} términos)')
plt.title(f'Aproximación de la Serie de Fourier (T={T_ejemplo})', fontsize=15)
plt.xlabel('Tiempo (t)')
plt.ylabel('f(t)')
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()
plt.ylim(-1.5, 1.5)
plt.axhline(0, color='black', linewidth=0.5)

plt.show()