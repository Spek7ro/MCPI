import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# 1. Definición de Parámetros

# Rango de tiempo para el muestreo (suficientemente amplio para la convolución)
T_start = -1.0
T_end = 3.0 
# Número de puntos para una buena aproximación continua
# Un valor más alto dará una mejor aproximación a la convolución continua
muestras = 1000
dt = (T_end - T_start) / muestras # Paso de tiempo
t = np.linspace(T_start, T_end, muestras, endpoint=False) 

# 2. Definición de las Señales x(t) y h(t)

# x(t) = t, si 0 <= t <= 1; 0 en caso contrario (Señal Triangular/Rampa)
def x_func(t):
    # para 0 <= t <= 1
    return np.where((t >= 0) & (t <= 1), t, 0.0)

# h(t) = 1, si 0 <= t <= 1; 0 en caso contrario (Señal Rectangular/Pulso)
def h_func(t):
    # para 0 <= t <= 1
    return np.where((t >= 0) & (t <= 1), 1.0, 0.0)

# Muestreo de las señales
x_t = x_func(t)
h_t = h_func(t)

# --- 3. Cálculo de la Convolución Discreta ---

# La convolución discreta (numérica) se usa para aproximar la continua.
# La función `convolve` de SciPy devuelve la convolución de dos arreglos 1D.
# Multiplicamos por 'dt' para que la suma discreta aproxime la integral continua (método de Riemann).
y_conv_discreta = signal.convolve(x_t, h_t, mode='full') * dt

# --- 4. Cálculo del Vector de Tiempo para y(t) ---

# La longitud de la señal de convolución (y(t)) es len(x_t) + len(h_t) - 1.
# El tiempo de inicio de y(t) es la suma de los tiempos de inicio de x(t) y h(t).
len_y = len(y_conv_discreta)
t_y = np.linspace(T_start * 2, T_end * 2, len_y, endpoint=False)


# --- 5. Visualización de Resultados ---
## Gráficas de las Señales Originales
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, x_t, label='$x(t) = t \cdot u(t) - t \cdot u(t-1)$', color='blue')
plt.title('Señal $x(t)$')
plt.grid(True, linestyle='--')
plt.ylim(-0.1, 1.1)

plt.subplot(3, 1, 2)
plt.plot(t, h_t, label='$h(t) = u(t) - u(t-1)$', color='green')
plt.title('Señal $h(t)$')
plt.grid(True, linestyle='--')
plt.ylim(-0.1, 1.1)

# Recortar el eje x de y(t) para el rango de interés [0, 2]
# y(t) existe de 0+0=0 a 1+1=2.
idx_start = np.argmin(np.abs(t_y - (0.0))) 
idx_end = np.argmin(np.abs(t_y - (2.0)))
t_y_recortado = t_y[idx_start:idx_end+2]
y_conv_recortado = y_conv_discreta[idx_start:idx_end+2]

## Gráfica de la Convolución
plt.subplot(3, 1, 3)
plt.plot(t_y_recortado, y_conv_recortado, label='$y(t) = x(t) * h(t)$', color='red', linewidth=3)
plt.title('Resultado de la Convolución $y(t)$')
plt.xlabel('Tiempo $t$')
plt.grid(True, linestyle='--')
plt.xlim(T_start, T_end)
plt.ylim(-0.1, 0.6)

plt.tight_layout()
plt.show()

# 6. Resultado Analítico (Para Comparación)

# El resultado analítico de esta convolución es (lo puedes verificar resolviendo la integral)
def y_analitica(t):
    y = np.zeros_like(t)
    
    # Caso 1: 0 <= t < 1
    mask1 = (t >= 0) & (t < 1)
    y[mask1] = (t[mask1]**2) / 2
    
    # Caso 2: 1 <= t < 2
    mask2 = (t >= 1) & (t < 2)
    y[mask2] = -(t[mask2]**2) / 2 + 2 * t[mask2] - 1
    
    return y

# Gráfica para comparar la solución numérica con la analítica
plt.figure(figsize=(8, 4))
plt.plot(t_y_recortado, y_conv_recortado, label='Convolución Numérica (SciPy)', color='red', linestyle='--', linewidth=3)
plt.plot(t_y_recortado, y_analitica(t_y_recortado), label='Convolución Analítica', color='black', linewidth=1)
plt.title('Comparación: Convolución Numérica vs. Analítica')
plt.xlabel('Tiempo $t$')
plt.legend()
plt.grid(True, linestyle='--')
plt.ylim(-0.1, 0.6)
plt.xlim(0, 2)
plt.show()

print("\nLa convolución discreta con SciPy aproxima la solución analítica.")
