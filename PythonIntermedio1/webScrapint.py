
import requests
from bs4 import BeautifulSoup

url = "https://escueladirecta-blog.blogspot.com/2024/07/por-que-se-utiliza-python-en-ciencia-de.html"

try: 
    respuesta = requests.get(url)
    respuesta.raise_for_status() # Lanza un error si la respuesta no es 200

    html = respuesta.text
    #print(html)  # Imprime el contenido HTML de la página

    soup = BeautifulSoup(html, "html.parser")
    titulos = soup.find_all("b")
    print("titulos de los blogs:")
    for titulo in titulos:
        print(titulo.get_text(strip=True))  # Imprime el texto de cada título sin espacios en blanco

except requests.exceptions.RequestException as e:
    print(f"Error al realizar la solicitud: {e}")

"""
titulos de los blogs:
Las ventajas de Python como lenguaje
Las ventajas derivadas de la comunidad de Python
"""

