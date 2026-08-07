"""
Operadores #Recordar print(f"") para el formato del Op #Operadores de Aplican tanto numeros como cadenas de texto como a objetos
"""

# Operador Aritemeticos 
print(f"Suma: 10+3= {10+3}") #interpolacion {}  
print(f"Resta: 10-3= {10-3}")
print(f"Multiplicacion: 10*3 = {10*3}")
print(f"Division: 10 / 3 = {10/3}")
print(f"Modulo: 10 % 3 = {10*3}") #Resultado Entero
print(f"Exponente: 10 ** 3 = {10 ** 3}")
print(f"Division Entera: 10 // 3 = {10//3}")

#Operadores de Comparacion #sepueden con numeros y letras o variables
print(f"igualdad: 10==3 es {10==3}")
print(f"desigualdad: 10 != 3 es {10 != 3}")
print(f"Mayor que: 10 > 3 es {10 > 3}")
print(f"Menor que: 10 < 3 es {10 < 3}")
print(f"Mayor o igual que: 10 >= 3{10 >= 3}")
print(f"Menor o igual que: 10 <= 3{10 <= 3}")
print(f"Mayor o igual que: 10 >= 10 {10 >= 10}") # >= o <= True or False Terminal Segun la Realidad.

#Operadores Logicos 
print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}") #Para que AND && sea TRUE tienen que ser verdadero AMBOS.
print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 4 es {10 + 3 == 13 or 5 - 1 == 4}")
print(f"OR ||: 10 + 3 == 14 or 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4}") #El Resultado va ser TRUE en la Terminal porque se cumple una de las condiciones Logicas.
print(f"NOT !: 10 + 3 == 14 es {10 + 3 == 14}") 
print(f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14}") #Dara TRUE ya que la Condicion se cumple al ser incorrecto el Resultado #es una Realidad

#Operadores de Asignacion 
my_number = 11 #asignacion o Op de Asignacion # = sirve para asignar el numero a la variable en este caso "my_number"
print(my_number)
my_number += 1 # suma y Asignacion 
print(my_number)
my_number -= 1 #Resta y Asignacion  
print(my_number)
my_number *= 2 #Multiplicacion y Asignacion
print(my_number)
my_number /= 2 #Division y Asignacion
print(my_number)
my_number %= 2 #Modulo y Asignacion 
print(my_number)
my_number **= 1 #Exponente y Asignacion
print(my_number)
my_number //= 1 #Division Entera y Asignacion
print(my_number)

#Operadores de Indentidad #Sirven para comparar valores pero en la posicion de memoria
my_new_number = 1.0
print(f"my_number is my_new_number es {my_number is my_new_number}") #da False porque tiene Diferentes valores de memoria
my_new_number = my_number 
print(f"my_number is my_new_number es {my_number is my_new_number}") #Da True porque ahora "my_new_number ahora tiene el mismo valor que my_number" #la identidad es la misma
print(f"my_number is not my_new_number es {my_number is not my_new_number}") #agregando el not para negar la identidad.

# Operadores de Pertenencia #Algo pertene a algo
print(f"'a' in Mauricio' = {'a' in 'Mauricio'}") #Revisa que "a" esta dentro de "Mauricio" #True ya que si pertenece o si esta dentro del conjunto
print(f"'b' not in Mauricio' = {'b' not in 'Mauricio'}") #False ya que la 'b' no esta dentro de Mauricio o del conjunto

# Operadores de bit # se usan para ver operadores de bits 
a = 10 # 1010 #Numeros o valores en Binario
b = 3 # 0011
print(f"AND: 10 & 3 = {10 & 3}") # Resultado a nivel de bit 0010 = 2
print(f"OR: 10 | 3= {10 | 3}") #1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}") #1001
print(f"NOT: ~10 = {~10}") #da Negativo por que esta inviertiendo el resultado Bit a Bit sobre esa respresentacion del 10
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") #0010 es el valor binario que se le asigno a 2
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}") #101000  esto es basicamente 40 binario

"""
Estructuras de Control
"""

# Condicionales

my_string = "Mauricio"

if my_string == "Mauricio":
    print("my_string es 'Mauricio'")
elif my_string == "Mapiedra":
    print("my_string es 'Mapiedra'")
else:
    print("my_string no es 'Gutierrez' ni 'Rojas'")

# Interativas 

for i in range(11):  #FOR sirve para crear bucles.
    print(i)

i = 0   

while i <= 10: #para que el buclue se ejecute mientras la condicion se cumpla, El valor de i sea menor que 10 sigue el bucle hasta que no se cumpla la condicion
    print(i) #Bucle infinito
    i += 1  # suma +1 por cada bucle

# Manejo de Excepciones

try:
    print(10/0) #Error 100% ya que es imposible
except:
    print("Se ha producido un error") 
finally:
    print("Ha finalizado el manejo de excepciones") 


"""
Retro Extra
"""

for number in range(10 , 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0: #condicion 1: para que solo muestre pares , Condicion 2: para que se salte el 16, condicion 3: para que sea multiplo de 3 con el modolu.
         print(number) #Agregar doble TAB 

