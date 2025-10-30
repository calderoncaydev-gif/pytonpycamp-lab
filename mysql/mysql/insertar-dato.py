import mysql.connector

def insert_data(nombre, correo, contrasena):
    config = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'python',
        'port': '3306'
    }

    try:
        # Crear una conexión a la base de datos
        conexion = mysql.connector.connect(**config)

        # Crear un objeto cursor para interactuar con la base de datos
        cursor = conexion.cursor()

        # Consulta SQL para insertar un nuevo registro
        query = "INSERT INTO usuarios (nombre, correo, contrasena) VALUES (%s, %s, %s)"
        datos = (nombre, correo, contrasena)

        # Ejecutar la consulta SQL para insertar los datos
        cursor.execute(query, datos)

        # Aplicar los cambios
        conexion.commit()

        # Cerrar el cursor y la conexión
        cursor.close()
        conexion.close()

        print("Datos insertados exitosamente.")

    except mysql.connector.Error as e:
        print("Error al insertar datos:", e)

# Ejemplo de uso: insertar un nuevo registro
insert_data("Eduardo", "eduardo@example.com", "contraseña123")
insert_data("Camilo", "camilo@example.com", "contraseña123")
insert_data("Cecilia", "cecilia@example.com", "contraseña123")
insert_data("Mariano", "Mariano@example.com", "contraseña123")
insert_data("Miguel", "miguel@example.com", "contraseña123")
insert_data("Francisco", "Francisco@example.com", "contraseña123")
