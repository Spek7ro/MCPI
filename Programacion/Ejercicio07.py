num = int(input("Ingrese un numero: "))

# Comprobar si el numero es primo

def esPrimo(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

if esPrimo(num):
    print("El numero es primo")
else:
    print("El numero no es primo")
    