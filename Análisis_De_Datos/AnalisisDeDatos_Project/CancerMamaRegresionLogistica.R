# 1. cargar los datos
datos_cancer <- read.csv("D:/MCPI/Análisis_De_Datos/AnalisisDeDatos_Project/Datasets/bcdr_d01_features.csv")

# 2. limpiar los datos 
# por cada columna checar si hay NaN´S
# vamos a quitar la columna density por
sum(is.na(datos_cancer$density))

# como quitar una columna?
# paso 1: obtener el nombre y número (posicion) de columnas
colnames(datos_cancer) # me regresa el nombre y la posicion de las columnas

# paso 2: quitar la columna 15 density (operacion vectorial)
# datos_cancer <- datos_cancer[reglones(s), columnas(s)]
datos_cancer <- datos_cancer[ , -15] # todas menos la 15

# la columna classification tienen espacios 
datos_cancer$classification

# vamos a convertir Malign -> 1 y Benign -> 0
# datos_cancer$classification[cuales reglones]
datos_cancer$classification[datos_cancer$classification == " Malign "] <- 1
datos_cancer$classification[datos_cancer$classification == " Benign "] <- 0

class(datos_cancer$classification)

# cambiar la columna classification de caracter a numero
datos_cancer$classification <- as.numeric(datos_cancer$classification)
class(datos_cancer$classification)


##### Etapa de Analis Univariado
# 1. Generar Estadisticos 
# Desviacion Estandar: Que Tenga > 0
# Varianza: Que tenga > 0 
# Rango dinamico (max-min): Buscar valores atipicos (Que esten dentro de un criterio) 

# Crear un data frame vacío donde guardaremos los resultados
install.packages("gt")
library(gt)
library(dplyr)

resultados <- data.frame(
  Variable = character(),
  Desviacion_Estandar = numeric(),
  Varianza = numeric(),
  Rango = numeric(),
  P_Valor = numeric(),
  Accuracy = numeric(),
  stringsAsFactors = FALSE
)

# Obtener los nombres de las variables excepto la última ('classification')
variables <- colnames(datos_cancer)[colnames(datos_cancer) != "classification"]

# Obtener: Desviacion estandar, Varianza, Rango Dinamico, p-valor y Accuracy 
# De cada variable independinte 
# Recorrer cada variable con un ciclo for
for (var in variables) {
  # Verificar si la variable es numérica (para evitar errores con texto o factores)
  if (is.numeric(datos_cancer[[var]])) {
    # Calcular estadísticas básicas
    sd_val <- sd(datos_cancer[[var]])
    var_val <- var(datos_cancer[[var]])
    rango_val <- max(datos_cancer[[var]], na.rm = TRUE) - min(datos_cancer[[var]], na.rm = TRUE)
    
    # -------- Modelo logístico univariado -------- ML
    p_val <- NA
    accuracy_val <- NA
    
    try({
      formulita <- as.formula(paste("classification ~", var))
      modelo <- glm(formula = formulita, data = datos_cancer, family = "binomial")
      resumen <- summary(modelo)
      
      # Verificar si hay coeficiente aparte del intercepto
      if (nrow(coef(resumen)) >= 2) {
        p_val <- coef(resumen)[2, 4]  # p-valor de la variable
      }
      
      # Calcular predicciones y accuracy
      predicciones <- ifelse(predict(modelo, type = "response") > 0.5, 1, 0)
      accuracy_val <- mean(predicciones == datos_cancer$classification, na.rm = TRUE)
      
    }, silent = TRUE)
    
    # Agregar resultados al data.frame
    resultados <- rbind(resultados, data.frame(
      Variable = var,
      Desviacion_Estandar = sd_val,
      Varianza = var_val,
      Rango = rango_val,
      P_Valor = p_val,
      Accuracy = accuracy_val,
      stringsAsFactors = FALSE
    ))
  }
}

options(scipen = 999)  # evitar la notación científica
print(resultados, digits = 4)

### Tabla de resultados:
gt(resultados)

resultados %>%
  gt() %>%
  tab_header(title = md("**Análisis univariado**"),
             subtitle = md("Cáncer de mama"))

resultados %>%
  gt() %>%
  tab_spanner(
    label = "Estadísticos",
    columns = c(Desviacion_Estandar, Varianza, Rango)) %>%
  tab_spanner(
    label = "ML",
    columns = c(P_Valor, Accuracy)
  )

### Otro tipo de tabla
library(gtsummary)
formulita <- as.formula("classification ~ age + t_energ")
modelo <- glm(formula = formulita, data = datos_cancer, family = "binomial")
summary(modelo)
# generate table 
modelo %>%
  tbl_regression()

###### Fin analisis Univariado ######

############# Graficas de distribuciones #########
## Datos Cancer = Rojo
## Datos No Cancer = Azul

datosCancerX <- datos_cancer$t_inf1h[datos_cancer$classification == 1]
datosNoCancerX <- datos_cancer$t_inf1h[datos_cancer$classification == 0]

