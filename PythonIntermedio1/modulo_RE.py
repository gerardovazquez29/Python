
import re
texto = "Si necesitas ayuda, llama al (658)-598-9977 las 24 horas al servicio de ayuda online"

# palabra = 'ayuda' in texto
# print(palabra) # True

patron = 'ayuda'
busqueda = re.search(patron, texto)
print(busqueda)  # <re.Match object; span=(13, 18), match='ayuda'>

busqueda = re.findall(patron, texto)
print(len(busqueda)) # 2

for hallasgo in re.finditer(patron, texto):
    print(hallasgo.span()) # (13, 18) (72, 77) ubicaciones de la palabra 


texto1 = "llama al 564-525-6588 ya mismo"

patron1 = r'\d\d\d-\d\d\d-\d\d\d\d'
resultado = re.search(patron1, texto1)
print(resultado)  # <re.Match object; span=(9, 21), match='564-525-6588'>
print(resultado.group()) #564-525-6588

patron2 = r'\d{3}-\d{3}-\d{4}'
resultado = re.search(patron2, texto1)
print(resultado)  # <re.Match object; span=(9, 21), match='564-525-6588'>
print(resultado.group()) #564-525-6588

patron3 = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
resultado = re.search(patron3, texto1)
print(resultado.group()) #564-525-6588
print(resultado.group(1)) #564
print(resultado.group(2)) #525


# ejemplo

clave = input("clave: ")
patron4 = r'\D{1}\w{7}'
chequear = re.search(patron4, clave)
print(chequear) # clave: e325wsdc  <re.Match object; span=(0, 8), match='e325wsdc'>


texto3 = "No atendemos los jueves por la tarde"
buscar = re.findall(r'[^\s]+', texto3)
print(buscar) # ['No', 'atendemos', 'los', 'jueves', 'por', 'la', 'tarde']
print(''.join(buscar)) # Noatendemoslosjuevesporlatarde

