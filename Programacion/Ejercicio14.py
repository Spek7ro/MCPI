lista_tareas = []

while True:
    print('''
          1) Agregar tarea.
          2) Ver tareas.
          3) Marcar tarea como completada.
          4) Salir.
          ''')
    opcion = int(input("Opción: "))
    if opcion == 1:
        print("Ingresa la tarea a agregar:")
        tarea = input()
        lista_tareas.append(tarea)
        print(f"Tarea {tarea} agregada con éxito.")
    elif opcion == 2:
        print("Tareas:")
        if lista_tareas:
            for indice, tarea in enumerate(lista_tareas):
                print(indice + 1, "-", tarea)
        else:
            print("No hay tareas.")
    elif opcion == 3:
        print("Ingresa el número de la tarea a marcar como completada:")
        indice = int(input())
        if indice > 0 and indice <= len(lista_tareas):
            tarea_completada = lista_tareas.pop(indice - 1)
            print("Tarea", indice, "marcada como completada:", tarea_completada)
            continue
        else:
            print("Esa tarea no existe.")
            continue
    elif opcion == 4:
        print("Saliendo...")
        break
    else:
        print("Opción no válida.")
        continue
      