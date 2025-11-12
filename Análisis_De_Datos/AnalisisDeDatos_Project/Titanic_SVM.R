library(e1071)

# Carga los datos
datos <- read.csv("D:/MCPI/Análisis_De_Datos/AnalisisDeDatos_Project/Datasets/DatosTitanic_SinLimpiar.csv", stringsAsFactors=TRUE)

# Limpia los datos quitar NA´s
datos_limpios <- datos[!is.na(datos$Edad), ]

class(datos_limpios$Vivio) # Integer 

# Convertir la variable vivios a Factor 
datos_limpios$Vivio <- as.factor(datos_limpios$Vivio)
class(datos_limpios$Vivio)

datos_limpios$Sexo <- as.factor(datos_limpios$Sexo)
class(datos_limpios$Sexo)

# Mostramos los datos solo como visualizacion 
plot(datos_limpios[ , c(1,2)], col=datos_limpios$Sexo, pch=19)

# modelo SVR
# Establecer una semilla para reproducibilidad
set.seed(123)

# Dividir los datos (80% para entrenamiento, 20% para prueba)
train_indices <- sample(1:nrow(datos_limpios), 0.8 * nrow(datos_limpios))
training_set <- datos_limpios[train_indices, ]
test_set <- datos_limpios[-train_indices, ]

modelo_svm <- svm(Vivio ~ Sexo + Edad, data = datos_limpios,
                  type="C-classification",
                  kernel="radial",
                  scale = FALSE)

summary(modelo_svm)

# Predecir sobre el conjunto de prueba
predicciones_svm <- predict(modelo_svm, test_set)

# Crear una matriz de confusión para evaluar el rendimiento
matriz_confusion <- table(predicciones_svm, test_set$Vivio)
print(matriz_confusion)

# Calcular la precisión
precision <- sum(diag(matriz_confusion)) / sum(matriz_confusion)
print(paste("Precisión del modelo:", round(precision * 100, 2), "%"))


## 100% Didactico #####
# Donde estan los soportes (Soft margins)?
points(datos_limpios[modelo_svr$index, c(1,2)], col="green", cex=3, lwd=2)

# Dibujar el hiperplano (enalogo a los betas de una reg)
w <- t(modelo_svr$coefs)%*%modelo_svr$SV
b <- (modelo_svr$rho)

###
abline(a= -b/w[1,2], b= -w[1,1]/w[1,2], col="green", 
       lty=2)

### Terminamos la parte didactica
