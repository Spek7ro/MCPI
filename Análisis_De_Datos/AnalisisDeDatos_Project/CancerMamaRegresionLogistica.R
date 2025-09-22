# 1. cargar los datos
datos_cancer <- read.csv("D:/MCPI/Análisis_De_Datos/AnalisisDeDatos_Project/bcdr_d01_features.csv")

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


# 3. Crear un modelo: Regresion logistica
# Seleccionar que queremos predecir en funcion de que (seleccion de caracteristicas)
# usaremos age, i_mean y i_std_dev
datos_cancer$s_y_center_mass
formulita <- as.formula("classification ~ age + i_mean + i_std_dev + s_area + s_perimeter + s_solidity + s_elongation + s_form + s_extent + s_x_center_mass + s_y_center_mass")
modelo <- glm(formula = formulita, data = datos_cancer, family = "binomial")

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



