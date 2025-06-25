# Adivina el numero
import random as r

numero_random = r.randint(1, 100)
print(numero_random)

num_intentos = 0

while True:
    num_intentos += 1
    print("¿Cuál es el número?")
    respuesta = int(input())
    if respuesta == numero_random: 
        print("¡¡¡Felicitaciones!! ¡Has acertado! en", num_intentos, "intentos.")
        break
    elif respuesta < numero_random:
        print("El numero secreto es mas alto!!!")
        continue
    elif respuesta > numero_random:
        print("El numero secreto es mas bajo!!!")
        continue
    else:
        print("¡No has acertado! ¡Inténtalo de nuevo!")
        continue
