# Vamos a cargar y limpiar un dataset

# 1. Cargar el dataset
datos <- read.csv("D:/MCPI/Análisis_De_Datos/AnalisisDeDatos_Project/Datasets/DatosTitanic_SinLimpiar.csv")

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

##### Etapa de Analis Univariado
# 1. Generar Estadisticos 
# Desviacion Estandar: Que Tenga > 0
# Varianza: Que tenga > 0 
# Rango dinamico (max-min): Buscar valores atipicos (Que esten dentro de un criterio) 
# Ejemplo si estamos detectando Diabetes y la columna
# Glucosa nosotros esperamos que las personas tengan valores de 50 - 500

# Ojo, solo se hace en las caracteristicas de entrada no en las de salida
sd(datos_limpios$Pclase) # Desviacion estandar ->  0.8382499
var(datos_limpios$Pclase) # Varianza -> 0.7026628
range(datos_limpios$Pclase) # Rango Dinamico -> 1-3 = 2
max(datos_limpios$Pclase) - min(datos_limpios$Pclase) # 2

# Variable Sexo (No aplica es texto)

# Edad:
sd(datos_limpios$Edad) # 14.5265
var(datos_limpios$Edad) # 211.0191
max(datos_limpios$Edad) - min(datos_limpios$Edad) # 79.58

# HermaConyu
sd(datos_limpios$HermaConyu) # 0.9297835
var(datos_limpios$HermaConyu) # 0.8644973
max(datos_limpios$HermaConyu) - min(datos_limpios$HermaConyu) # 5

# PadresHijos
sd(datos_limpios$PadresHijos) # 0.8532894
var(datos_limpios$PadresHijos) # 0.7281027
max(datos_limpios$PadresHijos) - min(datos_limpios$PadresHijos) # 6

# Tarifa
sd(datos_limpios$Tarifa) # 52.91893
var(datos_limpios$Tarifa) # 2800.413
max(datos_limpios$Tarifa) - min(datos_limpios$Tarifa) # 512.3292

#### Ahora ML: 
modelo <- glm(Vivio ~ Tarifa, family = "binomial", data = datos_limpios)

summary(modelo)
# p-valor:
# Pclase -> 2e-16 ***
# Sexo -> 2e-16 ***
# Edad -> 0.03 97 *
# HermaConyu -> 0.643    
# PadresHijos -> 0.0142 *
# Tarifa -> 1.61e-10 ***ç

# Prediciones:
predicciones <- predict(modelo, newdata = datos_limpios, type = "response") 
predicciones[1:10]

# Construir la tabla
tablita <- data.frame(Original = datos_limpios$Vivio, 
                      prediccionesIA = predicciones)

# Binarizar pero de forma vectorial:   
tablita$prediccionesIA[tablita$prediccionesIA < 0.5] <- 0
tablita$prediccionesIA[tablita$prediccionesIA >= 0.5] <- 1

# Calcular el accuracy
accuracy <- sum(tablita$Original == tablita$prediccionesIA)/nrow(tablita)
accuracy
# Variables:
# Pcalse -> 0.67507 
# Sexo -> 0.780112 (La variable sexo por si sola nos podria detectar cerca del 80%)
# Edad -> 0.5938375
# HermaConyu -> 0.5938375   
# PadresHijos -> 0.5840336
# Tarifa -> 0.6694678

#### Fin de Analisi Univariados

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
DatosCalamarMCPI <- read.csv("D:/MCPI/Análisis_De_Datos/AnalisisDeDatos_Project/Datasets/DatosCalamarMCPI.csv")

# Obtener predicciones:
prediccionesMCPI <- predict(modelo, newdata = DatosCalamarMCPI, type = "response") 
prediccionesMCPI



