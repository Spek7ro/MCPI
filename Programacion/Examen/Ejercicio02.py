n = int(input("Ingrese un número entero: "))

if n > 0:
  for i in range(n):
      valor = 1
      for j in range(i + 1):
          print(valor, end=" ")
          valor = valor * (i - j) // (j + 1) 
      print() # salto de línea
else:
  print("El número introducido no es positivo")

'''
N = 9

1
1 1
121
1331
14641
15101051
1 6 15 20 15 6 1
1 7 21 35 35 21 7 1
1 8 28 56 70 56 28 8 1
'''
