import tkinter as tk
from tkinter import ttk
import subprocess

class Vista:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de app")
        self.root.geometry("600x400")

        self.btn_agregar = tk.Button(self.root, text="Adiministrar Persona", command=self.abrir_formulario)
        self.btn_agregar.pack(pady=20)

    def abrir_formulario(self):
          # Cerrar la ventana actual y abrir la ventana principal
        self.root.destroy()
        subprocess.Popen(['python', 'viewhome.py'])
    
    
root = tk.Tk()
app = Vista(root)
root.mainloop()