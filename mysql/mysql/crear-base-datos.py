import mysql.connector

def create_database():
    config = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'port': '3306'
    }

    try:
        # Crear una conexión a la base de datos (sin especificar el nombre de la base de datos)
        conexion = mysql.connector.connect(**config)

        # Crear un objeto cursor para interactuar con la base de datos
        cursor = conexion.cursor()

        # Consulta SQL para crear la base de datos
        query = "CREATE DATABASE python"

        # Ejecutar la consulta SQL para crear la base de datos
        cursor.execute(query)

        # Cerrar el cursor y la conexión
        cursor.close()
        conexion.close()

        print("Base de datos creada exitosamente.")

    except mysql.connector.Error as e:
        print("Error al crear la base de datos:", e)

# Llamada a la función para crear la base de datos
create_database()
