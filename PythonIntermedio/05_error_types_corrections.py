import math
from math import pi

# 1. Genera un SyntaxError al imprimir una cadena sin paréntesis.

# Error:
# print "Hola mundo" # Descomentar para error

print("Hola mundo")

# 2. Genera un NameError intentando usar una variable no definida.

# Error:
# print(language) # Descomentar para error

language = "Español"
print(language)

# 3. Genera un IndexError accediendo a un índice inexistente de una lista.

my_list = ["uno", "dos", "tres"]

# Error:
# print(my_list[5])  # Descomentar para error

print(my_list[2])

# 4. Genera un ModuleNotFoundError al importar un módulo inexistente.

# Error (existe math, no maths):
# import maths  # Descomentar para error

print(math.pi)

# 5. Genera un AttributeError accediendo a un atributo que no existe.

# Error:
# print(math.PI) # Descomentar para error

print(math.pi)

# 6. Genera un KeyError al acceder a una clave inexistente de un diccionario.

my_dict = {"name": "Brais", "age": 37}

# Error:
# print(my_dict["surname"]) # Descomentar para error

print(my_dict.get("surname", "No encontrado"))  # Acceso con valor por defecto

# 7. Genera un TypeError usando tipos incorrectos (índice string en lista).

my_list = [1, 2, 3]

# Error:
# print(my_list["0"]) # Descomentar para error

print(my_list[0])

# 8. Genera un ImportError al importar una función que no existe desde un módulo.

# Error (existe pi, no PI):
# from math import PI  # Descomentar para error

print(pi)

# 9. Genera un ValueError intentando convertir un string no numérico a entero.

# Error:
# my_int = int("10 años") # Descomentar para error

my_int = int("10")
print(my_int)

# 10. Genera un ZeroDivisionError al dividir por cero.

#print(10 / 0)  # Descomentar para error
print(10 / 2)

# 11. Intenta detectar si un error ocurre usando try-except con un KeyError.

my_dict = {"course": "Python"}
try:
    print(my_dict["level"])
except KeyError:
    print("Error: clave no encontrada")
