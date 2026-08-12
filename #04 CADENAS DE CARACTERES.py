"""
Operaciones 
"""
s1 = "Hola"
s2 = "Python"

# Concatenacion
print(s1 + ", " + s2 + "!")

# Repeticion
print(s1 * 3) 

# Indexacion
print(s1[0] + s1[1] + s1[2] + s1[3])

# Longitud
print(len(s2))

# Slicing (porcion)
print(s2[2:5])
print(s2[2:])
print(s2[0:2])
print(s2[:2])

# Busqueda
print("a" in s1)
print("i" in s1)

# Reemplazo
print(s1.replace("o", "a"))

# Division
print(s2.split("t")) #por definicio el split desecha la parte donde hace el split , pero se puede recuperar.

# Mayusculas y Minusculas
print(s1.upper()) #mayus
print(s1.lower()) #minus
print("mauricio piedra".title()) #deja la primera letra de cada texto en mayusculas
print("mauricio piedra".capitalize()) #solo pone la primera letra en mayus

# Eliminacion de espacios al principio y al final
print(" mauricio piedra ".strip())
print(" mauricio piedra ".strip() + "@MapiiedrA")

# Busqueda al principio y al final
print(s1.startswith("Ho"))
print(s1.startswith("Py"))
print(s1.endswith("la"))
print(s1.endswith("on"))

s3 = "Mauricio Piedra @MapiiedrA"

# Busqueda de pocision 
print(s3.find("Piedra"))
print(s3.find("M"))
print(s3.lower().find("p")) #se queda con la primera vez que aparece la letra.

# Busqueda de Ocurrencias
print(s3.lower().count("m")) #puedo poner un solo caracter hasta una palabra completa.

# Formateo
print("Saludo: {}, lenguaje: {}!".format(s1, s2)) #Intercambia las llames por la variable, en el orden que se pone en el formateo

# Interpolacion
print(f"Saludo: {s1}, lenguaje: {s2}!") #"f" hace entender que todo lo que esta entre llaves es una Variables

# Transformacion en lista de caracteres
print(list(s3)) #curiosidad

# Transformacion de lista en Cadena
l1= [s1, ", ",  s2, "!"]
print("-".join(l1)) #Criterio de union entre las comillas , puede ser un espacio en blanco.

# Trasformaciones numericas
s4 = "123456"
s4 = int(s4)  # para numeros enteros
print(s4)

s5 = "123456.123"
s5 = float(s5) #para numeros decimales
print(s5)

# Comprobaciones varias
s4 = "123456"
print(s1.isalnum())
print(s1.isalpha())
print(s4.isalpha())
print(s4.isnumeric())

"""
EXTRA : * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */
 """

def check(word1: str, word2: str):

    # Palindromos : es una palabra, frase o número que se lee exactamente igual de izquierda a derecha que de derecha a izquierda.
    print(f"¿{word1} es un palindromo?: {word1 == word1[::-1]}")
    print(f"¿{word2} es un palindromo?: {word2 == word2[::-1]}")

    # Anagramas: juego de palabras que consiste en cambiar el orden de las letras de una palabra o frase para crear otra nueva.
    print(f"¿{word1} es un Anagrama de {word2}?: {sorted(word1) == sorted(word2)}")
    print()

    # Isogramas : línea en un mapa o gráfico que conecta puntos que tienen el mismo valor, como la temperatura o la presión.
    print(f"¿{word1} es un Isograma?: {len(word1) == len(set(word1))}")
    print(f"¿{word2} es un Isograma?: {len(word2) == len(set(word2))}")

    # Prueba
    def isogram(word: str) -> bool:
        word_dict = dict()
        for character in word:
            word_dict[character] = word_dict.get(character, 0) + 1

        isogram_result = True
        values = list(word_dict.values())
        isogram_len = values[0]
        for word_count in values:
            if word_count != isogram_len:
                isogram_result = False
                break

        return isogram_result

    print(f"¿{word1} es un Isograma?: {isogram(word1)}")
    print(f"¿{word2} es un Isograma?: {isogram(word2)}")

check("radar", "pythonpythonpythonpython")   
#check("amor", "roma")