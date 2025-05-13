
from collections import deque

lista_ciudades= deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])

lista_ciudades.append("Lisboa")       # Agrega "Lisboa" al final
lista_ciudades.appendleft("Tokio")   # Agrega "Tokio" al inicio
lista_ciudades.pop()                 # Elimina y devuelve "Lisboa"
lista_ciudades.popleft()             # Elimina y devuelve "Tokio"

print(lista_ciudades)