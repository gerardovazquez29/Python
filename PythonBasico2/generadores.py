def mi_generador():
    yield 5

g = mi_generador()
print(next(g)) # 5


def mi_generador():
    for i in range(1, 5):
        yield i

g = mi_generador()
print(next(g)) # 5, 1


def secuencia_infinita():
    num = 0
    while True:
        num += 1
        yield num

generador = secuencia_infinita()
print(generador)  #<generator object secuencia_infinita at 0x000002C7BCA64880>



def multliplos_siete():
    num = 1
    while True:
        yield 7 * num
        num += 1

multiplos = multliplos_siete()
print(next(multiplos)) # 7


def mensaje():
    x = "Te quedan 3 vidas"
    yield x
    x = "Te quedan 2 vidas"
    yield x
    x = "Te queda 1 vida"
    yield x
    x = "Game Over"
    yield x

perder_vida = mensaje()
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))