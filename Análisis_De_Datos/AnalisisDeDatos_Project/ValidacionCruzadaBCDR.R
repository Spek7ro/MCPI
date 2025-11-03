# Librerias
library(caret)
library(pROC)

# 1. Cargar datos
datos_cancer <- read.csv("D:/MCPI/Análisis_De_Datos/AnalisisDeDatos_Project/Datasets/bcdr_d01_features.csv")

# 2. limpiar los datos 
# vamos a quitar la columna density que contiene Na´S
sum(is.na(datos_cancer$density))

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

# crear la particiones para TRAIN y TRAINING K = 3 
indices = createFolds(y = datos_cancer$classification, k = 3, 
                      returnTrain = TRUE,
                      list = TRUE)

# ------------------------------ Modelo 1 ------------------------------
##### Validacion Cruzada y metricas para entrenaimnto K = 1 ####
### Modelo con 3 variables 
datos_Fold_Entrenaminto <- datos_cancer[indices$Fold1, ]
datos_Fold_Prueba <- datos_cancer[-indices$Fold1, ] 

##### ----- Entrenamintos Modelos ------ ##### 
modeloX <- glm(classification ~ age + i_mean + i_std_dev, 
               data = datos_Fold_Entrenaminto,
               family = "binomial")

# Predicciones
predicciones <- predict(modeloX, newdata = datos_Fold_Entrenaminto,
                        type = "response")

# Construir la tabla
tablitaX <- data.frame(Original = datos_Fold_Entrenaminto$classification, 
                       prediccionesModelo = predicciones)

#### Calcular Curva ROC
mi_curva <- roc(tablitaX$Original, tablitaX$prediccionesModelo,
                levels=c(0,1), plot=TRUE, ci=TRUE,
                smooth=FALSE, direction='auto',
                col='red', main="Modelo 1: Grafica ROC -  Entrenamiento K=1")

### Area bajo la curva
mi_curva$auc 

#### Obtenemos los valores de Threshold (umbral binarizacion) y metricas 
valores <- coords(mi_curva, "best", ret=c("threshold", "specificity", "sensitivity"))
valores

# Binarizar pero de forma vectorial:   
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo < valores$threshold] <- 0
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo >= valores$threshold] <- 1

# Calcular el accuracy de entrenaminto 
accuracy <- sum(tablitaX$Original == tablitaX$prediccionesModelo)/nrow(tablitaX)
accuracy 

##### Validacion Cruzada y metricas para validacion de K = 1 ####
### Modelo con 3 variables 
predicciones <- predict(modeloX, newdata = datos_Fold_Prueba, type="response")

tablitaX <- data.frame(Original = datos_Fold_Prueba$classification,
                       prediccionesModelo = predicciones)

mi_curva <- roc(tablitaX$Original, tablitaX$prediccionesModelo,
               levels=c(0,1), plot=TRUE, ci=TRUE,
               smooth=FALSE, direction='auto',
               col='green', main="Modelo 1: Grafica ROC - Prueba K=1")
#AUC
mi_curva$auc 

valores <- coords(mi_curva,"best",ret=c("threshold","specificity", "sensitivity"))
valores

#Binarizar
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo<valores$threshold] <- 0
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo>=valores$threshold] <- 1

# Calcular el accuracy de validacion
accuracy <- sum(tablitaX$Original == tablitaX$prediccionesModelo)/nrow(tablitaX)
accuracy

##### Validacion Cruzada y metricas para entrenaimnto K = 2 ####
### Modelo con 3 variables 
datos_Fold_Entrenaminto <- datos_cancer[indices$Fold2, ]
datos_Fold_Prueba <- datos_cancer[-indices$Fold2, ] 

##### ----- Entrenamintos Modelos ------ ##### 
modeloX <- glm(classification ~ age + i_mean + i_std_dev, 
               data = datos_Fold_Entrenaminto,
               family = "binomial")

# Predicciones
predicciones <- predict(modeloX, newdata = datos_Fold_Entrenaminto,
                        type = "response")

# Construir la tabla
tablitaX <- data.frame(Original = datos_Fold_Entrenaminto$classification, 
                       prediccionesModelo = predicciones)

