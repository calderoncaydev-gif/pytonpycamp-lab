import mysql.connector

def create_tables():
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

        # Consulta SQL para crear la tabla usuarios
        query_usuarios = """
        CREATE TABLE usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(50) NOT NULL,
            correo VARCHAR(100) NOT NULL,
            contrasena VARCHAR(100) NOT NULL
        )
        """

        # Consulta SQL para crear la tabla pedidos
        query_pedidos = """
        CREATE TABLE pedidos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            descripcion VARCHAR(100) NOT NULL,
            usuario_id INT,
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
        )
        """

        # Ejecutar las consultas SQL para crear las tablas
        cursor.execute(query_usuarios)
        cursor.execute(query_pedidos)

        # Aplicar los cambios
        conexion.commit()

        # Cerrar el cursor y la conexión
        cursor.close()
        conexion.close()

        print("Tablas creadas exitosamente.")

    except mysql.connector.Error as e:
        print("Error al crear las tablas:", e)

# Llamada a la función para crear las tablas con la relación
create_tables()
