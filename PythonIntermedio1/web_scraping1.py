
import bs4
import requests

resultado = requests.get("https://www.escueladirecta.com/l/products")

sopa = bs4.BeautifulSoup(resultado.text, "lxml")

imagenes = sopa.select(".ProductImage")
for i in imagenes:
    if i.has_attr("src"):
        print(i["src"])
    else:
        print("No hay imagen")

# Descargar imagenes
for img in imagenes:
    if img.has_attr("src"): 
        # Obtener la URL de la imagen
        imagen_url = img["src"]
        # Realizar la solicitud para descargar la imagen
        imagen_curso1 = requests.get(imagen_url)
         # Guardar la imagen
        with open('mi_imagen.jpg', 'wb') as f:
            f.write(imagen_curso1.content)

        print(f"Imagen descargada: {img['src']}")
        break # Salir después de guardar la primera imagen
    else:
        print("No hay imagen")
        break


