import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button

# --- 1. Definición de Parámetros de Tiempo (AJUSTADOS para la Figura 2) ---

# Señales: x(t) es de [-2, 2], h(t) es de [-0.5, 0.5].
# Resultado y(t) existe de (-2 + -0.5) = -2.5 a (2 + 0.5) = 2.5.

# Rango de tiempo para las señales individuales (eje tau). Debe cubrir de -2 a 2.
t_original_start = -3.0  
t_original_end = 3.0    
muestras_original = 500
t_tau = np.linspace(t_original_start, t_original_end, muestras_original, endpoint=False) 

# Rango de tiempo para el desplazamiento 't' (eje y(t)). Debe cubrir de -2.5 a 2.5.
t_desplazamiento_start = -3.0 
t_desplazamiento_end = 3.0    
num_frames = 150 # Más frames para mejor resolución de y(t)
t_valores_animacion = np.linspace(t_desplazamiento_start, t_desplazamiento_end, num_frames)

dt = t_tau[1] - t_tau[0] # Paso de tiempo para la integración

# --- 2. Definición de las Señales x(tau) y h(tau) (FIGURA 2) ---

# x(tau): Pulso Triangular, Altura 2, de -2 a 2
def x_func(tau):
    y = np.zeros_like(tau)
    
    # Rampa ascendente: 2*tau + 4, para -2 <= tau < 0
    mask_asc = (tau >= -2) & (tau < 0)
    y[mask_asc] = 2 * tau[mask_asc] + 4
    
    # Rampa descendente: -2*tau + 4, para 0 <= tau <= 2
    mask_desc = (tau >= 0) & (tau <= 2)
    y[mask_desc] = -2 * tau[mask_desc] + 4
    
    return y

# h(tau): Pulso rectangular, Altura 1, de -0.5 a 0.5
def h_func(tau):
    return np.where((tau >= -0.5) & (tau <= 0.5), 1.0, 0.0)

# Muestreo de x(tau)
x_tau = x_func(t_tau)

# --- 3. Inicialización de las Gráficas ---

# --- Figura 1: Animación de la Operación (ax1) ---
fig1 = plt.figure(figsize=(10, 6)) 
ax1 = fig1.add_subplot(1, 1, 1)
fig1.subplots_adjust(bottom=0.15) 

ax1.set_xlim(t_original_start, t_original_end)
ax1.set_ylim(-0.5, 4) # x(t) alcanza altura 2
ax1.set_xlabel('$\\tau$')
ax1.set_ylabel('Amplitud')
ax1.set_title('Convolución Animada (Operación de Solapamiento)')
ax1.grid(True, linestyle='--')

line_x, = ax1.plot(t_tau, x_tau, 'g-', linewidth=2, label='$x(\\tau)$')
line_h_shifted, = ax1.plot(t_tau, np.zeros_like(t_tau), 'r-', linewidth=2, label='$h(t-\\tau)$')
line_product, = ax1.plot(t_tau, np.zeros_like(t_tau), 'm-', linewidth=2, label='$x(\\tau) h(t-\\tau)$')

fill_product = ax1.fill_between(t_tau, np.zeros_like(t_tau), np.zeros_like(t_tau), color='purple', alpha=0.3, label='Producto Integrado')
ax1.legend()

# --- Figura 2: Resultado de la Convolución (ax2) ---
fig2 = plt.figure(figsize=(8, 4))
ax2 = fig2.add_subplot(1, 1, 1) 

# Amplitud máxima es aproximadamente 2 (Integral de una sección de ancho 1 alrededor del pico de x(t))
ax2.set_xlim(t_desplazamiento_start, t_desplazamiento_end) 
ax2.set_ylim(-0.5, 4) 
ax2.set_xlabel('Tiempo $t$')
ax2.set_ylabel('$y(t)$')
ax2.set_title('Resultado de la Convolución $y(t)$: Triángulo * Rectangular') 
ax2.grid(True, linestyle='--')

line_y, = ax2.plot([], [], 'b-', linewidth=2, label='Convolución $y(t)$')
ax2.legend()
plt.tight_layout() 

# Almacenar los valores de y(t) y control de animación
y_valores = []
t_puntos_y = []
is_paused = False
anim = None # Inicialización global de la animación

# --- 4. Función de Pausa/Reanudar ---

def pause_resume(event):
    global is_paused, anim
    is_paused = not is_paused 
    
    if anim is None:
        print("Error: La animación aún no ha sido inicializada.")
        return

    if is_paused:
        anim.event_source.stop()
        button.label.set_text('Reanudar ▶')
        print(f"Animación pausada en t = {t_puntos_y[-1]:.2f}")
    else:
        anim.event_source.start()
        button.label.set_text('Pausa ⏸')
        print("Animación reanudada.")

# --- 5. Función de Actualización para la Animación ---
def animate(i):
    global y_valores, t_puntos_y, fill_product, is_paused

    if is_paused:
        return line_h_shifted, line_product, line_y,

    current_t = t_valores_animacion[i]
    
    # Flip and Shift: h(t-tau)
    h_shifted_tau = h_func(current_t - t_tau) 
    
    # Producto de las señales: x(tau) * h(t-tau)
    product = x_tau * h_shifted_tau
    
    # Integral (Convolución para el tiempo actual 't')
    integral_value = np.sum(product) * dt
    
    # Actualizar Figura 1 (ax1)
    line_h_shifted.set_ydata(h_shifted_tau)
    line_product.set_ydata(product)
    
    fill_product.remove()
    fill_product = ax1.fill_between(t_tau, 0, product, where=(product > 0), color='purple', alpha=0.3)
    
    ax1.set_title(f'Convolución Animada (t = {current_t:.2f})')
    
    # Actualizar Figura 2 (ax2)
    y_valores.append(integral_value)
    t_puntos_y.append(current_t)
    
    line_y.set_data(t_puntos_y, y_valores)
    
    return line_h_shifted, line_product, line_y,

# --- 6. Crear el Botón y Ejecutar la Animación ---

# Conectamos el botón a la Figura 1 (fig1)
ax_button = fig1.add_axes([0.4, 0.05, 0.2, 0.05])
button = Button(ax_button, 'Pausa ⏸')
button.on_clicked(pause_resume) 

# La animación está ligada a la Figura 1
anim = FuncAnimation(fig1, animate, frames=num_frames, interval=50, blit=False, repeat=False) 

# Muestra ambas figuras (ventanas)
plt.show()

print("\nSe ha iniciado la animación para la convolución del pulso triangular y el pulso rectangular de la Figura 2.")
print("La gráfica resultante y(t) será una curva con lados parabólicos y un pico suavizado.")
