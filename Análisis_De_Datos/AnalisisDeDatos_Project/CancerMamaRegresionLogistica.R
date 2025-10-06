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
resultados <- data.frame(
  Variable = character(),
  Desviacion_Estandar = numeric(),
  Varianza = numeric(),
  Rango_Dinamico = numeric(),
  P_Valor = numeric(),
  stringsAsFactors = FALSE
)

# Obtener los nombres de las variables excepto la última ('classification')
variables <- colnames(datos_cancer)[colnames(datos_cancer) != "classification"]

# Obtener: Desviacion estandar, Varianza, Rango Dinamico, p-valor y Accuracy 
# De cada variable independinte 
# Recorrer cada variable con un ciclo for
sd(datos_cancer$age)
for (var in variables) {
  # Verificar si la variable es numérica (para evitar errores con texto o factores)
  if (is.numeric(datos_cancer[[var]])) {
    # Calcular estadísticas básicas
    sd_val <- sd(datos_cancer[[var]])
    var_val <- var(datos_cancer[[var]])
    rango_val <- max(datos_cancer[[var]], na.rm = TRUE) - min(datos_cancer[[var]], na.rm = TRUE)
    
    # Agregar resultados al data.frame
    resultados <- rbind(resultados, data.frame(
      Variable = var,
      Desviacion_Estandar = sd_val,
      Varianza = var_val,
      Rango_Dinamico = rango_val,
      stringsAsFactors = FALSE
    ))
  }
}

formulita <- as.formula("classification ~ age")
modelo <- glm(formula = formulita, data = datos_cancer, family = "binomial")
summary(modelo)

options(scipen = 999)  # evitar la notación científica
print(resultados)

###### Fin analisis Univariado


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



