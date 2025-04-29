
class Cd:

    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        return f"Album: {self.titulo} de {self.autor}"
    
    def __len__(self):
        return self.canciones
    
    def __del__(self):
        print("se ha eliminado mi_cd")

mi_cd = Cd('Pink Floyd', 'The Wall', 24)

print(str(mi_cd))
print(len(mi_cd))
del mi_cd




class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
        
    def __str__(self):
        return f"{self.titulo} de {self.autor}"
    def __len__(self):
        return self.cantidad_paginas
        
mi_libro = Libro('Aves negras', 'Jose', 36)
print(str(mi_libro))
print(len(mi_libro))