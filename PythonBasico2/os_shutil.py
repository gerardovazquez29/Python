import os

print(os.getcwd())

archivo_path = os.path.join(os.getcwd(), 'curso.txt')

with open(archivo_path, 'a') as archivo:
    archivo.write('texto de prueba\n')

with open(archivo_path, 'r') as archivo:
    print(archivo.read())