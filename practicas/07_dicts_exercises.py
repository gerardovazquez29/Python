# 1. Crea un diccionario con las claves name, age, y country,
#  asignando valores a cada una. Imprime el diccionario.
my_dict ={'name':'Gerardo', 'age':42, 'country':'Mexico'}
#*print(my_dict)

# 2. Accede al valor de la clave name en el diccionario.
#*print(my_dict.get('name'))

# 3. Añade una nueva clave job con el valor "Programador" al diccionario del punto anterior. 
# Imprime el diccionario actualizado.
my_dict['job'] = 'Programador'
#*print(my_dict)

# 4. Modifica el valor de la clave age en el diccionario para que sea 38. 
# Imprime el diccionario actualizado.
my_dict['age'] = 38
#*print(my_dict)

# 5. Elimina la clave country del diccionario e imprime el diccionario resultante.
my_dict.pop('country')
#*print(my_dict)

# 6. Crea un diccionario donde las claves sean números del 1 al 5 y los valores sean 
# sus cuadrados (ejemplo: 1: 1, 2: 4, ...).
numeros = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
#*print(numeros)

# 7. Verifica si la clave age está presente en el diccionario 
# {"name": "Brais", "age": 37, "country": "Galicia"}.
dict = {"name": "Brais", "age": 37, "country": "Galicia"}
#*print('age' in dict) # True

# 8. Imprime solo las claves del diccionario.
#*print(dict.keys())

# 9. Convierte las claves del diccionario en una lista e imprime la lista resultante.
dict_keys = list(dict.keys())
#*print(dict_keys) # ['name', 'age', 'country']

# 10. Crea un nuevo diccionario a partir de una lista de claves ["name", "age", "job"] 
# usando fromkeys(), asignando a todas las claves el valor "Desconocido".
my_list = ["name", "age", "job"]
nuevo_dict = dict.fromkeys(my_list, "Desconocido")
print(nuevo_dict) # {'name': 'Desconocido', 'age': 'Desconocido', 'job': 'Desconocido'}