#### Calcular Curva ROC
mi_curva <- roc(tablitaX$Original, tablitaX$prediccionesModelo,
                levels=c(0,1), plot=TRUE, ci=TRUE,
                smooth=FALSE, direction='auto',
                col='red', main="Modelo 1: Grafica ROC -  Entrenamiento K=2")

### Area bajo la curva
mi_curva$auc 

#### Obtenemos los valores de Threshold (umbral binarizacion) y metricas 
valores <- coords(mi_curva, "best", ret=c("threshold", "specificity", "sensitivity"))
valores

# Binarizar pero de forma vectorial:   
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo < valores$threshold] <- 0
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo >= valores$threshold] <- 1

# Calcular el accuracy de entrenaminto 
accuracy <- sum(tablitaX$Original == tablitaX$prediccionesModelo)/nrow(tablitaX)
accuracy 

##### Validacion Cruzada y metricas para validacion de K = 2 ####
### Modelo con 3 variables 
predicciones <- predict(modeloX, newdata = datos_Fold_Prueba, type="response")

tablitaX <- data.frame(Original = datos_Fold_Prueba$classification,
                       prediccionesModelo = predicciones)

mi_curva <- roc(tablitaX$Original, tablitaX$prediccionesModelo,
                levels=c(0,1), plot=TRUE, ci=TRUE,
                smooth=FALSE, direction='auto',
                col='green', main="Modelo 1: Grafica ROC - Prueba K=2")
#AUC
mi_curva$auc 

valores <- coords(mi_curva,"best",ret=c("threshold","specificity", "sensitivity"))
valores

#Binarizar
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo<valores$threshold] <- 0
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo>=valores$threshold] <- 1

# Calcular el accuracy de validacion
accuracy <- sum(tablitaX$Original == tablitaX$prediccionesModelo)/nrow(tablitaX)
accuracy

### Validacion Cruzada y metricas para entrenaimnto K = 3 ####
### Modelo con 3 variables 
datos_Fold_Entrenaminto <- datos_cancer[indices$Fold3, ]
datos_Fold_Prueba <- datos_cancer[-indices$Fold3, ]

##### ----- Entrenamintos Modelos ------ ##### 
modeloX <- glm(classification ~ age + i_mean + i_std_dev, 
               data = datos_Fold_Entrenaminto,
               family = "binomial")

# Predicciones
predicciones <- predict(modeloX, newdata = datos_Fold_Entrenaminto,
                        type = "response")

# Construir la tabla
tablitaX <- data.frame(Original = datos_Fold_Entrenaminto$classification, 
                       prediccionesModelo = predicciones)

#### Calcular Curva ROC
mi_curva <- roc(tablitaX$Original, tablitaX$prediccionesModelo,
                levels=c(0,1), plot=TRUE, ci=TRUE,
                smooth=FALSE, direction='auto',
                col='red', main="Modelo 1: Grafica ROC -  Entrenamiento K=3")

### Area bajo la curva
mi_curva$auc 

#### Obtenemos los valores de Threshold (umbral binarizacion) y metricas 
valores <- coords(mi_curva, "best", ret=c("threshold", "specificity", "sensitivity"))
valores

# Binarizar pero de forma vectorial:   
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo < valores$threshold] <- 0
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo >= valores$threshold] <- 1

# Calcular el accuracy de entrenaminto 
accuracy <- sum(tablitaX$Original == tablitaX$prediccionesModelo)/nrow(tablitaX)
accuracy 

##### Validacion Cruzada y metricas para validacion de K = 3 ####
### Modelo con 3 variables 
predicciones <- predict(modeloX, newdata = datos_Fold_Prueba, type="response")

tablitaX <- data.frame(Original = datos_Fold_Prueba$classification,
                       prediccionesModelo = predicciones)

mi_curva <- roc(tablitaX$Original, tablitaX$prediccionesModelo,
                levels=c(0,1), plot=TRUE, ci=TRUE,
                smooth=FALSE, direction='auto',
                col='green', main="Modelo 1: Grafica ROC - Prueba K=3")
