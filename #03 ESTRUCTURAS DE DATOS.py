# Listas
my_list = ["Mauricio", "Black", "Wolfy", "Piedra"]
print(my_list)
my_list.append("MapiiedrA") #insercion #sirve para agregar datos a la lista. su orden va ir de acuerdo a su orden de insercion. 
print(my_list)
my_list.remove("Mauricio") #Eliminacion
print(my_list)
print(my_list[1]) #Acceso
my_list[1] = "Cuervillo" #Actualizacion + Insercion de nuevos datos.
print(my_list)
my_list.sort() #ordenacion (por defecto lo hace de forma alfabetica, si fueran numeros seria de menor a mayor)
print(my_list)

# Tuplas #Tipo constructor mas seguro y que sea inmutable.
my_tuple = ("Mauricio", "Piedra", "MapiiedrA", "32")
print(type(my_tuple))
print(my_tuple[1]) #Acceso
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple)) #Ordenacion  #asi creamos un objeto de type tuple 
print(my_tuple)
print(type(my_tuple))

# Sets #set es un Hashset, en los set no se duplican datos.
my_set = {"Mauricio", "Piedra", "MapiiedrA", "32"}
print(my_set)
print(type(my_set))
my_set.add("mapiedra3223@gmail.com")  #Insercion 
print(my_set)
my_set.remove("Mauricio") #Eliminacion
print(my_set)
my_set.update

my_set = set(sorted(my_set)) #NO SE PUEDE ORDENAR, POR DEFINICIO DEL SISTEMA YA ES DESORDENADO.
print(my_set)
print(type(my_set))

# Diccionario

my_dict: dict = {"name":"Mauricio",
                "surname":"Piedra",
                "alias":"MapiiedrA",
                "age":"32"
} #La Diferencia entre un set y un Dict , es que el dict se ordena por clave valor a difencia del set.
my_dict["email"] = "mapiedra3223@gmail.com" #Insercion
print(my_dict)
del my_dict["surname"] #Eliminacion
print(type(my_dict))
print(my_dict["name"]) #Acceso
my_dict["age"] = "33" #Actualizacion
print(my_dict)
my_dict = dict(sorted(my_dict.items())) #Ordenacion #Warm los dicts solo son ordenados en python.
print(my_dict)
print(type(my_dict))

"""
Extra  * Crea una agenda de contactos por terminal.   #match : esto viene a ser Switch en otros lenguajes.
"""

def my_agenda(): 
    agenda = {}

    def insert_contact(name: str):
        """Ask for a phone number and insert it into agenda for given name."""
        phone = input("Introduce el numero de telefono del contacto: ")
        if phone.isdigit() and 0 < len(phone) <= 11:
            agenda[name] = phone
            print(f"Contacto {name} guardado.")
        else:
            print("Debes introducir un numero de telefono con un maximo de 11 digitos.")

    while True:
        print()
        print("1. Buscar Contacto")
        print("2. Insertar Contacto")
        print("3. Actualizar Contacto")
        print("4. Eliminar Contacto")
        print("5. Salir")

        option = input("\nSelecciona una Opcion: ")

        match option:
            case "1":
                name = input("Introduce el nombre del contacto a buscar: ")
                if name in agenda:
                    print(f"El numero de telefono de {name} es {agenda[name]}.")
                else:
                    print(f"El contacto {name} no existe.")
            case "2":
                name = input("Introduce el nombre del contacto: ")
                if name:
                    insert_contact(name)
                else:
                    print("El nombre no puede estar vacio.")
            case "3":
                name = input("Introduce el nombre del contacto a actualizar: ")
                if name in agenda:
                    insert_contact(name)
                else:
                    print(f"El contacto {name} no existe.")
            case "4":
                name = input("Introduce el nombre del contacto a eliminar: ")
                if name in agenda:
                    del agenda[name]
                    print(f"Contacto {name} eliminado.")
                else:
                    print(f"El contacto {name} no existe.")
            case "5":
                print("Saliendo de la Agenda.")
                break
            case _:
                print("Opcion no valida. Elige una opcion del 1 al 5.")


if __name__ == "__main__":
    my_agenda()

#Revisar los Errores de las variables que no funcionan y resto del codigo #Resueltos, faltaba asignar un if a __name__ == "__main__" .
