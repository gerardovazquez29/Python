
from collections import defaultdict

mi_dic = defaultdict(lambda: "nada")
mi_dic['uno'] = 'verde'
print(mi_dic['dos']) #nada

print(mi_dic) # defaultdict(<function <lambda> at 0x000001F15540A2A0>, {'uno': 'verde', 'dos': 'nada'})


mi_diccionario = defaultdict(lambda: "Valor no hallado")

mi_diccionario['edad'] = 44
print(mi_diccionario['estatura']) # Valor ni hallado
print(mi_diccionario)