#AUC
mi_curva$auc 

valores <- coords(mi_curva,"best",ret=c("threshold","specificity", "sensitivity"))
valores

#Binarizar
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo<valores$threshold] <- 0
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo>=valores$threshold] <- 1

# Calcular el accuracy de validacion
accuracy <- sum(tablitaX$Original == tablitaX$prediccionesModelo)/nrow(tablitaX)
accuracy

# ------------------------------ Modelo 2 ------------------------------
##### Validacion Cruzada y metricas para entrenaimnto K = 1 ####
### Modelo con 5 variables 
datos_Fold_Entrenaminto <- datos_cancer[indices$Fold1, ]
datos_Fold_Prueba <- datos_cancer[-indices$Fold1, ] 

##### ----- Entrenamintos Modelos ------ ##### 
modeloX <- glm(classification ~ age + i_mean + i_std_dev + i_skewness + s_area, 
               data = datos_Fold_Entrenaminto,
               family = "binomial")

# Predicciones
predicciones <- predict(modeloX, newdata = datos_Fold_Entrenaminto,
                        type = "response")

# Construir la tabla
tablitaX <- data.frame(Original = datos_Fold_Entrenaminto$classification, 
                       prediccionesModelo = predicciones)

#### Calcular Curva ROC
mi_curva <- roc(tablitaX$Original, tablitaX$prediccionesModelo,
                levels=c(0,1), plot=TRUE, ci=TRUE,
                smooth=FALSE, direction='auto',
                col='red', main="Modelo 2: Grafica ROC -  Entrenamiento K=1")

### Area bajo la curva
mi_curva$auc 

#### Obtenemos los valores de Threshold (umbral binarizacion) y metricas 
valores <- coords(mi_curva, "best", ret=c("threshold", "specificity", "sensitivity"))
valores

# Binarizar pero de forma vectorial:   
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo < valores$threshold] <- 0
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo >= valores$threshold] <- 1

# Calcular el accuracy de entrenaminto 
accuracy <- sum(tablitaX$Original == tablitaX$prediccionesModelo)/nrow(tablitaX)
accuracy 

##### Validacion Cruzada y metricas para validacion de K = 1 ####
### Modelo con 5 variables 
predicciones <- predict(modeloX, newdata = datos_Fold_Prueba, type="response")

tablitaX <- data.frame(Original = datos_Fold_Prueba$classification,
                       prediccionesModelo = predicciones)

mi_curva <- roc(tablitaX$Original, tablitaX$prediccionesModelo,
                levels=c(0,1), plot=TRUE, ci=TRUE,
                smooth=FALSE, direction='auto',
                col='green', main="Modelo 2: Grafica ROC - Prueba K=1")
#AUC
mi_curva$auc 

valores <- coords(mi_curva,"best",ret=c("threshold","specificity", "sensitivity"))
valores

#Binarizar
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo<valores$threshold] <- 0
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo>=valores$threshold] <- 1

# Calcular el accuracy de validacion
accuracy <- sum(tablitaX$Original == tablitaX$prediccionesModelo)/nrow(tablitaX)
accuracy

##### Validacion Cruzada y metricas para entrenaimnto K = 2 ####
### Modelo con 5 variables 
datos_Fold_Entrenaminto <- datos_cancer[indices$Fold2, ]
datos_Fold_Prueba <- datos_cancer[-indices$Fold2, ] 

##### ----- Entrenamintos Modelos ------ ##### 
modeloX <- glm(classification ~ age + i_mean + i_std_dev + i_skewness + s_area, 
               data = datos_Fold_Entrenaminto,
               family = "binomial")

# Predicciones
predicciones <- predict(modeloX, newdata = datos_Fold_Entrenaminto,
                        type = "response")

# Construir la tabla
tablitaX <- data.frame(Original = datos_Fold_Entrenaminto$classification, 
                       prediccionesModelo = predicciones)

#### Calcular Curva ROC
mi_curva <- roc(tablitaX$Original, tablitaX$prediccionesModelo,
                levels=c(0,1), plot=TRUE, ci=TRUE,
                smooth=FALSE, direction='auto',
                col='red', main="Modelo 2: Grafica ROC -  Entrenamiento K=2")

