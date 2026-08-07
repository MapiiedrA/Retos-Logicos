### Funciones definidas por el Usuario ###

# Funcion Simple

def greet():
    print("Hola, Python!")

greet() 

#Funcion con Retorno

def return_greet():
    return "Hola, Python!"

greet = return_greet() #para guardar el retorno en una variable
print(return_greet) #impresion simplete sin guardado en una variable

# Funcion con un Argumento

def arg_greet(name):
    print(f"Hola, {name}!") #Requiere complir la condicion de name , para que se ejecute

arg_greet("Mauricio") #condicion completa, ya que ahora si tiene el parametro name completo o relleno.

# Funcion con varios argumentos

def args_greet(greet, name):
    print(f"{greet}, {name}!") #Requiere cumplir ambas condiciones "greet" and "name" sino va dar error.

args_greet("hi", "Mauricio") #se cumplen los requisitios de las Funciones para que se complete el retorno.
args_greet("Mauricio", "Hi") #se Invierte el Saludo.
args_greet(name="Mauricio", greet="Hi") #agregando parametros para que se cumpla la condicion de forma correcta sin importar el orden.

# Funcion con Argumento Predeterminado 

def default_arg_greet(name="Python"): #si no se cumple la condicion de name ahora pone por defecto el valor "Python"
    print(f"Hola, {name}!")

default_arg_greet("Mauricio") #Con condicion de name Rellena.
default_arg_greet() #sin Condicion de name, solo valor predeterminado.

# Funciones con Argumentos y Retorno

def return_args_greet(greet, name):
    return f"{greet}, {name}!"

print(return_args_greet("Hi", "Mauricio"))

# Funcion con retorno de varios valores

def multiple_return_greet():
    return "Hola", "Python"

greet, name = multiple_return_greet()
print(greet)
print(name)

# Funciones con un numero variable de argumentos

def variable_arg_greet(*names): # * antes del name significa que puede ser mas de un "name".
    for name in names:
        print(f"Hola, {name}!")

variable_arg_greet("Python", "Mauricio", "MapiiedrA", "World")

#Funciones con numero variable de argumentos con palabras clave

def variable_arg_greet(**names):  # ** significa palabra clave de argumentos
    for key, value in names.items():
        print(f"{value} ({key})!")

variable_arg_greet(
     language="Python", 
     names="Mauricio", 
     alias="MapiiedrA", 
     age=32
     )

### Funciones dentro de funciones ###

def outer_function():
    def inner_fuction():
        print("Funcion interna: Hola, Python !")
    inner_fuction()

outer_function()

### Funciones Propias del lenguaje (built-in) ###

print(len("Mauricio"))
print(type(32))
print("Mauricio".upper())

### Variables Locales y Globales ### Ambito o scope #Consejo, Restrigir lo maximo el codigo segun la circunstacia para hacerlo mas seguro.

global_var= "Python"
print(global_var)

def hello_python():
    print(f"Hello, {global_var}")

def hello_python():
    local_var = "Hola"
    print(f"{local_var}, {global_var}")

print(global_var)
# print(local_var) No se puede acceder desde fuera de la funcion

hello_python()

### RETO EXTRA ###

def print_numbers(text_1, text_2)-> int:
    count = 0
    for number in range (1, 101):
        if number % 3 == 0 and number % 5 == 0: #esta condicion debe ser la primera por que sino luego no va afectar a ninguno , ya que los multiplos puede verse afectados por otros
            print(text_1 + text_2)
        elif number % 3 == 0:
            print(text_1)
        elif number % 5 == 0:
            print(text_2)
        else:
            print(number)
            count += 1
    return count

print(print_numbers("Fizz", "Buzz")) #Famoso "Text_1 = Fizz", "Text_2 = Buzz" por si quremos imprimir esto para una prueba tecnica.


