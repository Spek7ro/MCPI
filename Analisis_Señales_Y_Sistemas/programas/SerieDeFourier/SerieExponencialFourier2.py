import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-2, 2, 1000)
j = 1j

# Definir función del término n-ésimo
def fourier_term(n, t):
    return (2 / (j * n * np.pi)) * (np.exp(j * n * np.pi * t) - np.exp(-j * n * np.pi * t))

n_values = [1, 3, 5, 7, 9, 11]

fig, axes = plt.subplots(3, 2, figsize=(10, 8))
axes = axes.flatten()

for i, n in enumerate(n_values):
    term = np.real(fourier_term(n, t))  # Parte real del término
    axes[i].plot(t, term, label=f"n={n}", color=f"C{i}")
    axes[i].set_title(f"Término n={n}")
    axes[i].set_xlabel("t")
    axes[i].set_ylabel("Re{fₙ(t)}")
    axes[i].grid(True)
    axes[i].legend()

plt.tight_layout()
plt.suptitle("Primeros 6 términos individuales de la serie exponencial de Fourier", fontsize=14, y=1.02)
plt.show()

suma6 = np.zeros_like(t, dtype=complex)
for n in n_values:
    suma6 += fourier_term(n, t)

plt.figure(figsize=(10, 6))
plt.plot(t, np.real(suma6), color='blue', label="Suma de los primeros 6 términos")
plt.title("Suma de los primeros 6 términos de la serie exponencial de Fourier")
plt.xlabel("t")
plt.ylabel("Re{f(t)}")
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
for i, n in enumerate(n_values):
    plt.plot(t, np.real(fourier_term(n, t)), label=f"n={n}")
plt.plot(t, np.real(suma6), label="Suma total (6 términos)", color='black', linewidth=2)
plt.title("Todos los primeros 6 términos + suma total")
plt.xlabel("t")
plt.ylabel("Re{f(t)}")
plt.legend()
plt.grid(True)
plt.show()
