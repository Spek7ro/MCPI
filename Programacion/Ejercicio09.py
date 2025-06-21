fecha_nacimiento = input("Ingrese la fecha de nacimiento: ")

# Formato de fecha: dd/mm/aaaa
dia, mes, anio = fecha_nacimiento.split("/")

anio = int(anio)
mes = int(mes)
dia = int(dia)

print(f"Nacio el dia {dia} del mes {mes} del año {anio}")
