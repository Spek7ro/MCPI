# Regresión lineal simple con bucles/sumatorias (sin numpy.polyfit / sin sklearn)
import math
import matplotlib.pyplot as plt
import pandas as pd

# Datos
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]
n = len(x)

# 1) Sumas y medias (solo bucles)
sum_x = 0.0
sum_y = 0.0
for i in range(n):
    sum_x += x[i]
    sum_y += y[i]
xbar = sum_x / n
ybar = sum_y / n

# 2) Desviaciones y sumatorias Sxx, Syy, Sxy
Sxx = 0.0
Syy = 0.0
Sxy = 0.0
dx_list, dy_list, dx2_list, dxdy_list = [], [], [], []

for i in range(n):
    dx = x[i] - xbar
    dy = y[i] - ybar
    dx2 = dx * dx
    dxdy = dx * dy
    dx_list.append(dx); dy_list.append(dy)
    dx2_list.append(dx2); dxdy_list.append(dxdy)
    Sxx += dx2; Syy += dy * dy; Sxy += dxdy

# 3) Parámetros
beta1 = Sxy / Sxx
beta0 = ybar - beta1 * xbar

# 4) Predicciones, residuales y métricas
yhat, resid, resid2 = [], [], []
SSE = 0.0
SSR = 0.0
for i in range(n):
    yh = beta0 + beta1 * x[i]
    yhat.append(yh)
    e = y[i] - yh
    resid.append(e)
    ee = e * e
    resid2.append(ee)
    SSE += ee
    SSR += (yh - ybar) * (yh - ybar)

SST = Syy
R2 = 1.0 - SSE / SST
sigma2 = SSE / (n - 2) # varianza residual
se_beta1 = math.sqrt(sigma2 / Sxx)
se_beta0 = math.sqrt(sigma2 * (1.0/n + (xbar * xbar) / Sxx))
t_beta1 = beta1 / se_beta1
t_beta0 = beta0 / se_beta0
r = Sxy / math.sqrt(Sxx * Syy) # Correlacion de Pearson

# 5) Tabla punto a punto para “ver” cada contribución
df = pd.DataFrame({
    'i': list(range(n)),
    'x': x,
    'y': y,
    'x - x̄': dx_list,
    'y - ȳ': dy_list,
    '(x - x̄)^2': dx2_list,
    '(x - x̄)(y - ȳ)': dxdy_list,
    'ŷ = β0 + β1·x': yhat,
    'e = y - ŷ': resid,
    'e^2': resid2,
})
print(df.to_string(index=False))

# 6) Resumen numérico
print(f"\nn = {n}")
print(f"x̄ = {xbar:.6f}, ȳ = {ybar:.6f}")
print(f"Sxx = {Sxx:.6f}, Syy = {Syy:.6f}, Sxy = {Sxy:.6f}")
print(f"Pendiente β1 = {beta1:.6f}")
print(f"Intercepción β0 = {beta0:.6f}")
print(f"Ecuación: ŷ = {beta0:.6f} + {beta1:.6f}·x")
print(f"SSE = {SSE:.6f}, SSR = {SSR:.6f}, SST = {SST:.6f}")
print(f"R^2 = {R2:.6f}")
print(f"σ^2 (var resid) = {sigma2:.6f}")
print(f"SE(β1) = {se_beta1:.6f}, SE(β0) = {se_beta0:.6f}")
print(f"t(β1) = {t_beta1:.6f}, t(β0) = {t_beta0:.6f}")
print(f"r (Pearson) = {r:.6f}")

# 7) Gráfico (sin estilos/colores explícitos)
plt.figure()
plt.scatter(x, y, label='Datos')
plt.plot(x, yhat, label='Recta ajustada')
plt.xlabel("Variable Independiente (X)")
plt.ylabel("Variable Dependiente (Y)")
plt.title("Regresión Lineal Simple — cálculos desde cero (bucles)")
plt.legend()
plt.grid(True)
plt.show()

