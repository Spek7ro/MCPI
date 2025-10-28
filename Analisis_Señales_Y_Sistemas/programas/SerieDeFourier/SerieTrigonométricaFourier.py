import numpy as np
import matplotlib.pyplot as plt

T = 2.0
omega_0 = np.pi

# Coeficientes Analíticos:
# a0/2 = 4/3
# an = 4 / (n^2 * pi^2)
# bn = -4 / (n * pi)

N_max = 6 
t = np.linspace(-4, 6, 800) 


def serie_fourier_t_squared(t, N_terms):
    """Calcula la aproximación de la Serie de Fourier para f(t)=t^2 en (0, 2)."""
    
    
    f_t = (T**2 / 3) / 2 # A0 = 4/3
    
    # Suma de armónicos
    for n in range(1, N_terms + 1):
        # Coeficientes analíticos
        an = 4.0 / (n**2 * np.pi**2)
        bn = -4.0 / (n * np.pi)
        
        # Armónico (an*cos(n*w0*t) + bn*sin(n*w0*t))
        termino = an * np.cos(n * omega_0 * t) + bn * np.sin(n * omega_0 * t)
        f_t += termino
        
    return f_t

def funcion_original_periodica(t, T):
    """
    Representa la función original f(t) = t^2 en (0, 2) extendida periódicamente.
    """
    # Mapear t al rango [0, T) usando la operación módulo
    t_periodo = np.fmod(t, T)
    # Ajustar para números negativos (el módulo en Python puede dar resultados negativos)
    t_periodo = np.where(t_periodo < 0, t_periodo + T, t_periodo)
    
    return t_periodo**2


fig1, axs1 = plt.subplots(3, 2, figsize=(14, 10))
fig1.suptitle(r'Primeros 6 Términos Individuales de la Serie de Fourier para $f(t)=t^2$', fontsize=16)
plt.subplots_adjust(hspace=0.5)
axs_flat = axs1.flatten()
f_t_aproximacion = (T**2 / 3) / 2 # Inicializar con el término constante 4/3

for i, n in enumerate(range(1, N_max + 1)):
    ax = axs_flat[i]
    
    # Coeficientes
    an = 4.0 / (n**2 * np.pi**2)
    bn = -4.0 / (n * np.pi)
    
    # Calcular el término armónico
    termino = an * np.cos(n * omega_0 * t) + bn * np.sin(n * omega_0 * t)
    
    # El primer término graficado debe incluir el término constante A0 para tener sentido físico
    if i == 0:
        termino_con_a0 = termino + (T**2 / 3) / 2
        ax.plot(t, termino_con_a0, label=f'n={n}', color='C0')
        titulo = f'Término 1 (n=1) + A0 = 4/3'
    else:
        ax.plot(t, termino, label=f'n={n}', color=f'C{i}')
        titulo = f'Término {i+1} (n={n})'

    ax.set_title(titulo, fontsize=10)
    ax.set_xlabel('$t$')
    ax.set_ylabel('Amplitud')
    ax.grid(True, linestyle='--', alpha=0.7)

plt.show()

fig2, ax2 = plt.subplots(figsize=(10, 6))

# Calcular la aproximación
aproximacion = serie_fourier_t_squared(t, N_max)

# Calcular la función original periódica
original = funcion_original_periodica(t, T)

# Gráfica de la función original (parábola extendida)
ax2.plot(t, original, color='blue', linewidth=2.5, linestyle='-', 
         label=r'Función Original $f(t)=t^2$ (Periódica)')

ax2.plot(t, aproximacion, color='red', linewidth=1.5, linestyle='--', 
         label=f'Aproximación de Fourier (Suma de {N_max} términos)')

formula_term = r'$A_0 + \sum_{n=1}^{6} \left[ \frac{4}{n^2 \pi^2} \cos(n\pi t) - \frac{4}{n\pi} \sin(n\pi t) \right]$'
ax2.set_title(f'Gráfica de la Suma de los Primeros {N_max} Términos\n' + formula_term, fontsize=14)
ax2.set_xlabel('$t$ (Tiempo)')
ax2.set_ylabel('Amplitud $f(t)$')
ax2.set_ylim(-1, 5) 
ax2.grid(True, linestyle='--', alpha=0.6)
ax2.legend()

plt.show()

fig3, ax3 = plt.subplots(figsize=(10, 6))
ax3.axhline((T**2 / 3) / 2, color='gray', linestyle=':', label=r'Término Constante ($A_0 = 4/3$)')

for i, n in enumerate(range(1, N_max + 1)):
    # Coeficientes
    an = 4.0 / (n**2 * np.pi**2)
    bn = -4.0 / (n * np.pi)
    
    # Calcular el término armónico
    termino = an * np.cos(n * omega_0 * t) + bn * np.sin(n * omega_0 * t)
    
    # Graficar el término armónico (sin el término constante A0)
    ax3.plot(t, termino, label=f'Armónico n={n}', linewidth=1.5)

ax3.set_title(f'Superposición de los Primeros {N_max} Armónicos Individuales', fontsize=15)
ax3.set_xlabel('$t$ (Tiempo)')
ax3.set_ylabel('Amplitud del Término')
ax3.set_ylim(-1.5, 1.5) 
ax3.grid(True, linestyle='--', alpha=0.6)
ax3.legend(loc='upper right', ncol=2, fontsize='small')

plt.show()
