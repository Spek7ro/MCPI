#Dado el vector x<-c(1,2,3,4,5,6,7,8,9)
x <- c(1,2,3,4,5,6,7,8,9)
x

#1, encontrar los numeros mayores a 3 y menores a 7
#imprimir la suma de ellos R = 15
suma <- 0
for (num in x) {
  if (num > 3 && num < 7) {
    print(num)
    suma <- suma + num
  }
}
suma

#2 imprimir en orden descendente el vector
for (i in length(x):1) {
  print(x[i])
}

#3, imprimir solo los valores menores a 5
for (num in x) {
  if (num < 5) {
    print(num)
  }
}

#4, imprimir el valor acumulado ej:1, 3, 6, 10, 15...
acumulado <- 0
for (num in x) {
  acumulado <- acumulado + num
  print(acumulado)
}

#5, imprimir el valor más grande
aux <- x[1]

for (num in x) {
  if (num > aux) {
    aux <- num
  }
}
aux

#6, imprimir el valor más pequeño
#min(x)
aux <- x[1]

for (num in x) {
  if (num < aux) {
    aux <- num
  }
}
aux

#7, obtener la suma total de los elementos en el arreglo pero
#8, a cada elemento del arreglo se le restará el "promedio"
# y se sumara el total   === Sum(xi - mean)
suma_total <- 0

for (num in x) {
  suma_total <- suma_total + num
}
print(suma_total)

promedio <- suma_total / length(x)
promedio
suma_dif <- 0

for (num in x) {
  suma_dif <- suma_dif + (num - promedio)
}

print(suma_dif)

#9, a cada elemento del arreglo se le restará el "promedio"
#   el resultado de esta suma, se elevará al cuadrado ^2
#   y se sumara el total   === Sum(xi - mean)^2
suma_cuadrados <- 0
for (num in x) {
  suma_cuadrados <- suma_cuadrados + (num - promedio)^2
}

suma_cuadrados

#10, Obtemer el rango dinamico  = max() - min() de un areglo
aux_max <- x[1]
aux_min <- x[1]

for (num in x) {
  if (num > aux_max) {
    aux_max <- num
  }
  if (num < aux_min) {
    aux_min <- num
  }
}

rango_dinamico <- aux_max - aux_min
print(rango_dinamico)

# max(x) - min(x)


