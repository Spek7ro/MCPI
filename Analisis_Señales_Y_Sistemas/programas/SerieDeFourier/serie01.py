import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-2, 2, 500) 
n_values = [1, 3, 5, 7, 9, 11]

# Coeficiente A
A = 4 / np.pi 

fig, axs = plt.subplots(3, 2, figsize=(15, 15))
plt.subplots_adjust(hspace=0.4, wspace=0.4) # espaciado entre subplots

f_t_aproximacion = np.zeros_like(t)

axs_flat = axs.flatten()

# Graficas de cada término
for i, n in enumerate(n_values):
    termino = (A / n) * np.sin(n * np.pi * t)
    f_t_aproximacion += termino
    ax = axs_flat[i]
    ax.plot(t, termino, label=f'n={n}', color=f'C{i}') 
    
    ax.set_title(f'Término {i+1} ($n={n}$)')
    ax.set_xlabel('$t$')
    ax.set_ylabel(f'${A:.2f}/n \\sin({n}\\pi t)$')
    ax.grid(True, linestyle='--')
    
fig.suptitle('Primeros 6 Términos de la Serie de Fourier', fontsize=16)

plt.show()

# Gráfica de la suma de los primeros 6 términos
plt.figure(figsize=(8, 4))
plt.plot(t, f_t_aproximacion, color='red', label='Suma de 6 términos')
plt.title('Aproximación de $f(t)$ con la Suma de los Primeros 6 Términos')
plt.xlabel('$t$')
plt.ylabel('$f(t)$')
plt.grid(True, linestyle='--')
plt.axhline(0, color='black', linewidth=0.5)
plt.legend()
plt.show()

# Grafica de todos los términos juntos en una misma gráfica
plt.figure(figsize=(15, 5))
#plt.plot(t, f_t_aproximacion, color='red', label='Suma de 6 términos')
for i, n in enumerate(n_values):
    termino = (A / n) * np.sin(n * np.pi * t)
    plt.plot(t, termino, label=f'n={n}', color=f'C{i}')
plt.title('Aproximación de $f(t)$ con la Suma de los Primeros 6 Términos')
plt.xlabel('$t$')
plt.ylabel('$f(t)$')
plt.grid(True, linestyle='--')
plt.axhline(0, color='black', linewidth=0.5)
plt.legend()
plt.show()
