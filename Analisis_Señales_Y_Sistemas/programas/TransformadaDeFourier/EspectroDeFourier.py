import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq


Fs = 1000       # Frecuencia de muestreo (muestras por segundo)
T = 1 / Fs      # Período de muestreo (tiempo entre muestras)
L = 1500        # Longitud de la señal (número total de muestras)
t = np.arange(L) * T # Vector de tiempo

# Frecuencias de las componentes de la señal
f1 = 50.0       # Componente principal (50 Hz)
f2 = 120.0      # Componente armónica (120 Hz)

# Crear la señal f(t) = sin(2*pi*f1*t) + 0.5*sin(2*pi*f2*t) + ruido
S = 0.7 * np.sin(2 * np.pi * f1 * t) + \
    0.5 * np.sin(2 * np.pi * f2 * t)

ruido = 0.2 * np.random.randn(L)
f_t = S + ruido

# 1. Aplicar la Transformada Rápida de Fourier (FFT)
# El resultado es un vector de números complejos F(k)
F_k = fft(f_t)


f_eje = fftfreq(L, T)

P1 = np.abs(F_k / L)
P1 = 2 * P1
P1[0] = P1[0] / 2 # Ajuste para el componente DC (f=0)


n_unilateral = L // 2
P1_unilateral = P1[0:n_unilateral]
f_eje_unilateral = f_eje[0:n_unilateral]


fig, axs = plt.subplots(2, 1, figsize=(12, 8))
fig.suptitle('Cálculo del Espectro de Fourier (FFT)', fontsize=16)
plt.subplots_adjust(hspace=0.4)

# --- Subplot 1: Señal en el Dominio del Tiempo ---
axs[0].plot(t, f_t, color='blue', linewidth=1.5, label='Señal con Ruido')
axs[0].set_title('Dominio del Tiempo: Señal Muestreada')
axs[0].set_xlabel('Tiempo (s)')
axs[0].set_ylabel('Amplitud')
axs[0].grid(True, linestyle=':', alpha=0.6)
axs[0].set_xlim(0, 0.1) # Mostrar solo los primeros 0.1 segundos

# --- Subplot 2: Espectro de Amplitud (Magnitud) ---
# Usamos el espectro unilateral (frecuencias positivas)
axs[1].stem(f_eje_unilateral, P1_unilateral, basefmt='gray', linefmt='red', markerfmt='ro', label='Magnitud $|F(f)|$')
axs[1].set_title('Espectro de Fourier (FFT)')
axs[1].set_xlabel('Frecuencia (Hz)')
axs[1].set_ylabel('Magnitud de Amplitud')
axs[1].grid(True, linestyle=':', alpha=0.6)
axs[1].set_xlim(0, Fs / 2) # Límite en la frecuencia de Nyquist
axs[1].set_ylim(0, 1.0) # Ajuste para mejor visualización de picos

plt.show()

print("\n--- Análisis del Espectro ---")
print(f"Las componentes de frecuencia detectadas se encuentran en:")
# Encontrar los índices de los picos más grandes (excepto el ruido)
indices_picos = np.argsort(P1_unilateral)[-3:] # Las 3 magnitudes más grandes
frecuencias_detectadas = f_eje_unilateral[indices_picos]
magnitudes_detectadas = P1_unilateral[indices_picos]

# Filtrar solo picos significativos (por ejemplo, magnitud > 0.1)
for f_peak, mag in zip(frecuencias_detectadas, magnitudes_detectadas):
    if mag > 0.1:
        print(f"Pico en {f_peak:.2f} Hz con Magnitud {mag:.3f}")
    
print("\nEl espectro de Fourier muestra claramente los dos picos de frecuencia inyectados (50 Hz y 120 Hz).")