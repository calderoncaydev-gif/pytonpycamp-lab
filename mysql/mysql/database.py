import mysql.connector

# Configuración de la conexión
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',  # Por ejemplo, 'localhost' para una base de datos local
    'database': 'test-python',
    'port': '3306'  # Por defecto, el puerto es 3306 para MySQL
}

# Intentar establecer la conexión
try:
    # Crear una conexión a la base de datos
    conexion = mysql.connector.connect(**config)

    # Comprobar si la conexión se estableció correctamente
    if conexion.is_connected():
        print('Conexión exitosa a la base de datos.')

        # Aquí puedes realizar operaciones en la base de datos, como consultas o inserciones.

        # No olvides cerrar la conexión una vez que hayas terminado.
        conexion.close()
        print('Conexión cerrada.')

except mysql.connector.Error as e:
    print('Error al intentar conectar:', e)
