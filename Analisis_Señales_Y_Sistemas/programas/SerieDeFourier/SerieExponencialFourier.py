import numpy as np
import matplotlib.pyplot as plt

T = 2.0
omega_0 = np.pi

N_max = 6 
t = np.linspace(-3, 3, 500) 
c0 = 0.0

def obtener_cn_onda_cuadrada(n):
    """
    Calcula el coeficiente cn analítico para la onda cuadrada (-1 a 1, T=2).
    cn = 2 / (j * n * pi) si n es impar
    cn = 0 si n es par
    """
    if n == 0:
        return 0.0
    
    if n % 2 != 0:
        # El término 'j' en Python es 1j
        return 2.0 / (1j * n * np.pi)
    else:
        return 0.0

def serie_exponencial_fourier(t, N_terms):
    """Calcula la aproximación de la Serie Exponencial de Fourier."""

    f_t = c0 * np.ones_like(t, dtype=complex)
    
    for n in range(-N_terms, N_terms + 1):
        if n == 0:
            continue
            
        cn = obtener_cn_onda_cuadrada(n)
        
        # Calcular el término exponencial: cn * exp(j * n * omega_0 * t)
        termino_exponencial = cn * np.exp(1j * n * omega_0 * t)
        
        # Sumar el término. La parte imaginaria debe ser despreciable y tiende a cero.
        f_t += termino_exponencial
        
    # Devolver solo la parte real, ya que la suma de la serie de Fourier es una función real.
    return np.real(f_t)

def onda_cuadrada_original(t, T):
    """Función original periódica (-1 a 1)."""
    t_periodo = np.fmod(t, T)
    t_periodo = np.where(t_periodo < 0, t_periodo + T, t_periodo)
    
    # f(t) = 1 si 0 <= t < 1, f(t) = -1 si 1 <= t < 2
    return np.where((t_periodo >= 0) & (t_periodo < 1), 1.0, -1.0)


fig1, axs1 = plt.subplots(3, 2, figsize=(14, 10))
fig1.suptitle(r'Primeros 6 Armónicos Reales de la Serie Exponencial (Pares $c_n, c_{-n}$)', fontsize=15)
plt.subplots_adjust(hspace=0.5)
axs_flat = axs1.flatten()

# Sumamos n=1, n=3, n=5, n=7, n=9, n=11 (6 armónicos impares)
n_values = [1, 3, 5, 7, 9, 11]

for i, n in enumerate(n_values):
    ax = axs_flat[i]
    
    # Coeficientes para el par n y -n
    cn = obtener_cn_onda_cuadrada(n)
    cn_neg = obtener_cn_onda_cuadrada(-n)
    
    # Armónico real: cn*exp(jnw0t) + c_{-n}*exp(-jnw0t)
    # Esto es equivalente a (4/(n*pi)) * sin(n*pi*t)
    termino_par = cn * np.exp(1j * n * omega_0 * t) + cn_neg * np.exp(-1j * n * omega_0 * t)
    
    ax.plot(t, np.real(termino_par), label=f'n={n}', color=f'C{i}')
    
    # Fórmula del término real (derivada del par exponencial)
    formula_termino = r'$\frac{4}{' + str(n) + r'\pi} \sin(' + str(n) + r'\pi t)$'
    # Arreglo de escape sequence en el f-string
    titulo = f'Término {i+1} ($n=\\pm{n}$)\n' + formula_termino

    ax.set_title(titulo, fontsize=10)
    ax.set_xlabel('$t$')
    ax.set_ylabel('Amplitud')
    ax.grid(True, linestyle='--', alpha=0.7)

plt.show()


fig2, ax2 = plt.subplots(figsize=(10, 6))
N_terms_sum = 11 
aproximacion = serie_exponencial_fourier(t, N_terms_sum)
original = onda_cuadrada_original(t, T)

ax2.plot(t, original, color='blue', linewidth=2.5, linestyle='-', 
         label=r'Onda Cuadrada Original $f(t)$')

# Gráfica de la suma de Fourier
# Arreglo de escape sequence en el f-string
label_sum = f'Aproximación Exponencial (Suma de n=$\\pm$ {N_terms_sum} términos)'
ax2.plot(t, aproximacion, color='red', linewidth=1.5, linestyle='--', 
         label=label_sum)

# Fórmulas en el título para referencia
formula_general = r'$f(t) \approx \sum_{n=-11}^{11} c_n e^{j n \pi t}, \quad c_n = \frac{2}{j n \pi} \text{ (n impar)}$'
ax2.set_title('Gráfica de la Suma de la Serie Exponencial de Fourier', fontsize=15)
ax2.text(0.05, 0.9, formula_general, transform=ax2.transAxes, fontsize=12, verticalalignment='top')
ax2.set_xlabel('$t$ (Tiempo)')
# Arreglo de escape sequence usando raw string r''
ax2.set_ylabel(r'Amplitud $\mathbb{R}\{f(t)\}$')
ax2.set_ylim(-1.5, 1.5) 
ax2.grid(True, linestyle='--', alpha=0.6)
ax2.legend(loc='lower center')

plt.show()

# Generar los índices n y los valores de |cn|
n_indices = np.arange(-N_max, N_max + 1)
cn_magnitudes = [np.abs(obtener_cn_onda_cuadrada(n)) for n in n_indices]
cn_fase = [np.angle(obtener_cn_onda_cuadrada(n)) for n in n_indices]

fig3, (ax3a, ax3b) = plt.subplots(2, 1, figsize=(10, 7), sharex=True)
fig3.suptitle('Espectro de Frecuencia de la Onda Cuadrada (Coeficientes $c_n$)', fontsize=15)
plt.subplots_adjust(hspace=0.3)

# 3a. Magnitud |cn|
ax3a.stem(n_indices, cn_magnitudes, linefmt='b-', markerfmt='bo', basefmt='r-')
ax3a.set_ylabel(r'$|c_n|$ (Magnitud)')
ax3a.grid(True, linestyle='--', alpha=0.6)
ax3a.set_title('Espectro de Amplitud')

# 3b. Fase <cn
ax3b.stem(n_indices, cn_fase, linefmt='g-', markerfmt='go', basefmt='r-')
ax3b.set_xlabel('n (Índice Armónico)')
ax3b.set_ylabel(r'$\angle c_n$ (Fase, radianes)')
ax3b.set_yticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
ax3b.set_yticklabels([r'$-\pi$', r'$-\pi/2$', '0', r'$\pi/2$', r'$\pi$'])
ax3b.grid(True, linestyle='--', alpha=0.6)
ax3b.set_title('Espectro de Fase')

plt.show()

