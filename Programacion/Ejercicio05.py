lista = [[['naranja', 'pera', 'manzana'], 'limón', 'pepino', ['habanero', 'jalapeño']], 'enchiladas', 'pozole']

print(lista)

# Pera
print(lista[0][0][1])

# Habanero
print(lista[0][3][0])

# Pozole
print(lista[-1])

# [limón, pepino]
print(lista[0][1] +", " + lista[0][2])

# [habanero, jalapeño]
print(lista[0][3])

# Ultimo elemento de la colección de frutas
print(lista[0][0][-1])

# Ultimo elemento de la colección de chiles
print(lista[0][3][-1])

#Mofificar el elemento pepino por [calabaza, zanahoria]
lista[0][2] = ['calabaza', 'zanahoria']

print(lista)
