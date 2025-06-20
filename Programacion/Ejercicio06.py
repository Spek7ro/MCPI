palabra = input("Ingrese una palabra: ")

traduccion = {
    "hola": "hello",
    "adios": "goodbye",
    "malo": "bad",
    "jugar": "play",
    "cafe": "coffee",
    "comer": "eat",
    "beber": "drink",
    "cantar": "sing",
}

if palabra in traduccion:
    print(palabra, "->", traduccion[palabra])
else:
    print("Palabra no existe")
    