nombre: str = input("Ingrese su nombre: ")
edad: int = int(input("Ingrese su edad: "))

calificaciones: list = [7, 9, 8 , 10, 9]

promedio: float = sum(calificaciones) / len(calificaciones)

print(f"El alumno: {nombre}, tiene {edad} años y su promedio es {promedio}")
