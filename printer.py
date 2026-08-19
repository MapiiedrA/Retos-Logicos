def shared_printer():

    queue = []

    while True:

        action = input("Añade un documento o selecciona imprimir/salir: ")

        if action == "Salir":
            break
        elif action == "imprimir":
            if len(queue) > 0:
                print(f"Imprimiendo: {queue.pop(0)}")
        else:
            queue.append(action)

            print(f"Cola de impresion: {queue}")


shared_printer()