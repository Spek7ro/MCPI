# =========================================
# BLOQUE 1 — Imports + Descarga y Carga del Dataset (KaggleHub)
# =========================================
# Requiere: pip install kagglehub
# Dataset: https://www.kaggle.com/datasets/yasserh/housing-prices-dataset

# !pip install kagglehub  # <-- descomenta si hace falta instalar

import kagglehub
import pandas as pd

# Descargar carpeta del dataset
data_path = kagglehub.dataset_download("yasserh/housing-prices-dataset")
print("Ruta de descarga:", data_path)

# Cargar CSV principal
df = pd.read_csv(f"{data_path}/Housing.csv")
print("Dimensiones:", df.shape)
print(df.head(3))

# =========================================
# BLOQUE 2 — EDA rápida (estructura, nulos, stats + 2 gráficas)
# =========================================
import matplotlib.pyplot as plt

print("Tipos de datos:\n", df.dtypes)
print("\nNulos por columna:\n", df.isnull().sum())
print("\nEstadísticas numéricas:\n", df.describe())

# Histograma de precios
# plt.hist(df['price'], bins=30)
fig, axs = plt.subplots(1, 2, figsize=(12, 6))
axs[0].hist(df['price'], bins=30)
plt.title('Distribución de precios')
plt.xlabel('Precio (INR)')
plt.ylabel('Frecuencia')

# Dispersión precio vs área
# plt.figure()
# plt.scatter(df['area'], df['price'], alpha=0.6)
axs[1].scatter(df['area'], df['price'], alpha=0.6)
plt.title('Precio vs Área')
plt.xlabel('Área (sqft)')
plt.ylabel('Precio (INR)')

# =========================================
# BLOQUE 3 — Preprocesamiento (dummies + escalado numérico) y Split
# =========================================
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Separar target
y = df['price']
X = df.drop(columns=['price'])

# One-Hot Encoding (drop_first para evitar multicolinealidad perfecta)
X = pd.get_dummies(X, drop_first=True)

# Escalar solo columnas numéricas originales
numeric_feats = ['area', 'bedrooms', 'bathrooms', 'stories', 'parking']
scaler = StandardScaler()
X[numeric_feats] = scaler.fit_transform(X[numeric_feats])

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=0
)

print("X_train:", X_train.shape, "X_test:", X_test.shape)
print("Columnas de X:", list(X.columns))

# =========================================
# BLOQUE 4 — Regresión Lineal (OLS): entrenamiento, evaluación y gráfico
# =========================================
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt

lin = LinearRegression().fit(X_train, y_train)
y_pred_lin = lin.predict(X_test)

def report_metrics(name, yt, yp):
    r2 = r2_score(yt, yp)
    mae = mean_absolute_error(yt, yp)
    rmse = mean_squared_error(yt, yp, squared=False)
    print(f"{name} | R2={r2:.3f}  MAE={mae:.0f}  RMSE={rmse:.0f}")

report_metrics("Linear (OLS)", y_test, y_pred_lin)

# Predicho vs Real
plt.figure()
plt.scatter(y_test, y_pred_lin, alpha=0.6, label='OLS')
mn, mx = min(y_test.min(), y_pred_lin.min()), max(y_test.max(), y_pred_lin.max())
plt.plot([mn, mx], [mn, mx], 'k--', label='Ideal')
plt.xlabel('Real (INR)')
plt.ylabel('Predicho (INR)')
plt.title('Predicción vs Real — OLS')
plt.legend()
plt.show()

# Coeficientes (ordenados por |peso|)
coefs_lin = pd.Series(lin.coef_, index=X.columns).sort_values(key=np.abs, ascending=False)
print("\nTop 10 coeficientes OLS (por magnitud absoluta):\n", coefs_lin.head(10))

# =========================================
# BLOQUE 5 — Ridge: baseline (α=1.0), validación de α y reentrenamiento
# =========================================
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

# Baseline
ridge = Ridge(alpha=1.0).fit(X_train, y_train)
y_pred_ridge = ridge.predict(X_test)
report_metrics("Ridge (alpha=1.0)", y_test, y_pred_ridge)

# Búsqueda simple de alpha con CV
alphas = [0.01, 0.1, 1, 10, 100]
cv_means = []
cv_stds = []

for a in alphas:
    mdl = Ridge(alpha=a)
    scores = cross_val_score(mdl, X_train, y_train, cv=5, scoring='r2')
    cv_means.append(scores.mean())
    cv_stds.append(scores.std())
    print(f"alpha={a:>6}  R2-CV={scores.mean():.3f} ± {scores.std():.3f}")

# Curva de validación
plt.figure()
plt.plot(alphas, cv_means, marker='o')
plt.xscale('log')
plt.xlabel('alpha')
plt.ylabel('R2 (CV)')
plt.title('Validación Ridge: alpha vs R2')
plt.show()

# Entrenar con el mejor alpha (máximo R2-CV)
best_alpha = alphas[int(np.argmax(cv_means))]
ridge_best = Ridge(alpha=best_alpha).fit(X_train, y_train)
y_pred_ridge_best = ridge_best.predict(X_test)
report_metrics(f"Ridge (alpha={best_alpha})", y_test, y_pred_ridge_best)

