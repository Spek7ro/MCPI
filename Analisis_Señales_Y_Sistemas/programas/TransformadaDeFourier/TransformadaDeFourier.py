import numpy as np
import matplotlib.pyplot as plt

# Amplitud del pulso (A)
A = 1.0
# Duración total del pulso (tau)
tau = 1.0

def pulso_rectangular(t, A, tau):
    return np.where(np.abs(t) <= tau / 2.0, A, 0.0)

def transformada_fourier_rect(omega, A, tau):
    x = omega * tau / 2.0
    sinc_no_normalizada = np.where(x != 0, np.sin(x) / x, 1.0)
    
    return A * tau * sinc_no_normalizada

# Dominio del tiempo (t) para el pulso
t = np.linspace(-3 * tau, 3 * tau, 500)
omega = np.linspace(-15 * np.pi, 15 * np.pi, 500)

# Calcular las funciones
f_t = pulso_rectangular(t, A, tau)
F_omega = transformada_fourier_rect(omega, A, tau)

fig, axs = plt.subplots(2, 1, figsize=(10, 8))
fig.suptitle(f'Transformada de Fourier del Pulso Rectangular (A={A}, $\\tau={tau}$)', fontsize=16)
plt.subplots_adjust(hspace=0.4)

axs[0].plot(t, f_t, 'b', linewidth=2, label=r'$f(t) = \text{rect}(t/\tau)$')
axs[0].set_title('Dominio del Tiempo: Pulso Rectangular', fontsize=12)
axs[0].set_xlabel('$t$ (Tiempo)')
axs[0].set_ylabel('$f(t)$ (Amplitud)')
axs[0].set_ylim(-0.1, A + 0.1)
axs[0].axhline(0, color='gray', linestyle='--', linewidth=0.5)
axs[0].axvline(0, color='gray', linestyle='--', linewidth=0.5)
axs[0].grid(True, linestyle=':', alpha=0.6)

axs[1].plot(omega, F_omega, 'r', linewidth=2, label=r'$F(\omega) = A\tau \cdot \text{sinc}(\omega\tau/2)$')

cero_indices = np.arange(1, 5) * 2 * np.pi / tau
for cero in cero_indices:
    axs[1].axvline(cero, color='gray', linestyle=':', linewidth=0.8)
    axs[1].axvline(-cero, color='gray', linestyle=':', linewidth=0.8)

axs[1].set_title('Dominio de la Frecuencia: Función Sinc', fontsize=12)
axs[1].set_xlabel(r'$\omega$ (Frecuencia Angular)')
axs[1].set_ylabel(r'$F(\omega)$ (Magnitud)')
axs[1].axhline(0, color='black', linewidth=0.8)
axs[1].grid(True, linestyle=':', alpha=0.6)
axs[1].set_xlim(omega[0], omega[-1])
axs[1].legend()
plt.show()
