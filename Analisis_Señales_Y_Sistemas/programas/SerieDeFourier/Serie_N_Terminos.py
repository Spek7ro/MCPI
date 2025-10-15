import numpy as np
import matplotlib.pyplot as plt

def calcular_serie_fourier(t, num_terminos):
    A = 4 / np.pi 
    f_t = np.zeros_like(t)
    for k in range(1, num_terminos + 1):
        n = 2 * k - 1 
        termino = (A / n) * np.sin(n * np.pi * t)
        f_t += termino
    return f_t

while True:
    try:
        N = int(input("Ingrese el número de términos impares (N) a sumar: "))
        if N > 0:
            break
        else:
            print("Por favor, ingrese un número entero positivo.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")

t = np.linspace(-2, 2, 500) 

resultado_serie = calcular_serie_fourier(t, N)
plt.figure(figsize=(10, 6))
plt.plot(t, resultado_serie, 
         label=f'Suma de {N} términos impares', 
         color='blue', 
         linewidth=2)

def onda_cuadrada(t):
    return np.where((t % 2 >= -1) & (t % 2 < 0), -1, 1)

# plt.plot(t, onda_cuadrada(t), 'r--', label='Función Original (Onda Cuadrada)', alpha=0.6) # Descomentar para ver la comparación

plt.title(f'Aproximación de la Serie de Fourier con N = {N} Términos', fontsize=15)
# plt.suptitle(r'$f(t) \approx \frac{4}{\pi} \sum_{k=1}^{N} \frac{1}{2k-1} \sin((2k-1)\pi t)$', fontsize=12)

plt.xlabel('$t$ (Tiempo)')
plt.ylabel('Amplitud $f(t)$')
plt.ylim(-2, 2) 
plt.grid(True, linestyle='--', alpha=0.6)
plt.axhline(0, color='black', linewidth=0.8)
plt.legend(loc='upper right')
plt.show()
