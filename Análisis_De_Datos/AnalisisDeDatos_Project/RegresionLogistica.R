# Vamos a cargar y limpiar un dataset

# 1. Cargar el dataset
datos <- read.csv("D:/MCPI/Análisis_De_Datos/AnalisisDeDatos_Project/DatosTitanic_SinLimpiar.csv")

# 2. Limpiar el dataset
sum(is.na(datos$Id))
sum(is.na(datos$Vivio))
sum(is.na(datos$Pclase))
sum(is.na(datos$Nombre))
sum(is.na(datos$Sexo))
sum(is.na(datos$Edad))

# Cuando tenemos datos faltantes hay dos opciones:
# 1. Quitarlos (renglones)
# 2. Imputarlos (Invetarlos)

# En este caso quitaremos el 20% de los datos vamos a remover 177 datos
datos_limpios <- datos[!is.na(datos$Edad), ]

# Continumaos analizando 
sum(is.na(datos_limpios$HermaConyu))
sum(is.na(datos_limpios$PadresHijos))
sum(is.na(datos_limpios$Ticket))
sum(is.na(datos_limpios$Tarifa))
sum(is.na(datos_limpios$Cabina))
sum(is.na(datos_limpios$PuertoEmb))

# False = 0, True = 1

# 3. Crear un modelo de Regresion logistica
# Formula: en la cual le vamos a indicar que queremos predecir
# Predecir si una persona hubiera sobrevivido o no usando la hipoteis
# Mujeres y niños primero 
# formula = "vivio ~ sexo + edad"
modelo <- glm(Vivio ~ Sexo + Edad, family = "binomial", data = datos_limpios)

# Obtener el desempeño usando metricas:
# 1.  Accuracy: Exactitud = % de instancias 
# Paso 1: Calcular la salida del algoritmo
# Predicciones 
predicciones <- predict(modelo, newdata = datos_limpios, type = "response") 
predicciones[1:10]
# la salida de la regresion logistica son valores entre 0 y 1

# Vamos a crear la tabla con las salidas del modelo 
tablita <- data.frame(Original = datos_limpios$Vivio, 
                      prediccionesIA = predicciones)

# para poder comprar lo que deberia de ser con la salida de IA
# Vamos a Binarizar: Valores menores a 0.5 sera cero y cualquier valor 
# Mayor o igual a 0.5 sera uno

# Binarizacion manual con un ciclo for:
for (i in seq_along(tablita$prediccionesIA)) {
  if (tablita$prediccionesIA[i] < 0.5) {
    tablita$prediccionesIA[i] <- 0
  } else {
    tablita$prediccionesIA[i] <- 1
  }
}

# Binarizar pero de forma vectorial:   
tablita$prediccionesIA[tablita$prediccionesIA < 0.5] <- 0
tablita$prediccionesIA[tablita$prediccionesIA >= 0.5] <- 1

# Una vez que tenemos la tabla con las dos columnas ya binarizadas
# Calculamos su accuracy
# forma tradicional: 
suma <- 0
for (i in seq_along(tablita$Original)) {
  if (tablita$Original[i] == tablita$prediccionesIA[i]) {
    suma <- suma + 1
  }
}

accuracy <- suma/nrow(tablita)
accuracy

# Accuracy de forma vectorial:
accuracy <- sum(tablita$Original == tablita$prediccionesIA)/nrow(tablita)
accuracy

# Vamos a probarlo 
# Cargar datos:
DatosCalamarMCPI <- read.csv("D:/MCPI/Análisis_De_Datos/AnalisisDeDatos_Project/DatosCalamarMCPI.csv")

# Obtener predicciones:
prediccionesMCPI <- predict(modelo, newdata = DatosCalamarMCPI, type = "response") 
prediccionesMCPI