plot(density(datosCancerX), 
     col="red",
     xlim=c(-0.5, 0.5),
     ylim=c(0,8),
     main="",
     xlab="")
par(new=TRUE)
plot(density(datosNoCancerX),
     col="blue",
     xlim=c(-0.5, 0.5),
     ylim=c(0,8),
     main="t_inf1h Cancer vs No Cancer",
     xlab="")
legend("topright", cex = 0.7, 
       c("Cancer", "No Cancer"),
       fill=c("red", "blue"))

# Segunda grafica:s_elongation
datosCancerX <- datos_cancer$s_elongation[datos_cancer$classification == 1]
datosNoCancerX <- datos_cancer$s_elongation[datos_cancer$classification == 0]

plot(density(datosCancerX), 
     col="red",
     xlim=c(-1, 2),
     ylim=c(0,5),
     main="",
     xlab="")
par(new=TRUE)
plot(density(datosNoCancerX),
     col="blue",
     xlim=c(-1, 2),
     ylim=c(0,5),
     main="s_elongation Cancer vs No Cancer",
     xlab="")
legend("topright", cex = 0.7, 
       c("Cancer", "No Cancer"),
       fill=c("red", "blue"))

# sacar graficas desde age hasta t_inf2h
datosCancerX <- datos_cancer$age[datos_cancer$classification == 1]
datosNoCancerX <- datos_cancer$age[datos_cancer$classification == 0]

plot(density(datosCancerX), 
     col="red",
     xlim=c(-10, 5),
     ylim=c(0,5),
     main="",
     xlab="")
par(new=TRUE)
plot(density(datosNoCancerX),
     col="blue",
     xlim=c(-10, 5),
     ylim=c(0,5),
     main="Age Cancer vs No Cancer",
     xlab="")
legend("topright", cex = 0.7, 
       c("Cancer", "No Cancer"),
       fill=c("red", "blue"))

# i_mean
datosCancerX <- datos_cancer$i_mean[datos_cancer$classification == 1]
datosNoCancerX <- datos_cancer$i_mean[datos_cancer$classification == 0]

plot(density(datosCancerX), 
     col="red",
     xlim=c(-1, 2),
     ylim=c(0,5),
     main="",
     xlab="")
par(new=TRUE)
plot(density(datosNoCancerX),
     col="blue",
     xlim=c(-1, 2),
     ylim=c(0,5),
     main="	i_mean Cancer vs No Cancer",
     xlab="")
legend("topright", cex = 0.7, 
       c("Cancer", "No Cancer"),
       fill=c("red", "blue"))

# para las de mas variaables 
datosCancerX <- datos_cancer$s_circularity[datos_cancer$classification == 1]
datosNoCancerX <- datos_cancer$s_circularity[datos_cancer$classification == 0]

plot(density(datosCancerX), 
     col="red",
     xlim=c(-1, 2),
     ylim=c(0,3),
     main="",
     xlab="")
par(new=TRUE)
plot(density(datosNoCancerX),
     col="blue",
     xlim=c(-1, 2),
     ylim=c(0,3),
     main="s_circularity Cancer vs No Cancer",
     xlab="")
legend("topright", cex = 0.7, 
       c("Cancer", "No Cancer"),
       fill=c("red", "blue"))

# Using Small multiple
library(ggplot2)

var <- "i_kurtosis"

ggplot(datos_cancer, aes_string(x = var, fill = "classification")) +
  geom_density(alpha = 0.6, adjust = 1.5) +
  facet_wrap(~classification) +
  theme_minimal() +  
  theme(
    legend.position = "none",
    panel.spacing = unit(0.3, "lines"),
    axis.ticks.x = element_blank()
  ) +
  labs(
    title = paste("Distribución de densidad para", var),
    x = var,
    y = "Densidad"
  )

####### Fin garficas


############## 3. Crear un modelo: Regresion logistica #############
# Seleccionar que queremos predecir en funcion de que (seleccion de caracteristicas)
# usaremos age, i_mean y i_std_dev
datos_cancer$s_y_center_mass
formulita <- as.formula("classification ~ age")
modelo <- glm(formula = formulita, data = datos_cancer, family = "binomial")
summary(modelo)

# Obtener las prediccines sobre el conjunto de datos
predicciones <- predict(modelo, newdata = datos_cancer, type = "response")
predicciones

# Crear la tabla de comparaciones entre lo real y lo predicho
tablita <- data.frame(Original = datos_cancer$classification, 
                      prediccionesModelo = predicciones)

# Binarizar pero de forma vectorial los datos de tablita (prediccionesModelo) 
tablita$prediccionesModelo[tablita$prediccionesModelo < 0.5] <- 0
tablita$prediccionesModelo[tablita$prediccionesModelo >= 0.5] <- 1

# Calcular las metricas (Accuracy)
accuracy <- sum(tablita$Original == tablita$prediccionesModelo)/nrow(tablita)
accuracy



