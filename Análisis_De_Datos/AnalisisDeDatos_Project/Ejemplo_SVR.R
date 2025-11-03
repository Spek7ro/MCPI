datos <- read.delim("D:/MCPI/Análisis_De_Datos/AnalisisDeDatos_Project/Datasets/caballos.txt", stringsAsFactors=TRUE)

# Para SVM la calse debe ser factor
class(datos$animal)

# Vamos a convertir la columna de "animal" de entero a FACTOR
datos$animal <- as.factor(datos$animal)
class(datos$animal)

# Mostramos los datos solo como visualizacion 
plot(datos[ , c(1,2)], col=datos$animal, pch=19)

# Vamos a crear el modelo SVM
library(e1071)

# modelo
modelo_svm <- svm(animal ~ Height + Weight, data = datos,
                  type="C-classification",
                  kernel="linear",
                  scale = FALSE)

summary(modelo_svm)

## 100% Didactico #####
# Donde estan los soportes (Soft margins)?
points(datos[modelo_svm$index, c(1,2)], col="green", cex=3, lwd=2)

# Dibujar el hiperplano (enalogo a los betas de una reg)
w <- t(modelo_svm$coefs)%*%modelo_svm$SV
b <- (modelo_svm$rho)

###
abline(a= -b/w[1,2], b= -w[1,1]/w[1,2], col="green", 
       lty=2)

### Terminamos la parte didactica

### Vamos a probar con nuevos datos
nuevos_datos <- data.frame(Height=c(67, 120, 100),
                           Weight=c(100, 190, 100)
                           )


# Regeneramos grafica para actualizar los margenes x e y
# para poder visualizar los nuevos datos
plot(datos[ ,c(1,2)], col=datos$animal,
     pch=19,
     xlim=c(0, 180),
     ylim=c(80,200))

abline(a = -b/w[1, 2], b = -w[1, 1]/w[1, 2], 
       col = "green", lty = 2)

# Vamos a agregar a la grafica los nuevos datos 
# Para clasificarlos 
points(nuevos_datos[1, ], col="green", pch=11) # primer animal
points(nuevos_datos[2, ], col="red", pch=11) # segundo animal
points(nuevos_datos[3, ], col="pink", pch=11) # tercer animal

#### Ahora vamos a predecir ####
predict(modelo_svm, newdata = nuevos_datos)

# Crear un modelo de SVR para los datos del Titanic
