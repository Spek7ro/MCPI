num = int(input("Ingrese un numero: "))

# Comprobar si el numero es primo

def esPrimo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

if esPrimo(num):
    print("El numero es primo")
else:
    print("El numero no es primo")
    