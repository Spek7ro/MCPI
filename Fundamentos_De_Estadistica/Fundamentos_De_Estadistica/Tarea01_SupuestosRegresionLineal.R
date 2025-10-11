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

par(mfrow = c(2, 2))
plot(modelo)
par(mfrow = c(1, 1))

