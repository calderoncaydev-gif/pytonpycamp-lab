import mysql.connector

def create_table():
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

        # Consulta SQL para crear la tabla
        query = """
        CREATE TABLE empleado (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(50) NOT NULL,
            correo VARCHAR(100) NOT NULL,
            contrasena VARCHAR(100) NOT NULL,
            rol VARCHAR(100) NOT NULL
        )
        """

        # Ejecutar la consulta SQL para crear la tabla
        cursor.execute(query)

        # Aplicar los cambios
        conexion.commit()

        # Cerrar el cursor y la conexión
        cursor.close()
        conexion.close()

        print("Tabla creada exitosamente.")

    except mysql.connector.Error as e:
        print("Error al crear la tabla:", e)

# Llamada a la función para crear la tabla
create_table()
