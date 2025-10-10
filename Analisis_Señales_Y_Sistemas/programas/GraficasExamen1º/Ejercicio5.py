import numpy as np
import matplotlib.pyplot as plt

# --- 1. Definición de la Señal Original x(t) de la Figura 3 (CORREGIDA) ---

def x_original(t):
    y = np.zeros_like(t, dtype=float)

    # TRAMO 1: Constante 2 en [-2, -1]
    mask1 = (t >= -2) & (t <= -1)
    y[mask1] = 2.0

    # TRAMO 2: Constante 1 en (-1, 1]
    mask2 = (t > -1) & (t <= 1)
    y[mask2] = 1.0

    # TRAMO 3: Rampa de (1, 1) a (2, 0) => y = -t + 2 en (1, 2]
    mask3 = (t > 1) & (t <= 2)
    y[mask3] = -t[mask3] + 2
    
    # Asegurar los puntos de quiebre
    y[t == -2] = 2.0
    y[t == -1] = 1.0
    y[t == 1] = 1.0
    y[t == 2] = 0.0

    return y

# --- 2. Función de Transformación Genérica ---

def get_transformed_signal(signal_func, t_new_range, transform_func):
    """Calcula el valor de la señal transformada x(g(t)) para cada punto de t_new_range."""
    t_original_values_for_transform = transform_func(t_new_range)
    return signal_func(t_original_values_for_transform)

# --- 3. Parámetros y Preparación de la Gráfica ---

# Rango de tiempo para ambas señales. Cubre de -3 a 4.
t_range = np.linspace(-3, 4, 1000) 
x_t = x_original(t_range)

# --- 4. Generación de Subplots en UNA ventana ---

fig, axs = plt.subplots(2, 1, figsize=(10, 8)) # 2 filas, 1 columna
fig.suptitle('Señal Original $x(t)$ vs. Transformación $x((5/3)t - 2)$', fontsize=16)

# --- Gráfica 1: Señal Original $x(t)$ ---
axs[0].plot(t_range, x_t, label='$x(t)$ Original', color='black', linewidth=2)
axs[0].set_title('Señal Original $x(t)$', loc='left')
axs[0].set_xlabel('Tiempo $t$')
axs[0].set_ylabel('Amplitud')
axs[0].set_xlim(-3, 3) 
axs[0].set_ylim(-0.5, 2.5)
axs[0].grid(True, linestyle='--')
axs[0].axvline(0, color='gray', linestyle=':', linewidth=0.8)
axs[0].axhline(0, color='gray', linestyle=':', linewidth=0.8)
axs[0].legend()

# --- Gráfica 2: Transformación d) x((5/3)t - 2) ---
# Soporte: [0, 2.4]

transform_func_d = lambda t_val: (5/3) * t_val - 2
x_d = get_transformed_signal(x_original, t_range, transform_func_d)

axs[1].plot(t_range, x_d, label='$x((5/3)t - 2)$', color='orange', linewidth=2)
axs[1].set_title('d) $x((5/3)t - 2)$ (Compresión y Desplazamiento a la Derecha)', loc='left')
axs[1].set_xlabel('Tiempo $t$')
axs[1].set_ylabel('Amplitud')
axs[1].set_xlim(-1, 3) # Ajustar límites para esta transformación (de 0 a 2.4)
axs[1].set_ylim(-0.5, 2.5)
axs[1].grid(True, linestyle='--')
axs[1].axvline(0, color='gray', linestyle=':', linewidth=0.8)
axs[1].axhline(0, color='gray', linestyle=':', linewidth=0.8)
axs[1].legend()

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()