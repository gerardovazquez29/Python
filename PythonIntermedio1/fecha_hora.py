
from datetime import datetime


fecha_hora = datetime.now() 
fecha = fecha_hora.date()
hora = fecha_hora.time()
print(f"hoy es: {fecha} y la hora es:{hora.hour}") 

formato_personalizado = fecha_hora.strftime("%d/%m/%y %H:%M:%S")
print(f"Fecha y hora en formato personalizado. {formato_personalizado}")