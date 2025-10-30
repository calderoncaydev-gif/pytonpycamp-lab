import tkinter as tk
from model.model import Modelo


class Controlador:
    def __init__(self):
        self.modelo = Modelo()

    def form_add(self):
        return self.vista

    def agregar_persona(self, nombre, correo, contrasena, rol):
        self.modelo.agregar_datos(nombre, correo, contrasena, rol)

    def obtener_datos(self):
        return self.modelo.obtener_datos()
    
    
