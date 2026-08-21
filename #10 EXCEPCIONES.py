"""
Ejercicios Excepciones 
"""

try:
    print(10/0)

    my_list = [1, 2, 3, 4]
    print([1, 2, 3, 4][4])
except Exception as e:
    print(f"Se ha producido un error:{e}({type(e).__name__})")

print("Hola, todo sigue!")

"""
EXTRA 
* Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado.
 """

class StrTypeError(Exception):
    pass

def process_params(parameters: list):

    if len(parameters) < 3:
        raise IndexError() 
    elif parameters[1] ==0:
        raise ZeroDivisionError()
    elif type(parameters[2]) == str:
        raise StrTypeError("El Tercer elemento no ser una cadena de texto.")

    print(parameters[2])
    print(parameters[0]/parameters[1])
    print(parameters[2] + 5)

try:
    process_params([1, 2, "Mauricio", 4])
except IndexError as e:
    print("El numero de elementos de la lista debe ser mayor que dos.")
except ZeroDivisionError as e:
    print("El segundo elemento de la lista no puede ser un Cero")
except StrTypeError as e:
    print(f"{e}")
except Exception as e:
    print(f"Se ha producido un error inesperado: {e}")
else:
    print("No se ha producido ningun error")
finally:
    print("El Programa Finaliza sin detenerse.")