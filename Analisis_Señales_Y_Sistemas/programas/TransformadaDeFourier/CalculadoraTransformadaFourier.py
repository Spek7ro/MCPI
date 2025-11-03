import numpy as np
import matplotlib.pyplot as plt

A = 1.0 
tau_base = 1.0

# Valores de tau a comparar: tau/2, tau/4, tau/1 y 2*tau y tau/32
tau_list = [tau_base / 2, tau_base / 4.0, tau_base / 1, tau_base * 2.0, tau_base / 32.0]

colors = ['red', 'blue', 'green', 'purple', 'yellow']
labels = [r'$\tau/2 = 0.5$', r'$\tau/4 = 0.25$', r'$\tau/1 = 1.0$', r'$2*\tau = 2.0$',  r'$\tau/32 = 0.03125$']

def pulso_rectangular(t, A, tau):
    return np.where(np.abs(t) <= tau / 2.0, A, 0.0)

def transformada_fourier_rect(omega, A, tau):
    x = omega * tau / 2.0
    sinc_no_normalizada = np.where(x != 0, np.sin(x) / x, 1.0)
    return A * tau * sinc_no_normalizada

t = np.linspace(-1.5, 1.5, 500) 
omega = np.linspace(-30 * np.pi, 30 * np.pi, 1000)

fig, axs = plt.subplots(2, 1, figsize=(12, 10))
fig.suptitle(r'Efecto del Ancho del Pulso ($\tau$) en la Transformada de Fourier', fontsize=16)
plt.subplots_adjust(hspace=0.4)

for i, tau in enumerate(tau_list):
    color = colors[i]
    label = labels[i]
    f_t = pulso_rectangular(t, A, tau)
    F_omega = transformada_fourier_rect(omega, A, tau)
    axs[0].plot(t, f_t, color=color, linewidth=2, label=label)
    axs[1].plot(omega, F_omega, color=color, linewidth=2, label=label)    
    primer_cero = 2 * np.pi / tau
    axs[1].axvline(primer_cero, color=color, linestyle=':', linewidth=0.8, alpha=0.5)
    axs[1].axvline(-primer_cero, color=color, linestyle=':', linewidth=0.8, alpha=0.5)

# --- Estilo del Subplot de Tiempo ---
axs[0].set_title('Dominio del Tiempo: Pulso Rectangular $f(t)$', fontsize=14)
axs[0].set_xlabel('$t$ (Tiempo)')
axs[0].set_ylabel('$f(t)$ (Amplitud)')
axs[0].set_ylim(-0.1, A + 0.1)
axs[0].axhline(0, color='gray', linestyle='--', linewidth=0.5)
axs[0].axvline(0, color='gray', linestyle='--', linewidth=0.5)
axs[0].grid(True, linestyle=':', alpha=0.6)
axs[0].legend(title=r'Duración ($\tau$)', loc='upper right')

# --- Estilo del Subplot de Frecuencia ---
axs[1].set_title('Dominio de la Frecuencia: Transformada $|F(\omega)|$', fontsize=14)
axs[1].set_xlabel(r'$\omega$ (Frecuencia Angular)')
axs[1].set_ylabel(r'$F(\omega)$ (Magnitud)')
axs[1].axhline(0, color='black', linewidth=0.8)
axs[1].grid(True, linestyle=':', alpha=0.6)
axs[1].set_xlim(omega[0], omega[-1])
axs[1].legend(title=r'Pulso ($\tau$)', loc='upper right')
plt.show()