
def suma():
    ni = int(input("Imgrese el primer numero: "))
    n2 = int(input("ingrese el segundo numero: "))
    print(ni + n2)
    print("Gracias por sumar")

try:
    # codigo que queremos pprobar
    suma()
except:
    # codigo a ejecutar si no hay un error
    print("Ha ocurrido un error")
else:
    # codigo a ejecutar si hay un error
    print("Todo ha salido bien")
finally:
    # codigo que se va a ejecutar de togos modos
    print("fin del programa")





def pedir_numero():

    while True:
        try:
            numero = int(input("Ingrese un numero: "))
        except:
            print("Ese no es un numero")
        else:
            print(f"ingresaste el numero {numero}")
            break
    print("fin del programa")
pedir_numero()






def suma():
    num1 = int(input( "ingresa un numero: "))
    num2 = int(input("Ingresa otro numero: "))
    try:
        print(num1+num2)    
    except:
        print("Error inesperado")

suma()

        



def cociente(num1, num2):
    try:
        print(num1/num2)
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")
cociente(10, 5)    
        
    



def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("Error al abrir el archivo")        
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")
abrir_archivo("archivo.txt")

