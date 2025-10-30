
import tkinter as tk
from tkinter import ttk
from controller import Controlador
from tkinter import messagebox  # Importa el módulo messagebox
import subprocess


class Vista:
    def __init__(self, root):
        self.root = root
        self.root.title("Tabla de Datos")
        self.root.geometry("600x400")
        self.controlador = Controlador()

        self.tabla = ttk.Treeview(self.root)
        self.tabla["columns"] = ("columna1", "columna2", "columna3", "columna4")  # Define las columnas de la tabla
        self.tabla.heading("#0", text="ID")
        self.tabla.heading("columna1", text="Nombre")
        self.tabla.heading("columna2", text="Correo")
        self.tabla.heading("columna3", text="Contrasenia")
        self.tabla.heading("columna4", text="Rol")
        self.tabla.pack(fill=tk.BOTH, expand=1)
        self.tabla.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.btn_agregar = tk.Button(self.root, text="Agregar Persona", command=self.abrir_formulario)
        self.btn_agregar.pack(pady=20)
        self.btn_update = tk.Button(self.root, text="Actualizar Persona", command=self.abrir_formulario_update)
        self.btn_update.pack(pady=20)

        self.cargar_datos()

    def cargar_datos(self):
        datos = self.controlador.obtener_datos()
        for dato in datos:
            self.tabla.insert("", "end", text=dato[0], values=(dato[1], dato[2], dato[3], dato[4]))

    def abrir_formulario(self):
          # Cerrar la ventana actual y abrir la ventana principal
        self.root.destroy()
        subprocess.Popen(['python', 'view.py'])
    
    def abrir_formulario_update(self):
        if len(self.sel) == 1:
            # Cerrar la ventana actual y abrir la ventana principal
            self.root.destroy()
            self.controlador.form_update()
        elif len(self.sel) == 0:
            messagebox.showerror(
                "Error", "Por favor seleccionar un empleado en la tabla"
            )

    def obtener_datos_seleccionados(self, item):
        datos = self.tabla.item(item, "values")
        return datos
    
    def actualizar_tabla(self):
        # Limpiar la tabla antes de cargar nuevos datos
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        
        # Cargar los nuevos datos en la tabla
        self.cargar_datos()
    sel = []
    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tabla.selection():
            if i not in self.sel:
                self.sel.append(i)
root = tk.Tk()
app = Vista(root)
root.mainloop()