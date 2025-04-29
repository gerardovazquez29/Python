
import time

def  prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista

def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista

inicio = time.time()
prueba_for(140000)
final = time.time()
print(f"Tiempo de ejecucion del for: {final - inicio} segundos") # : 0.012967348098754883 segundos

inicio = time.time()
prueba_while(140000)
final = time.time()
print(f"Tiempo de ejecucion del while: {final - inicio} segundos") #  0.030912160873413086 segundos

