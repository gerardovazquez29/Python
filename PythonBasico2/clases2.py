

class Persona:
    especie = "humano"

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}")

    def cumplir_anios(self, estado_humor):
        print(f"Cumplir {self.edad + 1} años me pone {estado_humor}")


juan = Persona("Juan", 37)
juan.saludar()
juan.cumplir_anios("Contento")


class Perro:
    def ladrar(self):
        print("Guau!")
    
pluto = Perro()
pluto.ladrar()

class Mago:
    def lanzar_hechizo(self,):
        print("¡Abracadabra!")

merlin = Mago()
merlin.lanzar_hechizo()

class Alarma:
    
    def postergar(self, cantidad_minutos):
    
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")
        
alarma = Alarma()
alarma.postergar(30)





class Personaje:
    
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas
    
    
    def lanzar_flechas(self):
        self.cantidad_flechas -= 1
        print(f"lanzo {self.cantidad_flechas}")

apache = Personaje(4)
apache.lanzar_flechas()