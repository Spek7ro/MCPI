# Cargar datos
cereal <- read.csv("D:/MCPI/Fundamentos_De_Estadistica/cereal_2.csv")

# Limpiar datos
# Obtener los nombres de las columnas
variables <- colnames(cereal)

for (var in variables) {
  cantidad_na <- sum(is.na(cereal[[var]]))
  cat(var, ":", cantidad_na, "valores NA\n")
}

# No tenemos valores faltntes 
na_summary <- data.frame(
  Variable = variables,
  Cantidad_NA = sapply(variables, function(v) sum(is.na(cereal[[v]])))
)

na_summary <- na_summary[order(-na_summary$Cantidad_NA), ]
print(na_summary)


# Comprobar los primeros dos supuestos del modelo de regresión lineal:
# 1- Linealidad
library(ggplot2)

variables_predictoras <- c("calories.per.serving",
                 "grams.of.protein",
                 "milligrams.of.sodium",
                 "grams.of.dietary.fiber",
                 "grams.of.complex.carbohydrates",
                 "grams.of.sugars",
                 "milligrams.of.potassium")

for (var in variables_predictoras) {
  p <- ggplot(cereal, aes_string(x = var, y = "Rating.of.cereal")) +
    geom_point(color = "steelblue") +
    geom_smooth(method = "lm", se = TRUE, color = "red") +
    labs(title = paste("Supuesto de linealidad:", var, "vs Rating.of.cereal"),
         x = var, y = "Rating.of.cereal") +
    theme_minimal(base_size = 11)
  print(p)
}

# 2- Independencia de los residuos (Durbin–Watson test)
####
# Estadístico cercano a 2 → residuos independientes 
# Valor menor que 2 → autocorrelación positiva
# Valor mayor que 2 → autocorrelación negativa
###

modelo <- lm(Rating.of.cereal ~ calories.per.serving + grams.of.protein +
               milligrams.of.sodium + grams.of.dietary.fiber +
               grams.of.complex.carbohydrates + grams.of.sugars +
               milligrams.of.potassium, data = cereal)

install.packages("lmtest")
library(lmtest)

dwtest(modelo)
# DW = 1.8441, p-value = 0.1972
## los residuos son independientes.
## La hipótesis nula (H₀) del test: no hay autocorrelación.
## Si p-value > 0.05 → no se rechaza H₀ → los residuos son independientes. 
## Si p-value < 0.05 → hay autocorrelación → no cumple el supuesto.

# SUPUESTOS 3 Y 4: HOMOSCEDASTICIDAD Y NORMALIDAD DE LOS RESIDUOS
# # Obtener valores ajustados y residuos
residuos <- residuals(modelo)
predichos <- fitted(modelo)

# Gráfico de dispersión: residuos vs valores ajustados
library(ggplot2)
ggplot(data.frame(predichos, residuos), aes(x = predichos, y = residuos)) +
  geom_point(color = "steelblue") +
  geom_hline(yintercept = 0, color = "red", linetype = "dashed") +
  labs(title = "Supuesto de Homoscedasticidad",
       x = "Valores ajustados",
       y = "Residuos") +
  theme_minimal(base_size = 12)

# Prueba de correlación entre residuos y predichos
cor_test <- cor.test(predichos, residuos, method = "spearman")
print(cor_test)

# Interpretación:
# H0: No hay correlación → Homoscedasticidad (varianza constante)
# H1: Sí hay correlación → Heterocedasticidad (varianza no constante)

if (cor_test$p.value > 0.05) {
  cat("No hay correlación significativa: Se cumple el supuesto de homoscedasticidad.\n")
} else {
  cat("Existe correlación: Se viola el supuesto de homoscedasticidad.\n")
}

ggsave("graficas_linealidad/homoscedasticidad.png", width = 7, height = 5, dpi = 300)

# SUPUESTO DE NORMALIDAD DE LOS RESIDUOS

# Histograma de los residuos
ggplot(data.frame(residuos), aes(x = residuos)) +
  geom_histogram(aes(y = ..density..), bins = 20, fill = "green", color = "black") +
  geom_density(color = "red") +
  labs(title = "Histograma de los residuos",
       x = "Residuos", y = "Densidad") +
  theme_minimal(base_size = 12)
ggsave("graficas_linealidad/histograma_residuos.png", width = 7, height = 5, dpi = 300)

# Gráfico Q–Q (Quantile–Quantile)
qqnorm(residuos, main = "Gráfico Q–Q de los residuos")
qqline(residuos, col = "red", lwd = 2)
dev.copy(png, "graficas_linealidad/qqplot_residuos.png", width = 700, height = 500)
dev.off()

# Gráfico P–P (Probabilidad–Probabilidad)
# Usando función acumulada normal teórica vs empírica
residuos_std <- (residuos - mean(residuos)) / sd(residuos)
pp_data <- data.frame(
  emp = ppoints(length(residuos)),
  theor = pnorm(sort(residuos_std))
)
ggplot(pp_data, aes(x = theor, y = emp)) +
  geom_point(color = "steelblue") +
  geom_abline(slope = 1, intercept = 0, color = "red") +
  labs(title = "Gráfico P–P de los residuos",
       x = "Probabilidad teórica", y = "Probabilidad empírica") +
  theme_minimal(base_size = 12)
ggsave("graficas_linealidad/ppplot_residuos.png", width = 7, height = 5, dpi = 300)

# Prueba de normalidad de Kolmogorov–Smirnov
ks_result <- ks.test(residuos_std, "pnorm")
print(ks_result)

# Interpretación:
# H0: Los residuos se distribuyen normalmente
# H1: Los residuos no se distribuyen normalmente

if (ks_result$p.value > 0.05) {
  cat("P-value > 0.05: Los residuos siguen una distribución normal.\n")
} else {
  cat("p-value < 0.05: Los residuos NO siguen una distribución normal.\n")
}


# Graficos en uno
par(mfrow = c(2, 2))
plot(modelo)
par(mfrow = c(1, 1))

# Calcular la matriz de correlación
sapply(cereal, class)
library(corrplot)

# Selecciona solo las columnas que te interesan
vars_interes <- c(
  "Rating.of.cereal",
  "calories.per.serving",
  "grams.of.protein",
  "milligrams.of.sodium",
  "grams.of.dietary.fiber",
  "grams.of.complex.carbohydrates",
  "grams.of.sugars",
  "milligrams.of.potassium"
)

# Filtrar las columnas del dataframe
cereal_sel <- cereal[, vars_interes]

# Calcular la matriz de correlación
matriz_cor <- cor(cereal_sel, method = "pearson")

# Mostrar la matriz
print(round(matriz_cor, 2))

# Mapa de correlación tipo círculo
corrplot(matriz_cor, method = "circle")

library(ggcorrplot)
ggcorrplot(matriz_cor,
           hc.order = TRUE,
           type = "lower",
           lab = TRUE,
           colors = c("red", "white", "blue"),
           title = "Mapa de correlaciones del cereal",
           ggtheme = ggplot2::theme_minimal)


# R^2: coeficinte de determinacion 0.4752  
modelo2 <- lm(Rating.of.cereal ~ calories.per.serving, data = cereal)
summary(modelo2)
plot(modelo2)
