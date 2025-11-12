# Cargar los datos 
prestamos <- read.csv("D:/MCPI/Análisis_De_Datos/AnalisisDeDatos_Project/Datasets/loan_data.csv", stringsAsFactors=TRUE)

# Vamos a checar los NA´S con librerias 
library(naniar)
vis_miss(prestamos) # tenemos el 100% de los datos 

# Vamos a usar ep 100% de los datos (en la vida real se usa CroosValidation)

# Vamos a crear un modelo 
# Paso 1: (Vamos a seleccionar las mejores variabeles)
# El genero afecta en la otorgacion de creditos?
# a) Buro de credito, edad, Ingresos, (sin genero)
# b) Buro de credito, edad, Ingresos, genero

# Vamos a crear el modelo SVM
library(e1071)

### Muestra del 10% 
library(caret)

datos_muestra <- createDataPartition(
  y = prestamos$loan_status,
  p = 0.1,
  list = FALSE
)

datosEntrenaminto <- prestamos[ datos_muestra, ]

# modelo a
modelo_a <- svm(loan_status ~ credit_score + person_age + person_income, 
                  data = datosEntrenaminto,
                  type="C-classification",
                  kernel="radial",
                  scale = FALSE)

summary(modelo_a)

# modelo b
modelo_b <- svm(loan_status ~ credit_score + person_age + person_income + person_gender, 
                data = datosEntrenaminto,
                type="C-classification",
                kernel="radial",
                scale = FALSE)

summary(modelo_b)


#### Predicciones modelo a
predicciones_a <- predict(modelo_a, newdata = datosEntrenaminto)

#### Predicciones modelo b
predicciones_b <- predict(modelo_b, newdata = datosEntrenaminto)


# Crear las tablitas para obtener la curva ROC
tablita_a <- data.frame(Original = datosEntrenaminto$loan_status,
                        Predicciones = as.numeric(predicciones_a)-1) 

tablita_b <- data.frame(Original = datosEntrenaminto$loan_status,
                        Predicciones = as.numeric(predicciones_b)-1) 


#### Curvas ROC
library(pROC)

#### Calcular Curva ROC modelo a
mi_curva_a <- roc(tablita_a$Original, tablita_a$Predicciones,
                levels=c(0,1), plot=TRUE, ci=TRUE,
                smooth=FALSE, direction='auto',
                col='blue', main=" ")

### Area bajo la curva
mi_curva_a$auc 

#### Calcular Curva ROC modelo b
par(new=TRUE)
mi_curva_b <- roc(tablita_b$Original, tablita_b$Predicciones,
                levels=c(0,1), plot=TRUE, ci=TRUE,
                smooth=FALSE, direction='auto',
                col='red', lty=3,
                main=" ")

### Area bajo la curva
mi_curva_b$auc 

#### Crear modelos de regresion logistica
modelo_rl_a <- glm(loan_status ~ credit_score + person_age + 
                   person_income + person_gender, 
                   data = datosEntrenaminto,
                   family= "binomial",
                  )

summary(modelo_rl_a)

#### Predicciones del modelo a de regresion logistica 
predicciones_rl_a <- predict(modelo_rl_a, newdata = datosEntrenaminto,type = "response")

# Creamos la tabla  
tablita_rl_a <- data.frame(Original = datosEntrenaminto$loan_status,
                           Predicciones = as.numeric(predicciones_rl_a)-1)

#### Calcular Curva ROC modelo a
par(new=TRUE)
mi_curva_rl_a <- roc(tablita_a$Original, tablita_rl_a$Predicciones,
                  levels=c(0,1), plot=TRUE, ci=TRUE,
                  smooth=FALSE, direction='auto',
                  col='green', main="")

### Area bajo la curva
mi_curva_rl_a$auc 


#### Nuevos Modelos sin credit score
# modelo a
modelo_a_2 <- svm(loan_status ~ + person_age + person_income, 
                data = datosEntrenaminto,
                type="C-classification",
                kernel="radial",
                scale = FALSE)

# modelo b
modelo_b_2 <- svm(loan_status ~ credit_score + person_age + person_income + person_gender, 
                data = datosEntrenaminto,
                type="C-classification",
                kernel="radial",
                scale = FALSE)

# Modelo de regresion logistica  
modelo_rl_a_2 <- glm(loan_status ~ + person_age + 
                     person_income + person_gender, 
                   data = datosEntrenaminto,
                   family= "binomial",
)


# Predicciones y tablitas 
#### Predicciones modelo a
predicciones_a <- predict(modelo_a_2, newdata = datosEntrenaminto)

#### Predicciones modelo b
predicciones_b <- predict(modelo_b_2, newdata = datosEntrenaminto)


# Crear las tablitas para obtener la curva ROC
tablita_a <- data.frame(Original = datosEntrenaminto$loan_status,
                        Predicciones = as.numeric(predicciones_a)-1) 

tablita_b <- data.frame(Original = datosEntrenaminto$loan_status,
                        Predicciones = as.numeric(predicciones_b)-1) 

### Curvas ROC
#### Calcular Curva ROC modelo a
mi_curva_a <- roc(tablita_a$Original, tablita_a$Predicciones,
                  levels=c(0,1), plot=TRUE, ci=TRUE,
                  smooth=FALSE, direction='auto',
                  col='blue', main=" ")

#### Calcular Curva ROC modelo b
par(new=TRUE)
mi_curva_b <- roc(tablita_b$Original, tablita_b$Predicciones,
                  levels=c(0,1), plot=TRUE, ci=TRUE,
                  smooth=FALSE, direction='auto',
                  col='red', lty=3,
                  main=" ")

# Modelo Regresion logistica 
par(new=TRUE)
mi_curva_rl_a <- roc(tablita_a$Original, tablita_rl_a$Predicciones,
                     levels=c(0,1), plot=TRUE, ci=TRUE,
                     smooth=FALSE, direction='auto',
                     col='green', main="")

## Area bajo la curva
par(new=TRUE)
mi_curva_rl_a <- roc(tablita_a$Original, tablita_rl_a$Predicciones,
                  levels=c(0,1), plot=TRUE, ci=TRUE,
                  smooth=FALSE, direction='auto',
                  col='green', main="")

### Area bajo la curva
mi_curva_a$auc 
mi_curva_b$auc
mi_curva_rl_a$auc


# Tarea expocicion de arboles de clasificacion
# que es 
# como funciona
# ejemplos

