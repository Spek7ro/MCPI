# Libreria Para la validacion cruzada
library(caret)

# Limpiar el dataset
sum(is.na(DatosTitanic$Id))
sum(is.na(DatosTitanic$Vivio))
sum(is.na(DatosTitanic$Pclase))
sum(is.na(DatosTitanic$Nombre))
sum(is.na(DatosTitanic$Sexo))
sum(is.na(DatosTitanic$Edad)) # 177 datos NA`S

# En este caso quitaremos el 20% de los datos vamos a remover 177 datos
datos_limpios <- DatosTitanic[!is.na(DatosTitanic$Edad), ]

# crear la particiones para TRAIN y TRAINING K = 3 
indices = createFolds(y = datos_limpios$Vivio, k = 3, 
            returnTrain = TRUE,
            list = TRUE)

###### Validacion Cruzada K = 1 #######
datos_Fold_Entrenaminto <- datos_limpios[indices$Fold1, ]
datos_Fold_Prueba <- datos_limpios[-indices$Fold1, ] # todos menos los del los inices

##### ----- Entrenamintos Modelos ------ ##### 
modeloX <- glm(Vivio ~ Sexo + Edad, 
               data = datos_Fold_Entrenaminto,
               family = "binomial")

# Metricas Entrenaminto 
predicciones <- predict(modeloX, newdata = datos_Fold_Entrenaminto,
                        type = "response")

# Construir la tabla
tablitaX <- data.frame(Original = datos_Fold_Entrenaminto$Vivio, 
                      prediccionesModelo = predicciones)

#### Calcular Curva ROC
library(pROC)
mi_curva <- roc(tablitaX$Original, tablitaX$prediccionesModelo,
                 levels=c(0,1), plot=TRUE, ci=TRUE,
                 smooth=FALSE, direction='auto',
                 col='red', main="Grafica ROC")

### Area bajo la curva
mi_curva$auc # 0.7932 AUC
mi_curva

#### Obtenemos los valores de Threshold (umbral binarizacion)
valores <- coords(mi_curva, "best", ret="threshold")
valores$threshold

# Binarizar pero de forma vectorial:   
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo < 0.5] <- 0
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo >= 0.5] <- 1

# Calcular el accuracy de entrenaminto 
accuracy <- sum(tablitaX$Original == tablitaX$prediccionesModelo)/nrow(tablitaX)
accuracy # 0.789916


######## Ahora para VALIDACION K = 1 ########
predicciones <- predict(modeloX, newdata = datos_Fold_Prueba,
                        type = "response")

tablitaX <- data.frame(Original = datos_Fold_Prueba$Vivio, 
                       prediccionesModelo = predicciones)

tablitaX$prediccionesModelo[tablitaX$prediccionesModelo < 0.5] <- 0
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo >= 0.5] <- 1

accuracy <- sum(tablitaX$Original == tablitaX$prediccionesModelo)/nrow(tablitaX)
accuracy # 0.7605042

######################
# Validacion Cruzada K = 2
datos_Fold_Entrenaminto <- datos_limpios[indices$Fold2, ]
datos_Fold_Prueba <- datos_limpios[-indices$Fold2, ] # todos menos los del los inices

##### ----- Entrenamintos Modelos ------ ##### 
modeloX <- glm(Vivio ~ Sexo + Edad, 
               data = datos_Fold_Entrenaminto,
               family = "binomial")

# Metricas Entrenaminto 
predicciones <- predict(modeloX, newdata = datos_Fold_Entrenaminto,
                        type = "response")

# Construir la tabla
tablitaX <- data.frame(Original = datos_Fold_Entrenaminto$Vivio, 
                       prediccionesModelo = predicciones)

# Binarizar pero de forma vectorial:   
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo < 0.5] <- 0
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo >= 0.5] <- 1

# Calcular el accuracy de entrenaminto 
accuracy <- sum(tablitaX$Original == tablitaX$prediccionesModelo)/nrow(tablitaX)
accuracy # 0.7941176


######## Ahora para VALIDACION K = 2 ########
predicciones <- predict(modeloX, newdata = datos_Fold_Prueba,
                        type = "response")

tablitaX <- data.frame(Original = datos_Fold_Prueba$Vivio, 
                       prediccionesModelo = predicciones)

tablitaX$prediccionesModelo[tablitaX$prediccionesModelo < 0.5] <- 0
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo >= 0.5] <- 1

accuracy <- sum(tablitaX$Original == tablitaX$prediccionesModelo)/nrow(tablitaX)
accuracy # 0.7521008


######################
# Validacion Cruzada K = 3
datos_Fold_Entrenaminto <- datos_limpios[indices$Fold3, ]
datos_Fold_Prueba <- datos_limpios[-indices$Fold3, ] # todos menos los del los inices

##### ----- Entrenamintos Modelos ------ ##### 
modeloX <- glm(Vivio ~ Sexo + Edad, 
               data = datos_Fold_Entrenaminto,
               family = "binomial")

# Metricas Entrenaminto 
predicciones <- predict(modeloX, newdata = datos_Fold_Entrenaminto,
                        type = "response")

# Construir la tabla
tablitaX <- data.frame(Original = datos_Fold_Entrenaminto$Vivio, 
                       prediccionesModelo = predicciones)

# Binarizar pero de forma vectorial:   
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo < 0.5] <- 0
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo >= 0.5] <- 1

# Calcular el accuracy de entrenaminto 
accuracy <- sum(tablitaX$Original == tablitaX$prediccionesModelo)/nrow(tablitaX)
accuracy # 0.7563025


######## Ahora para VALIDACION K = 3 ########
predicciones <- predict(modeloX, newdata = datos_Fold_Prueba,
                        type = "response")

tablitaX <- data.frame(Original = datos_Fold_Prueba$Vivio, 
                       prediccionesModelo = predicciones)

tablitaX$prediccionesModelo[tablitaX$prediccionesModelo < 0.5] <- 0
tablitaX$prediccionesModelo[tablitaX$prediccionesModelo >= 0.5] <- 1

accuracy <- sum(tablitaX$Original == tablitaX$prediccionesModelo)/nrow(tablitaX)
accuracy # 0.8277311



