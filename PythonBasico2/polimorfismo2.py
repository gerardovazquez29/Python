
palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)


for dato in [palabra, lista, tupla]:
    print("\n" + str(len(dato))) # 12  3  4



class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")

harypoter = Mago()
harcher = Arquero()
L = Samurai()

personajes = [harypoter, harcher, L]

for personaje in personajes:
    personaje.atacar()


def personaje(personaje):
    personaje.atacar()        # Ataque mágico  Lanzamiento de flecha Ataque con katana    

class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")


print("\nDefensas de los personajes:")

harypoter = Mago()
harcher = Arquero()
L = Samurai()

personajes = [harypoter, harcher, L]

for personaje in personajes:
    personaje.defender()

def personaje_defender(personaje):
    personaje.defender()                # Escudo mágico Esconderse  Bloqueo            
