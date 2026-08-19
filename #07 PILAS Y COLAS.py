"""
Ejecicio = Pila/Stack (LIFO =  Last in First Out)
"""

stack = []
# push
stack.append(1) #Push (cuando apilamos un elemento a un stack)
stack.append(2)
stack.append(3)
print(stack)

# pop (Cuando quitamos elementos del stack)
stack_item = stack[len(stack) - 1]
del stack[len(stack) - 1]
print(stack_item)

print(stack.pop())

print(stack)

# Cola/Queue (FIFO = First in First Out)

queue = []

# enqueue
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

# dequeue
queue_item = queue[0]
del queue[0]
print(queue_item)

print(queue.pop(0))

print(queue)

"""
- Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 """

# Web

def web_navigation():

    stack = []

    while True:

        action = input(
            "añade una url o interactua con las palabras adelante/atras/salir: "
        )

        if action == "salir":
            print("Saliendo del WebNav.")
            break
        elif action == "adelante":
            pass
        elif action == "atras":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(action)

        if len(stack) > 0:
            print(f"Has navegado a la web: {stack[len(stack) - 1]}.")
        else:
            print("Estas en la pagina de inicio.")


web_navigation()

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