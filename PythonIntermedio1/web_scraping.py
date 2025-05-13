import bs4
import requests

resultado = requests.get("https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html")

print(resultado.text)

sopa = bs4.BeautifulSoup(resultado.text, 'lxml') 
#print(sopa.select('title')[0].getText()) # Encapsulamiento: Pilares de la Programación Orientada a Objetos 
parrafo_especial = sopa.select('.content p')
for p in parrafo_especial:
    print(p.getText())