# =========================================
# BLOQUE 6 — Lasso: LassoCV para elegir α, evaluación y selección de variables
# =========================================
from sklearn.linear_model import LassoCV, Lasso

# LassoCV para seleccionar alpha (con escalado ya aplicado)
lasso_cv = LassoCV(cv=5, random_state=0, n_alphas=100, max_iter=20000)
lasso_cv.fit(X_train, y_train)
print("Alpha óptimo (LassoCV):", lasso_cv.alpha_)

# Reentrenar Lasso con alpha óptimo
lasso_best = Lasso(alpha=lasso_cv.alpha_, max_iter=20000).fit(X_train, y_train)
y_pred_lasso = lasso_best.predict(X_test)
report_metrics("Lasso (alpha óptimo)", y_test, y_pred_lasso)

# Coeficientes no-cero (selección de variables)
coefs_lasso = pd.Series(lasso_best.coef_, index=X.columns)
non_zero = coefs_lasso[coefs_lasso != 0].sort_values(key=np.abs, ascending=False)
print("\nVariables seleccionadas por Lasso (coef != 0):\n", non_zero)

# (Opcional) Conteo de coeficientes en cero
print("Coeficientes a cero en Lasso:", int((coefs_lasso == 0).sum()))

# =========================================
# BLOQUE 7 — Comparativa de coeficientes (OLS vs Ridge* vs Lasso*)
# *Usa el mejor alpha encontrado arriba
# =========================================
import numpy as np

# Asegúrate de haber ejecutado antes: lin, ridge_best, lasso_best
coefs_df = pd.DataFrame({
    'OLS': pd.Series(lin.coef_, index=X.columns),
    f'Ridge_{getattr(ridge_best, "alpha", 1.0)}': pd.Series(ridge_best.coef_, index=X.columns),
    f'Lasso_{getattr(lasso_best, "alpha", 1.0)}': pd.Series(lasso_best.coef_, index=X.columns),
})

# Orden por importancia OLS (|coef|)
order = coefs_df['OLS'].abs().sort_values(ascending=False).index
coefs_df = coefs_df.loc[order]

print("Resumen de coeficientes (primeras 15 filas):\n", coefs_df.head(15))

# =========================================
# BLOQUE 8 — Guardar modelo y scaler + Ejemplo de inferencia
# =========================================
import joblib
import numpy as np

# Elige el "mejor" modelo (por ejemplo, el Ridge con alpha óptimo)
best_model = ridge_best  # cámbialo a lasso_best o lin si lo prefieres

# Guardar modelo y scaler (para reusar en producción)
joblib.dump(best_model, "modelo_precio_vivienda.pkl")
joblib.dump(scaler, "scaler_numeric.pkl")
print("Modelos guardados: modelo_precio_vivienda.pkl, scaler_numeric.pkl")

# Ejemplo de inferencia con una fila del test
x_example = X_test.iloc[[0]].copy()
y_true = y_test.iloc[0]
y_pred = best_model.predict(x_example)[0]
print("Precio real:", y_true)
print("Predicción :", y_pred)

# Si necesitas preprocesar un nuevo registro crudo:
# 1) Crear DataFrame con mismas columnas que X (incluyendo dummies faltantes)
# 2) Aplicar scaler SOLO a numeric_feats
# 3) Llamar best_model.predict(new_X_preprocesado)

# =========================================
# BLOQUE 9 — (Opcional) Pipeline + GridSearchCV para Ridge/Lasso
# =========================================
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge, Lasso

# Ejemplo: rehacer preprocesamiento con ColumnTransformer (desde df original)
y = df['price']
X_raw = df.drop(columns=['price'])

num_cols = ['area', 'bedrooms', 'bathrooms', 'stories', 'parking']
cat_cols = [c for c in X_raw.columns if c not in num_cols]

pre = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), num_cols),
        ('cat', OneHotEncoder(drop='first', handle_unknown='ignore'), cat_cols),
    ],
    remainder='drop'
)

pipe_ridge = Pipeline(steps=[('pre', pre), ('mdl', Ridge())])
param_grid_ridge = {'mdl__alpha': [0.01, 0.1, 1, 10, 100]}
gs_ridge = GridSearchCV(pipe_ridge, param_grid_ridge, cv=5, scoring='r2')
gs_ridge.fit(X_raw, y)
print("Mejor alpha (Ridge, GridSearch):", gs_ridge.best_params_, " R2:", gs_ridge.best_score_)

pipe_lasso = Pipeline(steps=[('pre', pre), ('mdl', Lasso(max_iter=20000))])
param_grid_lasso = {'mdl__alpha': [0.001, 0.01, 0.1, 1, 10]}
gs_lasso = GridSearchCV(pipe_lasso, param_grid_lasso, cv=5, scoring='r2')
gs_lasso.fit(X_raw, y)
print("Mejor alpha (Lasso, GridSearch):", gs_lasso.best_params_, " R2:", gs_lasso.best_score_)
