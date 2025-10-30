import os
import shutil

# Directorio donde están los archivos
source_dir = 'C:\\xampp\\htdocs'


# Crear una función para organizar archivos por extensión
def organize_by_extension(source_dir):
    for filename in os.listdir(source_dir):
        # Obtener la ruta completa del archivo
        file_path = os.path.join(source_dir, filename)
        
        # Verificar si es un archivo
        if os.path.isfile(file_path):
            # Obtener la extensión del archivo
            file_extension = filename.split('.')[-1]
            destination_dir = os.path.join(source_dir, file_extension + 'Files')

            # Crear la carpeta si no existe
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)

            # Mover el archivo a la nueva carpeta
            shutil.move(file_path, os.path.join(destination_dir, filename))

# Llamar a la función
organize_by_extension(source_dir)
