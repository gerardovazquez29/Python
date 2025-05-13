

# .json file
import json
# 1. Crea un archivo JSON y escribe un diccionario en él.

json_file = open("data.json", "w+")

data_dict = {
    "name": "Gerardo",
    "surname": "Vazquez", 
    "age": 43, 
    "country": "Tlaquepaque",
    "Lenguajes": ["Python", "PHP", "Javascript"]
    }
json.dump(data_dict, json_file, indent=2)
json_file.close()

# 2. Abre el archivo JSON y lee su contenido.

with open("data.json", "r") as json_file:
    for line in json_file.readlines():
        print(line)
# 3 lo convierte en un diccionario

json_dict = json.load(open("data.json"))
print(json_dict)