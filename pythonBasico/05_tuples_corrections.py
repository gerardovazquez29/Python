# 1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprímela.

my_tuple = (10, 20, 30, 40, 50)
print(my_tuple)

# 2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muéstralo.

my_tuple = (100, 200, 300, 400, 500)
print(my_tuple[1])

# 3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado.

my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # Esto generará un error: TypeError

# 4. Cuenta cuántas veces aparece el número 3 en la tupla (1, 2, 3, 3, 4, 5, 3).

my_tuple = (1, 2, 3, 3, 4, 5, 3)
print(my_tuple.count(3))

# 5. Encuentra el índice de la primera aparición de la cadena "Python" en la tupla ("Java", "Python", "JavaScript", "Python").

my_tuple = ("Java", "Python", "JavaScript", "Python")
print(my_tuple.index("Python"))

# 6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.

my_tuple1 = (1, 2, 3)
my_tuple2 = (4, 5, 6)
my_tuple = my_tuple1 + my_tuple2
print(my_tuple)

# 7. Crea una subtupla con los elementos desde la posición 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).

my_tuple = (10, 20, 30, 40, 50)
my_subtuple = my_tuple[2:4]
print(my_subtuple)

# 8. Convierte la tupla ("rojo", "verde", "azul") en una lista, cambia el segundo elemento a "amarillo" y vuelve a convertirla en una tupla. Imprime la tupla resultante.

my_tuple = ("rojo", "verde", "azul")
my_list = list(my_tuple)
my_list[1] = "amarillo"
my_modified_tuple = tuple(my_list)
print(my_modified_tuple)

# 9. Elimina una tupla llamada my_tuple usando del y luego intenta imprimirla para ver el resultado.

my_tuple = (1, 2, 3)
del my_tuple

# 10. Crea una tupla con un solo elemento (el número 100) e imprímela. Asegúrate de usar la sintaxis correcta para crear una tupla con un solo elemento.

my_tuple = (100, )
print(my_tuple)
