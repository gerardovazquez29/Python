def cambiar_letras(tipo):

    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())

    if tipo == "may":
        return mayuscula
    elif tipo == "min":
        return minuscula
    
operacion = cambiar_letras("may")

operacion("objetivo")   #OBJETIVO

print('----------------------')

def decorar_saludo(funcion):
    def otra_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios')
    return otra_funcion

def mayuscula(texto):
    print(texto.upper())

def minuscula(texto):
    print(texto.lower())

mayuscula_decorada = decorar_saludo(mayuscula)
mayuscula_decorada('hola')  #HOLA

print('----------------------\n')

minuscula_decorada = decorar_saludo(minuscula)
minuscula_decorada('JOVEN')  #joven

