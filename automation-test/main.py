import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import simpledialog

def show_table(data):
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Tabla con Tkinter")

    # Crear la tabla (Treeview)
    table = ttk.Treeview(root)

    # Extraer las columnas del DataFrame
    columns = data.columns

    # Definir la lista de columnas
    table["columns"] = list(columns)

    # Formato de las columnas
    for col in columns:
        # Reemplazar espacios en blanco con guiones bajos
        col_heading = col.replace(" ", "_")
        table.column(col, anchor=tk.W, width=500)
        # Encabezados de las columnas
        table.heading(col, text=col, anchor=tk.W)

    # Agregar filas a la tabla (datos del DataFrame)
    for i, row in data.iterrows():
        table.insert("", "end", values=list(row))

    # Función para agregar un nuevo registro a la tabla
    def agregar_registro():
        # Abrir un cuadro de diálogo para ingresar los valores
        nuevo_registro = simpledialog.askstring("Agregar Registro", "Ingrese los valores separados por comas (ejemplo: valor1, valor2, valor3):")
        if nuevo_registro:
            # Dividir los valores ingresados por comas y agregarlos como una nueva fila en la tabla
            valores = nuevo_registro.split(",")
            table.insert("", "end", values=valores)

    # Función para editar un registro existente en la tabla
    def editar_registro():
        # Obtener la fila seleccionada en la tabla
        seleccion = table.selection()
        if seleccion:
            # Abrir un cuadro de diálogo para editar los valores
            registro_editar = simpledialog.askstring("Editar Registro", "Ingrese los nuevos valores separados por comas (ejemplo: valor1, valor2, valor3):")
            if registro_editar:
                # Dividir los valores ingresados por comas y actualizar la fila seleccionada en la tabla
                valores_nuevos = registro_editar.split(",")
                table.item(seleccion, values=valores_nuevos)

    # Función para eliminar un registro de la tabla
    def eliminar_registro():
        # Obtener la fila seleccionada en la tabla
        seleccion = table.selection()
        if seleccion:
            # Eliminar la fila seleccionada de la tabla
            table.delete(seleccion)

    # Agregar botones para administrar los datos
    agregar_btn = tk.Button(root, text="Agregar Registro", command=agregar_registro)
    agregar_btn.pack()

    editar_btn = tk.Button(root, text="Editar Registro", command=editar_registro)
    editar_btn.pack()

    eliminar_btn = tk.Button(root, text="Eliminar Registro", command=eliminar_registro)
    eliminar_btn.pack()

    # Mostrar la tabla en la ventana
    table.pack()

    # Ejecutar el loop principal
    root.mainloop()

if __name__ == "__main__":
    # Leer el archivo Excel y obtener los datos que deseas mostrar en la tabla
    archivo_excel = pd.read_excel('supermarket_sales.xlsx')
    data_to_show = archivo_excel[['Gender', 'Product line', 'Total']]

    # Llamar a la función para mostrar la tabla
    show_table(data_to_show)