### Area bajo la curva
mi_curva$auc 

#### Obtenemos los valores de Threshold (umbral binarizacion) y metricas 
valores <- coords(mi_curva, "best", ret=c("threshold", "specificity", "sensitivity"))
valores

# Binarizar pero de forma vectorial:   
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo < valores$threshold] <- 0
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo >= valores$threshold] <- 1

# Calcular el accuracy de entrenaminto 
accuracy <- sum(tablitaX$Original == tablitaX$prediccionesModelo)/nrow(tablitaX)
accuracy 

##### Validacion Cruzada y metricas para validacion de K = 2 ####
### Modelo con 5 variables 
predicciones <- predict(modeloX, newdata = datos_Fold_Prueba, type="response")

tablitaX <- data.frame(Original = datos_Fold_Prueba$classification,
                       prediccionesModelo = predicciones)

mi_curva <- roc(tablitaX$Original, tablitaX$prediccionesModelo,
                levels=c(0,1), plot=TRUE, ci=TRUE,
                smooth=FALSE, direction='auto',
                col='green', main="Modelo 2: Grafica ROC - Prueba K=2")
#AUC
mi_curva$auc 

valores <- coords(mi_curva,"best",ret=c("threshold","specificity", "sensitivity"))
valores

#Binarizar
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo<valores$threshold] <- 0
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo>=valores$threshold] <- 1

# Calcular el accuracy de validacion
accuracy <- sum(tablitaX$Original == tablitaX$prediccionesModelo)/nrow(tablitaX)
accuracy

### Validacion Cruzada y metricas para entrenaminto K = 3 ####
### Modelo con 5 variables 
datos_Fold_Entrenaminto <- datos_cancer[indices$Fold3, ]
datos_Fold_Prueba <- datos_cancer[-indices$Fold3, ] 

##### ----- Entrenamintos Modelos ------ ##### 
modeloX <- glm(classification ~ age + i_mean + i_std_dev + i_skewness + s_area, 
               data = datos_Fold_Entrenaminto,
               family = "binomial")

# Predicciones
predicciones <- predict(modeloX, newdata = datos_Fold_Entrenaminto,
                        type = "response")

# Construir la tabla
tablitaX <- data.frame(Original = datos_Fold_Entrenaminto$classification, 
                       prediccionesModelo = predicciones)

#### Calcular Curva ROC
mi_curva <- roc(tablitaX$Original, tablitaX$prediccionesModelo,
                levels=c(0,1), plot=TRUE, ci=TRUE,
                smooth=FALSE, direction='auto',
                col='red', main="Modelo 2: Grafica ROC -  Entrenamiento K=3")

### Area bajo la curva
mi_curva$auc 

#### Obtenemos los valores de Threshold (umbral binarizacion) y metricas 
valores <- coords(mi_curva, "best", ret=c("threshold", "specificity", "sensitivity"))
valores

# Binarizar pero de forma vectorial:   
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo < valores$threshold] <- 0
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo >= valores$threshold] <- 1

# Calcular el accuracy de entrenaminto 
accuracy <- sum(tablitaX$Original == tablitaX$prediccionesModelo)/nrow(tablitaX)
accuracy 

##### Validacion Cruzada y metricas para validacion de K = 3 ####
### Modelo con 5 variables 
predicciones <- predict(modeloX, newdata = datos_Fold_Prueba, type="response")

tablitaX <- data.frame(Original = datos_Fold_Prueba$classification,
                       prediccionesModelo = predicciones)

mi_curva <- roc(tablitaX$Original, tablitaX$prediccionesModelo,
                levels=c(0,1), plot=TRUE, ci=TRUE,
                smooth=FALSE, direction='auto',
                col='green', main="Modelo 2: Grafica ROC - Prueba K=3")
#AUC
mi_curva$auc 

valores <- coords(mi_curva,"best",ret=c("threshold","specificity", "sensitivity"))
valores

#Binarizar
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo<valores$threshold] <- 0
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo>=valores$threshold] <- 1

