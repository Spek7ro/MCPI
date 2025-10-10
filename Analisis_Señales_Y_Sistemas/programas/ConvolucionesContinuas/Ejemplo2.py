import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- 1. Definición de Parámetros de Tiempo ---
# Rango de tiempo para las señales individuales
t_original_start = -0.5
t_original_end = 2.5
muestras_original = 500
t_tau = np.linspace(t_original_start, t_original_end, muestras_original, endpoint=False) # Eje tau para x(tau) y h(t-tau)

# Rango de tiempo para el desplazamiento 't' de h(t-tau)
# Este rango cubre todo el proceso de solapamiento
t_desplazamiento_start = -0.5
t_desplazamiento_end = 2.5
num_frames = 100 # Número de pasos de tiempo en la animación
t_valores_animacion = np.linspace(t_desplazamiento_start, t_desplazamiento_end, num_frames)

dt = t_tau[1] - t_tau[0] # Paso de tiempo para la integración

# --- 2. Definición de las Señales x(tau) y h(tau) ---

# x(tau) = tau, si 0 <= tau <= 1; 0 en caso contrario (Señal Triangular/Rampa)
def x_func(tau):
    return np.where((tau >= 0) & (tau <= 1), tau, 0.0)

# h(tau) = 1, si 0 <= tau <= 1; 0 en caso contrario (Señal Rectangular/Pulso)
def h_func(tau):
    return np.where((tau >= 0) & (tau <= 1), 1.0, 0.0)

# Muestreo de x(tau)
x_tau = x_func(t_tau)

# --- 3. Inicialización de la Gráfica y la Animación ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), gridspec_kw={'height_ratios': [3, 1]})

# Configuración del primer subplot (visualización de la operación)
ax1.set_xlim(t_original_start, t_original_end)
ax1.set_ylim(-0.2, 1.2)
ax1.set_xlabel('$\\tau$')
ax1.set_ylabel('Amplitud')
ax1.set_title('Convolución Animada $y(t) = \\int x(\\tau) h(t-\\tau) d\\tau$')
ax1.grid(True, linestyle='--')

# Plot de x(tau) (fija)
line_x, = ax1.plot(t_tau, x_tau, 'g-', linewidth=2, label='$x(\\tau)$')

# Plot de h(t-tau) (volteada y desplazándose)
line_h_shifted, = ax1.plot(t_tau, np.zeros_like(t_tau), 'r-', linewidth=2, label='$h(t-\\tau)$')

# Plot del producto x(tau) * h(t-tau)
line_product, = ax1.plot(t_tau, np.zeros_like(t_tau), 'm-', linewidth=2, label='$x(\\tau) h(t-\\tau)$')

# Área sombreada del producto (inicialmente una referencia, no un objeto modificado)
# ¡IMPORTANTE! Al inicializar fill_product aquí, lo usamos antes de que la función animate lo reasigne.
# Lo inicializaremos fuera de la función animate, pero será necesario usar global dentro de animate.
fill_product = ax1.fill_between(t_tau, np.zeros_like(t_tau), np.zeros_like(t_tau), color='purple', alpha=0.3, label='Producto Integrado')

ax1.legend()

# Configuración del segundo subplot (resultado de la convolución y(t))
ax2.set_xlim(t_desplazamiento_start, t_desplazamiento_end + (t_original_end - t_original_start)/2 )
ax2.set_ylim(-0.1, 0.6) # Ajusta este rango según el valor máximo de y(t)
ax2.set_xlabel('Tiempo $t$')
ax2.set_ylabel('$y(t)$')
ax2.set_title('Resultado de la Convolución $y(t)$')
ax2.grid(True, linestyle='--')

# Plot de y(t) (se va construyendo)
line_y, = ax2.plot([], [], 'b-', linewidth=2, label='Convolución $y(t)$')
ax2.legend()

plt.tight_layout()

# Almacenar los valores de y(t)
y_valores = []
t_puntos_y = []

# --- 4. Función de Actualización para la Animación (CORREGIDA) ---
def animate(i):
    # Declaración global de las variables que serán modificadas (reasignadas o actualizadas)
    # y_valores y t_puntos_y se usan con .append, por lo que técnicamente no necesitan 'global', 
    # pero no está de más si quieres ser explícito.
    # fill_product DEBE ser global porque lo eliminamos (remove()) y luego lo volvemos a crear (reasignación).
    global y_valores, t_puntos_y, fill_product 
    
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
    # Removemos el objeto fill_between anterior
    fill_product.remove()
    # Creamos un nuevo objeto fill_between y lo reasignamos a la variable global
    fill_product = ax1.fill_between(t_tau, 0, product, where=(product > 0), color='purple', alpha=0.3)
    
    # Actualizar el título con el valor actual de 't'
    ax1.set_title(f'Convolución Animada (t = {current_t:.2f})')
    
    # 5. Actualizar el resultado de la convolución en el segundo subplot (ax2)
    y_valores.append(integral_value)
    t_puntos_y.append(current_t)
    
    line_y.set_data(t_puntos_y, y_valores)
    
    # Retornar los elementos modificados (necesario para blit=True)
    # En este caso, fill_product no se puede retornar directamente ya que es una colección,
    # pero FuncAnimation funciona mejor si retornas todos los objetos que cambian.
    return line_h_shifted, line_product, line_y,

# --- 5. Crear y Ejecutar la Animación ---
# Se recomienda usar blit=False cuando se trabaja con fill_between ya que es difícil de manejar.
anim = FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=False) 


plt.show()
