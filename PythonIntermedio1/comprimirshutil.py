
import shutil

# carpeta_origen = 'D:\\programacion\\basesPython\\carpeta_superior'

# archivo_destino = 'todo_comprimido'

# shutil.make_archive(archivo_destino, 'zip', carpeta_origen)

# descomprimir archivos

shutil.unpack_archive('todo_comprimido.zip', 'extraccion_terminada', 'zip')
