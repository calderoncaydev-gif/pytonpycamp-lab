import mysql.connector

class Modelo:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='python'
        )
        self.cursor = self.conexion.cursor()

    def agregar_datos(self, nombre, correo, contrasena, rol):
        sql = "INSERT INTO empleado (nombre, correo, contrasena, rol) VALUES (%s, %s, %s, %s)"
        val = (nombre, correo, contrasena, rol)
        self.cursor.execute(sql, val)
        self.conexion.commit()

    
    def obtener_datos(self):
        self.cursor.execute("SELECT * FROM empleado")
        return self.cursor.fetchall()
