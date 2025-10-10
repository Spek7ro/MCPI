import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button

t_original_start = -3.0  
t_original_end = 3.0    
muestras_original = 500
t_tau = np.linspace(t_original_start, t_original_end, muestras_original, endpoint=False) 

t_desplazamiento_start = -3.5 
t_desplazamiento_end = 3.5    
num_frames = 100 # Número de pasos de tiempo en la animación
t_valores_animacion = np.linspace(t_desplazamiento_start, t_desplazamiento_end, num_frames)

dt = t_tau[1] - t_tau[0]

# --- 2. Definición de las Señales x(tau) y h(tau) (NUEVAS SEÑALES) ---
# x(tau): Pulso rectangular, Altura 1, de -1 a 1 (Duración 2)
def x_func(tau):
    return np.where((tau >= -1) & (tau <= 1), 1.0, 0.0)

# h(tau): Pulso rectangular, Altura 1, de -2 a 2 (Duración 4)
def h_func(tau):
    return np.where((tau >= -2) & (tau <= 2), 1.0, 0.0)

x_tau = x_func(t_tau)

# --- 3. Inicialización de las Gráficas ---
fig1 = plt.figure(figsize=(10, 6)) 
ax1 = fig1.add_subplot(1, 1, 1)
fig1.subplots_adjust(bottom=0.15) 

ax1.set_xlim(t_original_start, t_original_end)
ax1.set_ylim(-0.2, 1.2)
ax1.set_xlabel('$\\tau$')
ax1.set_ylabel('Amplitud')
ax1.set_title('Convolución Animada (Operación de Solapamiento)')
ax1.grid(True, linestyle='--')

line_x, = ax1.plot(t_tau, x_tau, 'g-', linewidth=2, label='$x(\\tau)$')
line_h_shifted, = ax1.plot(t_tau, np.zeros_like(t_tau), 'r-', linewidth=2, label='$h(t-\\tau)$')
line_product, = ax1.plot(t_tau, np.zeros_like(t_tau), 'm-', linewidth=2, label='$x(\\tau) h(t-\\tau)$')

# Área sombreada del producto
fill_product = ax1.fill_between(t_tau, np.zeros_like(t_tau), np.zeros_like(t_tau), color='purple', alpha=0.3, label='Producto Integrado')
ax1.legend()

# --- Figura 2: Resultado de la Convolución (ax2) ---
fig2 = plt.figure(figsize=(8, 4))
ax2 = fig2.add_subplot(1, 1, 1) 

# Amplitud máxima es 2 (Altura 1 * Altura 1 * Duración 2)
ax2.set_xlim(t_desplazamiento_start, t_desplazamiento_end) 
ax2.set_ylim(-0.5, 2.5) 
ax2.set_xlabel('Tiempo $t$')
ax2.set_ylabel('$y(t)$')
ax2.set_title('Resultado de la Convolución $y(t)$: Pulso Rectangular * Pulso Rectangular') 
ax2.grid(True, linestyle='--')

line_y, = ax2.plot([], [], 'b-', linewidth=2, label='Convolución $y(t)$')
ax2.legend()
plt.tight_layout() 

# Almacenar los valores de y(t)
y_valores = []
t_puntos_y = []

# --- 4. Variables de Control de Pausa (Globales) ---
is_paused = False
anim = None

# --- 5. Función de Pausa/Reanudar ---

def pause_resume(event):
    global is_paused, anim
    is_paused = not is_paused 
    
    if anim is None: # <--- AÑADIR ESTA COMPROBACIÓN
      print("Error: La animación aún no ha sido inicializada.")
      return
    
    if is_paused:
        # Pausar la animación
        anim.event_source.stop()
        button.label.set_text('Reanudar ▶')
        print(f"Animación pausada en t = {t_puntos_y[-1]:.2f}")
    else:
        # Reanudar la animación
        anim.event_source.start()
        button.label.set_text('Pausa ⏸')
        print("Animación reanudada.")

# --- 6. Función de Actualización para la Animación ---
def animate(i):
    # Declaración global de las variables que serán modificadas (CORREGIDO)
    global y_valores, t_puntos_y, fill_product, is_paused

    if is_paused:
        return line_h_shifted, line_product, line_y,

    current_t = t_valores_animacion[i]
    
    # 1. Flip and Shift: h(t-tau)
    h_shifted_tau = h_func(current_t - t_tau) 
    
    # 2. Producto de las señales: x(tau) * h(t-tau)
    product = x_tau * h_shifted_tau
    
    # 3. Integral (Convolución para el tiempo actual 't')
    integral_value = np.sum(product) * dt
    
    # 4. Actualizar Figura 1 (ax1)
    line_h_shifted.set_ydata(h_shifted_tau)
    line_product.set_ydata(product)
    
    # Actualizar el área sombreada
    fill_product.remove()
    fill_product = ax1.fill_between(t_tau, 0, product, where=(product > 0), color='purple', alpha=0.3)
    
    ax1.set_title(f'Convolución Animada (t = {current_t:.2f})')
    
    # 5. Actualizar Figura 2 (ax2)
    y_valores.append(integral_value)
    t_puntos_y.append(current_t)
    
    # Actualizamos la línea en la Figura 2
    line_y.set_data(t_puntos_y, y_valores)
    
    # Devolvemos los objetos modificados de la Figura 1
    return line_h_shifted, line_product, line_y,

# --- 7. Crear el Botón ---

# Definir la posición del botón en la Figura 1 (fig1)
ax_button = fig1.add_axes([0.4, 0.05, 0.2, 0.05])
button = Button(ax_button, 'Pausa ⏸')
button.on_clicked(pause_resume) 

# --- 8. Crear y Ejecutar la Animación ---

# La animación está ligada a la Figura 1
anim = FuncAnimation(fig1, animate, frames=num_frames, interval=50, blit=False, repeat=False) 

# Muestra ambas figuras (ventanas)
plt.show()