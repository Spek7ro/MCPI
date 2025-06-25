frase = input("Ingresa una frase: ")

analisis = {}

frase_minusculas = frase.lower()

analisis["numero_caracteres"] = len(frase)
analisis["numero_palabras"] = len(frase_minusculas.split())
analisis["numero_vocales_a"] = frase_minusculas.count("a")
analisis["numero_vocales_e"] = frase_minusculas.count("e")
analisis["numero_vocales_i"] = frase_minusculas.count("i")
analisis["numero_vocales_o"] = frase_minusculas.count("o")
analisis["numero_vocales_u"] = frase_minusculas.count("u")

# print(analisis)

for key, value in analisis.items():
    print(key, ":", value)

