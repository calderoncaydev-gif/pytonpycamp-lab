import mysql.connector

def show_table_data():
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

        # Consulta SQL para seleccionar todos los registros de la tabla usuarios
        query = "SELECT * FROM usuarios"

        # Ejecutar la consulta SQL
        cursor.execute(query)

        # Obtener los resultados de la consulta
        resultados = cursor.fetchall()

        # Mostrar los resultados
        for fila in resultados:
            print(fila)

        # Cerrar el cursor y la conexión
        cursor.close()
        conexion.close()

    except mysql.connector.Error as e:
        print("Error al mostrar los datos de la tabla:", e)

# Llamada a la función para mostrar los datos de la tabla
show_table_data()
