n: int = int(input("Ingrese un numero: "))

#suma_enteros: int = sum(range(1, n + 1))
suma_enteros: int = n * (n + 1) // 2

print(f"La suma de los numeros enteros entre 1 y {n} es: {suma_enteros}")
