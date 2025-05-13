
import re


chequear  = input("Ingrese un email; ")
def verificar_email(chequear):
    patron = r'@\w+\.com'
    verificar = re.search(patron,chequear)
    if verificar:
        return"Ok"
    else:
        return "La dirección de email es incorrecta"
print(verificar_email(chequear))



frase = input("saluda porfavor: ")
def verificar_saludo(frase):
    patron = r'^Hola'
    verificar = re.search(patron,frase)
    if verificar:
        return "Ok"
    else:
        return "No has saludado"
print(verificar_saludo(frase))


codigo_postal = input("Ingrese su codigo postal: ") 
def verificar_cp(cp):
    patron = r'\w{2}\d{5}'
    verificar = re.search(patron,cp)
    if verificar:
        return "Ok"
    else:
        return "El código postal ingresado no es correcto"
print(verificar_cp(codigo_postal))
