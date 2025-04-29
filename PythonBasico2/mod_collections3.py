
from collections import namedtuple

mi_tupla = (500,18,65)

print(mi_tupla[1]) # 18

Persona = namedtuple('Persona', ['nombre','altura','peso'])

ariel = Persona('Ariel', 1.80, 82)
print(ariel.nombre) # Ariel