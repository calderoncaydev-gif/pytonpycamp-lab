import sqlite3

def conectar():
    conn = sqlite3.connect('datos_mapa.db')
    return conn

def cerrar(conn):
    conn.close()
