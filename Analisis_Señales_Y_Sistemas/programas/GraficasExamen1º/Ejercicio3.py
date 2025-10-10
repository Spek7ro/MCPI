import numpy as np
import matplotlib.pyplot as plt

# =============================
# Señal continua g(t)
# =============================
t = np.linspace(-8, 12, 2000)

u = lambda x: np.where(x >= 0, 1, 0)

g_t = 3 * (u(t + 4) - u(t - 1)) - 2 * (u(t - 3) - u(t - 10))

plt.figure(figsize=(10, 3))
plt.plot(t, g_t, color='blue', linewidth=2)
plt.title(r"$g(t) = 3\{u(t+4)-u(t-1)\} - 2\{u(t-3)-u(t-10)\}$", color='blue')
plt.xlabel("t")
plt.ylabel("Amplitud")
plt.grid(True, alpha=0.3)
plt.xlim(-8, 12)
plt.ylim(-3, 4)
plt.show()

# =============================
# Señal discreta p[n]
# =============================
n = np.arange(-10, 11)

# Función escalón y delta discretas
u_n = lambda x: np.where(x >= 0, 1, 0)
delta = lambda x: np.where(x == 0, 1, 0)

p_n = (u_n(n + 7) + u_n(n + 1)) + delta(n + 1) + 2 * delta(n) + (u_n(n - 3) + u_n(n - 5))

plt.figure(figsize=(10, 4))
plt.stem(n, p_n, basefmt=" ", linefmt='r-', markerfmt='ro')
plt.title(r"$p[n] = \{u[n+7]+u[n+1]\} + \delta[n+1] + 2\delta[n] + \{u[n-3]+u[n-5]\}$", color='red')
plt.xlabel("n")
plt.ylabel("Amplitud")
plt.grid(True, alpha=0.3)
plt.show()
