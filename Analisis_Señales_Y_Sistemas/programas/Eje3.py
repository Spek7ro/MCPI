import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button 

t_original_start = -0.5
t_original_end = 2.5
muestras_original = 500
t_tau = np.linspace(t_original_start, t_original_end, muestras_original, endpoint=False) 

t_desplazamiento_start = -0.5
t_desplazamiento_end = 2.5
num_frames = 100
t_valores_animacion = np.linspace(t_desplazamiento_start, t_desplazamiento_end, num_frames)

dt = t_tau[1] - t_tau[0] 

# 2. Definición de las Señales x(tau) y h(tau)

def x_func(tau):
    return np.where((tau >= 0) & (tau <= 1), tau, 0.0)

def h_func(tau):
    return np.where((tau >= 0) & (tau <= 1), 1.0, 0.0)

x_tau = x_func(t_tau)

# 3. Inicialización de la Gráfica y la Animación 
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 9), gridspec_kw={'height_ratios': [3, 1]})
plt.subplots_adjust(bottom=0.15)

# Configuración del primer subplot (visualización de la operación)
ax1.set_xlim(t_original_start, t_original_end)
ax1.set_ylim(-0.2, 1.2)
ax1.set_xlabel('$\\tau$')
ax1.set_ylabel('Amplitud')
ax1.set_title('Convolución Animada $y(t) = \\int x(\\tau) h(t-\\tau) d\\tau$')
ax1.grid(True, linestyle='--')

line_x, = ax1.plot(t_tau, x_tau, 'g-', linewidth=2, label='$x(\\tau)$')
line_h_shifted, = ax1.plot(t_tau, np.zeros_like(t_tau), 'r-', linewidth=2, label='$h(t-\\tau)$')
line_product, = ax1.plot(t_tau, np.zeros_like(t_tau), 'm-', linewidth=2, label='$x(\\tau) h(t-\\tau)$')

# Área sombreada del producto (global para poder eliminar y recrear)
fill_product = ax1.fill_between(t_tau, np.zeros_like(t_tau), np.zeros_like(t_tau), color='yellow', alpha=0.3, label='Producto Integrado')

ax1.legend()

# Configuración del segundo subplot (resultado de la convolución y(t))
ax2.set_xlim(t_desplazamiento_start, t_desplazamiento_end + (t_original_end - t_original_start)/2 )
ax2.set_ylim(-0.1, 0.6) 
ax2.set_xlabel('Tiempo $t$')
ax2.set_ylabel('$y(t)$')
ax2.set_title('Resultado de la Convolución $y(t)$: $x(t)$ y $h(t)$') 
ax2.grid(True, linestyle='--')

line_y, = ax2.plot([], [], 'b-', linewidth=2, label='Convolución $y(t)$')
ax2.legend()

plt.tight_layout(rect=[0, 0.15, 1, 1]) 

# Almacenar los valores de y(t) 
y_valores = []
t_puntos_y = []

is_paused = False

#  5. Función de Actualización para la Animación ---
def animate(i):
    # Declaración global de las variables que serán modificadas
    global y_valores, t_puntos_y, fill_product, is_paused

    # Si la animación está pausada, no hacer nada y devolver los objetos inmodificados.
    if is_paused:
        return line_h_shifted, line_product, line_y,

    current_t = t_valores_animacion[i]
    
    # 1. Volteo y Desplazamiento
    h_shifted_tau = h_func(current_t - t_tau) 
    
    # 2. Producto de las señales
    product = x_tau * h_shifted_tau
    
    # 3. Integral (Convolución para el tiempo actual 't')
    integral_value = np.sum(product) * dt
    
    # 4. Actualizar el primer subplot (ax1)
    line_h_shifted.set_ydata(h_shifted_tau)
    line_product.set_ydata(product)
    
    # Actualizar el área sombreada
    fill_product.remove()
    fill_product = ax1.fill_between(t_tau, 0, product, where=(product > 0), color='yellow', alpha=0.3)
    
    # Actualizar el título con el valor actual de 't'
    ax1.set_title(f'Convolución Animada (t = {current_t:.2f})')
    
    # 5. Actualizar el resultado de la convolución en el segundo subplot (ax2)
    y_valores.append(integral_value)
    t_puntos_y.append(current_t)
    
    line_y.set_data(t_puntos_y, y_valores)
    
    return line_h_shifted, line_product, line_y,

# 6. Función de Pausa/Reanudar ---
def pause_resume(event):
    global is_paused
    is_paused = not is_paused 
    
    if is_paused:
        anim.event_source.stop()
        button.label.set_text('Reanudar ▶')
        print(f"Animación pausada en t = {t_puntos_y[-1]:.2f}")
    else:
        # Reanudar la animación
        anim.event_source.start()
        button.label.set_text('Pausa ⏸')
        print("Animación reanudada.")

# Crear el Botón de pausa 
ax_button = fig.add_axes([0.4, 0.05, 0.2, 0.05])
button = Button(ax_button, 'Pausa ⏸')
button.on_clicked(pause_resume) # Conectar la función al evento de clic

anim = FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=False, repeat=False) 
plt.show()
print("Terminado...")