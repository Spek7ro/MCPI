import numpy as np
import matplotlib.pyplot as plt

def calcular_dft(x):
    N = len(x)
    X = np.zeros(N, dtype=complex) 
    
    for k in range(N):
        suma = complex(0.0, 0.0)
        
        for n in range(N):
            angulo = -2 * np.pi * k * n / N
            exponencial = np.exp(1j * angulo)
            
            suma += x[n] * exponencial
        X[k] = suma
    return X

# Parámetros
N_muestras = 50 # Número total de muestras (período discreto N)
amplitud = 1.0

x_n = np.zeros(N_muestras)
x_n[0 : N_muestras // 2] = amplitud      # Primera mitad (alto)
x_n[N_muestras // 2 : N_muestras] = -amplitud # Segunda mitad (bajo)
n_indices = np.arange(N_muestras)

X_k_manual = calcular_dft(x_n)
X_k_fft = np.fft.fft(x_n)

diferencia = np.max(np.abs(X_k_manual - X_k_fft))
print(f"Diferencia máxima entre cálculo manual y NumPy FFT: {diferencia:.2e}")

magnitud = np.abs(X_k_manual) / N_muestras

# 2. El eje de las frecuencias k:
k_indices = np.arange(N_muestras)

fig, axs = plt.subplots(2, 1, figsize=(10, 8))
fig.suptitle(f'Espectro de Fourier de Tiempo Discreto (DFT) de una Onda Cuadrada (N={N_muestras})', fontsize=16)
plt.subplots_adjust(hspace=0.4)

# --- Subplot 1: Señal en el Dominio del Tiempo Discreto ---
axs[0].stem(n_indices, x_n, linefmt='b-', markerfmt='bo', basefmt=' ', label=r'$x[n]$')
axs[0].set_title('Dominio del Tiempo Discreto: Onda Cuadrada')
axs[0].set_xlabel('$n$ (Muestras)')
axs[0].set_ylabel('Amplitud')
axs[0].set_ylim(-1.5, 1.5)
axs[0].grid(True, linestyle=':', alpha=0.6)

N_half = N_muestras // 2 + 1 
axs[1].stem(k_indices[:N_half], magnitud[:N_half], linefmt='r-', markerfmt='ro', basefmt=' ', label=r'$|X[k]|/N$')

# Marcar los índices de frecuencia esperados (impares)
expected_indices = np.arange(1, N_half, 2)
axs[1].stem(expected_indices, magnitud[expected_indices], linefmt='g-', markerfmt='go', basefmt=' ', label='Picos Impares (Armónicos)')

axs[1].set_title('Espectro de Amplitud $|X[k]|$ (Normalizado)')
axs[1].set_xlabel('$k$ (Índice Armónico/Frecuencia Discreta)')
axs[1].set_ylabel('Magnitud Normalizada')
axs[1].set_xlim(-0.5, N_half - 0.5)
axs[1].grid(True, linestyle=':', alpha=0.6)
axs[1].legend()

plt.show()

print("\nEl espectro discreto (DFT) muestra picos claros en los armónicos impares (k=1, 3, 5...), confirmando la composición de la onda cuadrada.")