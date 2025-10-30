import tkinter as tk
from tkinter import ttk
from controller import Controlador  # Importación absoluta
from tkinter import messagebox  # Importa el módulo messagebox
import subprocess

class VistaUpdate:
    def __init__(self, root):
        self.root = root
        self.root.title("Actualizar Datos")
        self.root.geometry("300x150")

        self.controlador = Controlador()

        self.lbl_nombre = tk.Label(self.root, text="Nombre:")
        self.lbl_nombre.pack()
        self.entry_nombre = tk.Entry(self.root)
        self.entry_nombre.pack()

        self.lbl_correo = tk.Label(self.root, text="Correo:")
        self.lbl_correo.pack()
        self.entry_correo = tk.Entry(self.root)
        self.entry_correo.pack()

        self.lbl_contrasenia = tk.Label(self.root, text="Contraseña:")
        self.lbl_contrasenia.pack()
        self.entry_contrasenia = tk.Entry(self.root)
        self.entry_contrasenia.pack()

        self.lbl_rol = tk.Label(self.root, text="Rol:")
        self.lbl_rol.pack()
        self.entry_rol = tk.Entry(self.root)
        self.entry_rol.pack()

        self.btn_agregar = tk.Button(self.root, text="Actualizar Persona", command=self.actulizar_persona)
        self.btn_agregar.pack(pady=20)

    def actulizar_persona(self):
        self.controlador = Controlador()
        nombre = self.entry_nombre.get()
        correo = self.entry_correo.get()
        contrasena = self.entry_contrasenia.get()
        rol = self.entry_rol.get()
        self.controlador.agregar_persona(nombre, correo, contrasena, rol)
        self.entry_nombre.delete(0, tk.END)
        self.entry_correo.delete(0, tk.END)
        self.entry_contrasenia.delete(0, tk.END)
        self.entry_rol.delete(0, tk.END)
        # Mostrar mensaje de éxito
        messagebox.showinfo("Éxito", "Persona agregada correctamente.")
        # Cerrar la ventana actual y abrir la ventana principal
        self.root.destroy()
        subprocess.Popen(['python', 'view/viewhome.py'])



root = tk.Tk()
app = VistaUpdate(root)
root.mainloop()


