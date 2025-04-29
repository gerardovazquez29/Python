
from collections import Counter

numeros = [8, 6,9,5,4,5,5,5,8,7,4,5,4,4,3]

print(Counter(numeros))  #Counter({5: 5, 4: 4, 8: 2, 6: 1, 9: 1, 7: 1, 3: 1})

frase = "al pan pan y al vino vino"
print(Counter(frase.split())) #Counter({'al': 2, 'pan': 2, 'vino': 2, 'y': 1})

serie = Counter([1,1,1,1,1,1,2,2,2,2,3,3,3,3,3,3,3,4])
print(serie.most_common()) #[(3, 7), (1, 6), (2, 4), (4, 1)]

lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]

contador = Counter(lista) # [(3, 7), (1, 6), (2, 4), (4, 1)]