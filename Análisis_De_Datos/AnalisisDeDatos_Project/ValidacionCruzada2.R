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

# Crear las particiones para K = 3
set.seed(123)
indices <- createFolds(y = datos_limpios$Vivio, k = 3, returnTrain = TRUE, list = TRUE)

# Función para calcular las métricas
calcular_metricas <- function(original, predicciones) {
  cm <- table(Original = original, Prediccion = predicciones)
  print(cm)
  
  # Matriz de confusion 
  TN <- cm[1,1] 
  FP <- cm[1,2] 
  FN <- cm[2,1] 
  TP <- cm[2,2] 
  
  # Métricas
  accuracy <- (TP + TN) / sum(cm)
  sensibilidad <- TP / (TP + FN)   
  especificidad <- TN / (TN + FP)  
  
  return(list(Accuracy = accuracy,
              Sensibilidad = sensibilidad,
              Especificidad = especificidad))
}

# Validación cruzada para cada FOLD 
for (i in 1:3) {
  cat("\n================ FOLD", i, "================\n")
  
  # Crear conjuntos de entrenamiento y prueba
  datos_Fold_Entrenaminto <- datos_limpios[indices[[i]], ]
  datos_Fold_Prueba <- datos_limpios[-indices[[i]], ]
  
  # Entrenar el modelo
  modeloX <- glm(Vivio ~ Sexo + Edad, data = datos_Fold_Entrenaminto, family = "binomial")
  
  # ---- TRAIN ----
  pred_train <- predict(modeloX, newdata = datos_Fold_Entrenaminto, type = "response")
  pred_train_bin <- ifelse(pred_train >= 0.5, 1, 0)
  
  metricas_train <- calcular_metricas(datos_Fold_Entrenaminto$Vivio, pred_train_bin)
  cat("TRAIN:\n")
  print(metricas_train)
  
  # ---- TEST ----
  pred_test <- predict(modeloX, newdata = datos_Fold_Prueba, type = "response")
  pred_test_bin <- ifelse(pred_test >= 0.5, 1, 0)
  
  metricas_test <- calcular_metricas(datos_Fold_Prueba$Vivio, pred_test_bin)
  cat("TEST:\n")
  print(metricas_test)
  
  # ---- Guardar tablitas en un Excel
  tablita_train <- data.frame(Original = datos_Fold_Entrenaminto$Vivio,
                              PrediccionIA = pred_train_bin)
  tablita_test <- data.frame(Original = datos_Fold_Prueba$Vivio,
                             PrediccionIA = pred_test_bin)
  
  write.csv(tablita_train, paste0("Fold", i, "_Train.csv"), row.names = FALSE)
  write.csv(tablita_test, paste0("Fold", i, "_Test.csv"), row.names = FALSE)
}