# Calcular el accuracy de validacion
accuracy <- sum(tablitaX$Original == tablitaX$prediccionesModelo)/nrow(tablitaX)
accuracy

# ------------------------------ Modelo 3 ------------------------------
##### Validacion Cruzada y metricas para entrenamiento K = 1 ####
### Modelo con 7 variables 
datos_Fold_Entrenaminto <- datos_cancer[indices$Fold1, ]
datos_Fold_Prueba <- datos_cancer[-indices$Fold1, ]

##### ----- Entrenamintos Modelos ------ ##### 
modeloX <- glm(classification ~ age + i_mean + i_std_dev 
               + i_skewness + s_area + s_circularity + t_energ,
               data = datos_Fold_Entrenaminto,
               family = "binomial")

# Predicciones
predicciones <- predict(modeloX, newdata = datos_Fold_Entrenaminto,
                        type = "response")

# Construir la tabla
tablitaX <- data.frame(Original = datos_Fold_Entrenaminto$classification, 
                       prediccionesModelo = predicciones)

#### Calcular Curva ROC
mi_curva <- roc(tablitaX$Original, tablitaX$prediccionesModelo,
                levels=c(0,1), plot=TRUE, ci=TRUE,
                smooth=FALSE, direction='auto',
                col='red', main="Modelo 3: Grafica ROC -  Entrenamiento K=1")

### Area bajo la curva
mi_curva$auc 

#### Obtenemos los valores de Threshold (umbral binarizacion) y metricas 
valores <- coords(mi_curva, "best", ret=c("threshold", "specificity", "sensitivity"))
valores

# Binarizar pero de forma vectorial:   
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo < valores$threshold] <- 0
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo >= valores$threshold] <- 1

# Calcular el accuracy de entrenaminto 
accuracy <- sum(tablitaX$Original == tablitaX$prediccionesModelo)/nrow(tablitaX)
accuracy

##### Validacion Cruzada y metricas para validacion de K = 1 ####
### Modelo con 7 variables 
predicciones <- predict(modeloX, newdata = datos_Fold_Prueba, type="response")

tablitaX <- data.frame(Original = datos_Fold_Prueba$classification,
                       prediccionesModelo = predicciones)

mi_curva <- roc(tablitaX$Original, tablitaX$prediccionesModelo,
                levels=c(0,1), plot=TRUE, ci=TRUE,
                smooth=FALSE, direction='auto',
                col='green', main="Modelo 3: Grafica ROC - Prueba K=1")
#AUC
mi_curva$auc 

valores <- coords(mi_curva,"best",ret=c("threshold","specificity", "sensitivity"))
valores

#Binarizar
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo<valores$threshold] <- 0
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo>=valores$threshold] <- 1

# Calcular el accuracy de validacion
accuracy <- sum(tablitaX$Original == tablitaX$prediccionesModelo)/nrow(tablitaX)
accuracy

##### Validacion Cruzada y metricas para entrenamiento K = 2 ####
### Modelo con 7 variables 
datos_Fold_Entrenaminto <- datos_cancer[indices$Fold2, ]
datos_Fold_Prueba <- datos_cancer[-indices$Fold2, ]

##### ----- Entrenamintos Modelos ------ ##### 
modeloX <- glm(classification ~ age + i_mean + i_std_dev 
               + i_skewness + s_area + s_circularity + t_energ,
               data = datos_Fold_Entrenaminto,
               family = "binomial")

# Predicciones
predicciones <- predict(modeloX, newdata = datos_Fold_Entrenaminto,
                        type = "response")

# Construir la tabla
tablitaX <- data.frame(Original = datos_Fold_Entrenaminto$classification, 
                       prediccionesModelo = predicciones)

#### Calcular Curva ROC
mi_curva <- roc(tablitaX$Original, tablitaX$prediccionesModelo,
                levels=c(0,1), plot=TRUE, ci=TRUE,
                smooth=FALSE, direction='auto',
                col='red', main="Modelo 3: Grafica ROC -  Entrenamiento K=2")

### Area bajo la curva
mi_curva$auc 

