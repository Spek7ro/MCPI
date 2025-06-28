inventario = {
  "Poción de agua": 10,
  "Poción de hierro": 20,
  "Poción de oro": 30,
  "Poción de plata": 40,
  "Poción de la suerte": 50,
}

ingredientes_receta = ["agua", "agua", "fuego", "hierro", "hierro", "hierro", "oro", "oro", "plata", "plata"]
    
print("------Inventario de la Tienda-----")
for item, precio in inventario.items():
    print(item, ":", precio)
    
print("------Ingredientes únicos para la poción-----")
ingredientes_unicos = set(ingredientes_receta)
print(ingredientes_unicos)


