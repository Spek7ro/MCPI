variable = 'Hola mundo'
variable = 4.3


# Asigancion <- o con =
num1 <- 5
num2 <- 10

print(num1 + num2)

# en R los indices de los arreglos inicia desde 1

# Todos los tipos de datos son vectores 
# Exiten valores infinitos Inf
# Valores faltantes NaN (not a number)

# Tipo entero
x <- 45L
x

cadena <- "Hola desde R"

# Para saber el tipo de dato de una variable
class(x)
class(cadena)
class(variable)

# Autos DataSet
class(Dataset_01)
class(Dataset_01$Coche)
class(Dataset_01$Kms)
class(Dataset_01$Comprar)

# Numero de reglones 
nrow(Dataset_01)

# Numero de columnas
ncol(Dataset_01)

# Nombre de las columnas
colnames(Dataset_01)

# Vectores y listas, para crear un vector se usa c
vector <- c(3,4,5,2,4) 
vector
letras <- c("c","d","a","k")
letras
# Crear un vectro con los numeros del 1 al 10
numeros <- 1:10
numeros

# Ciclo for para recorrer un vector
for (i in vector) {
  print(i)
} 

# Creando un vector con ciertas propiedades
vector2 <- vector("numeric", 20)
vector2

# Un vector todos los datos deben ser del mismo tipo
vector3 <- c(1.2, "w")
vector3
vector4 <- c(TRUE, 2)
vector4

# Convertir el tipo de datos de un vector (Explicita)
x <- c("1", "2", "3", "4", "5")
class(x)
numeros <- as.numeric(x)
class(numeros)
print(numeros)

# Si el caracter no se puede convertir se pone un NAs

# Matrices 
m <- matrix(nrow = 2, ncol = 3)
m
dim(m)
# en las marices siempre se crean atravez de las columnas

# pegar dos matrices (union)
x <- 1:3
y <- 10:12
# Unir de forma de columnas
cbind(x, y)
# Unir por filas
rbind(x,y)

# Agregar un nuevo reglon a un dataset 
rbind(Dataset_01, c("Leon", 40000, "NO"), c("Versa", 30000, "SI"))

# Listas: tipo especial de vector (cada elemnto de la lista es un vector) 
lista <- list(1, c("a", "b", "c"), TRUE, 1 + 4i)
lista

# Factores: forma de respresentar los datos que son categoricos 
# los numeros se asignan de orden alfabetica (1, 2)
factor <- factor(c("YES", "NO", "YES", "YES", "NO"))
factor
table(factor)
unclass(factor)


# asignar los numeros de forma explicita
factor <- factor(c("YES", "NO", "YES", "YES", "NO"), levels = c("yes", "no"))
factor

# Na y NaN
x <- c(1, 2, NA, 10, 3)
is.na(x)
is.nan(x)

# Dataframes 
df <- data.frame(alumno = c("Omar", "Rocio", "Cristian"), 
                 edad = c(32, 22, 33), 
                 sexo = as.factor(c("Hombre", "Mujer", "Hombre")))
df

# Se acceden medianrte indices
df[2,1]

# Si quiero todos los alumnos que sean mayores de 25 años 
df[df$edad > 25, ]

# encontrar NA
is.na(df$edad)

# Estructuras de control if
var <- 25
if (var > 18) {
  print("Si puede tomar alcohol")
} else {
  print("No puede tomar alcohol")
}

# Ciclo for
vector <- 1:10
for (i in vector) {
  print(i)
}

# Imprimir los numeros del 1-20, pero saltarse del 15 al 18
for (num in 1:20) {
  if (num < 15 || num > 18) {
    print(num)
  }
}

# Funcion seq_along
vector <- c(1,2,3,4,5,6,7,8,9)

for (i in 1:9) {
  print(vector[i])
}

for (i in seq_along(vector)) {
  print(vector[i])
}

# ciclo while
count <- 0
while (count < 10) {
  print(count)
  count <- count + 1
}

# Next y return
for (i in 1:50) {
  if (i <= 20) {
    next
  }
  print(i)
}


# Ejercicio 1:
# dado x <- c(3,8,1,10,5), recorre el vector y caclucla la suma de todos los numeros
# y si la suma es mayor a 20 imprime "Hurray"  de lo contario imprime "Naaah"
x <- c(3,8,1,10,5)
#suma1 = sum(x)
suma = 0

for (num in x) {
  suma = suma + num
}

if (suma > 20) {
  print("Hurray")
} else {
  print("Naaah")
}


# Ejercicio 2:
# Carga un dataset llamado mtcars y cuenta cuantos coches tienen un mpg > 20
# muestra el total
datos <- mtcars
datos

carros_mpg <- c(datos$mpg)
class(carros_mpg)

contador <- 0
for (mpg in carros_mpg) {
  if (mpg > 20) {
    contador <- contador + 1
  }
}
contador

# Ejercicio 3:
suma = 0
for (i in carros_mpg) {
  suma <- suma + i
}

promedio = suma / NROW(datos$mpg)
promedio

mean(datos$mpg)

# Dado el vector x <- c(1,2,3,4,5,6,7,9)
# Imprimir los valores mayores a 3 y menores a 7, imprimir su suma
x <- c(1,2,3,4,5,9,7,6)
suma = 0

for (num in x) {
  if (num > 3 && num < 7) {
    print(num)
    suma <- suma + num
  }
}
suma

# Ejercicio 2: imprimir de forma decendente el vector x 
for (i in length(x):1) {
  print(x[i])
}

# Imprimr los valores menores a 5
for (num in x) {
  if (num < 5) {
    print(num)
  }
}

# 4
acumulador = 0
for (num in x) {
  print(acumulador)
  acumulador <- acumulador + num
}

# Valor mas grande del vector x
max(x)

# Valor mas pequeño del vector x
min(x)

# Funciones (las funciones tienen sobrecaraga de argumntos)
args(lm)

calcularMin <- function(vector) {
  aux_min <- vector[1]
  
  for (num in vector) {
    if (num < aux_min) {
      aux_min <- num
    }
  }
  return(aux_min)
}

vector <- c(20,78,5,3,90)
calcularMin(vector)


# Funcion suma de un vector
sumaVector <- function(vector) {
  suma <- 0
  for (num in vector) {
    suma <- suma + num
  }
  return(suma)
}

sumaVector(vector)

# Funcion de promedio de un vector
promedio <- function(vector) {
  return(sumaVector(vector) / length(vector))
}

promedio(vector)

# funncion para calcular la desviacion estandar
desviacionEstandar <- function(vector) {
  suma <- 0
  for (num in vector) {
    suma <- suma + ((num - promedio(vector))^2  
  }
  
  desviacion <- (1 / (length(vector) - 1)) * suma
  desviacion <- sqrt(desviacion)
  return(desviacion)
}

vector <- c(1,2,4,5,6,7)
desviacionEstandar(vector)

# Funcion que convierta de grados centigrados a Farenheit
centigrados_a_Farenheit <- function(grados_centigrados) {
  grados_F <- (grados_centigrados * 1.8) + 32
  return(grados_F)
} 

centigrados_a_Farenheit(23)

# Funcion que convierta de grados Farenheit a centigrados
Farenheit_a_centigrados <- function(garados_Farenheit) {
  grados_c <- (garados_Farenheit - 32) / 1.8
  return(grados_c)
}

Farenheit_a_centigrados(200)

# Funcion que calcule si es impar o para
parOImpar <- function(n) {
  if (n %% 2 == 0) {
    print("Es par")
  } else {
    print("Es impar")
  }
}

parOImpar(5)
parOImpar(10)
parOImpar(3)