#### Obtenemos los valores de Threshold (umbral binarizacion) y metricas 
valores <- coords(mi_curva, "best", ret=c("threshold", "specificity", "sensitivity"))
valores

# Binarizar pero de forma vectorial:   
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo < valores$threshold] <- 0
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo >= valores$threshold] <- 1

# Calcular el accuracy de entrenaminto 
accuracy <- sum(tablitaX$Original == tablitaX$prediccionesModelo)/nrow(tablitaX)
accuracy

##### Validacion Cruzada y metricas para validacion de K = 2 ####
### Modelo con 7 variables 
predicciones <- predict(modeloX, newdata = datos_Fold_Prueba, type="response")

tablitaX <- data.frame(Original = datos_Fold_Prueba$classification,
                       prediccionesModelo = predicciones)

mi_curva <- roc(tablitaX$Original, tablitaX$prediccionesModelo,
                levels=c(0,1), plot=TRUE, ci=TRUE,
                smooth=FALSE, direction='auto',
                col='green', main="Modelo 3: Grafica ROC - Prueba K=2")
#AUC
mi_curva$auc 

valores <- coords(mi_curva,"best",ret=c("threshold","specificity", "sensitivity"))
valores

#Binarizar
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo<valores$threshold] <- 0
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo>=valores$threshold] <- 1

# Calcular el accuracy de validacion
accuracy <- sum(tablitaX$Original == tablitaX$prediccionesModelo)/nrow(tablitaX)
accuracy

### Validacion Cruzada y metricas para entrenamiento K = 3 ####
### Modelo con 7 variables 
datos_Fold_Entrenaminto <- datos_cancer[indices$Fold3, ]
datos_Fold_Prueba <- datos_cancer[-indices$Fold3, ]

##### ----- Entrenamintos Modelos ------ ##### 
modeloX <- glm(classification ~ age + i_mean + i_std_dev 
               + i_skewness + s_area + s_circularity + t_energ,
               data = datos_Fold_Entrenaminto,
               family = "binomial")

# Predicciones
predicciones <- predict(modeloX, newdata = datos_Fold_Entrenaminto,
                        type = "response")

# Construir la tabla
tablitaX <- data.frame(Original = datos_Fold_Entrenaminto$classification, 
                       prediccionesModelo = predicciones)

#### Calcular Curva ROC
mi_curva <- roc(tablitaX$Original, tablitaX$prediccionesModelo,
                levels=c(0,1), plot=TRUE, ci=TRUE,
                smooth=FALSE, direction='auto',
                col='red', main="Modelo 3: Grafica ROC -  Entrenamiento K=3")

### Area bajo la curva
mi_curva$auc 

#### Obtenemos los valores de Threshold (umbral binarizacion) y metricas 
valores <- coords(mi_curva, "best", ret=c("threshold", "specificity", "sensitivity"))
valores

# Binarizar pero de forma vectorial:   
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo < valores$threshold] <- 0
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo >= valores$threshold] <- 1

# Calcular el accuracy de entrenaminto 
accuracy <- sum(tablitaX$Original == tablitaX$prediccionesModelo)/nrow(tablitaX)
accuracy

##### Validacion Cruzada y metricas para validacion de K = 3 ####
### Modelo con 7 variables 
predicciones <- predict(modeloX, newdata = datos_Fold_Prueba, type="response")

tablitaX <- data.frame(Original = datos_Fold_Prueba$classification,
                       prediccionesModelo = predicciones)

mi_curva <- roc(tablitaX$Original, tablitaX$prediccionesModelo,
                levels=c(0,1), plot=TRUE, ci=TRUE,
                smooth=FALSE, direction='auto',
                col='green', main="Modelo 3: Grafica ROC - Prueba K=3")
#AUC
mi_curva$auc 

valores <- coords(mi_curva,"best",ret=c("threshold","specificity", "sensitivity"))
valores

#Binarizar
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo<valores$threshold] <- 0
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo>=valores$threshold] <- 1

# Calcular el accuracy de validacion
accuracy <- sum(tablitaX$Original == tablitaX$prediccionesModelo)/nrow(tablitaX)
accuracy

