dic_divisas = {
  'Euro': '€', 
  'Dollar': '$', 
  'Yen': '¥'
}

nombre_divisa = input("Ingrese el nombre de una divisa (Euro, Dollar o Yen): ")

# Verificar si la divisa está en el diccionario y mostrar el resultado
if nombre_divisa in dic_divisas:
    print(f"El símbolo de {nombre_divisa} es: {dic_divisas[nombre_divisa]}")
else:
    print("La divisa no está en el diccionario.")
