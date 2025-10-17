#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox
import subprocess
import webbrowser

# Ejecutar comando con pkexec
def ejecutar_con_sudo(comando):
    try:
        resultado = subprocess.run(['pkexec'] + comando, capture_output=True, text=True)
        return resultado
    except Exception as e:
        class ResultadoError:
            returncode = -1
            stderr = str(e)
        return ResultadoError()

# Verifica si XAMPP está corriendo
def estado_xampp():
    try:
        resultado = subprocess.run(['/opt/lampp/lampp', 'status'], capture_output=True, text=True)
        if "Apache is running" in resultado.stdout:
            return "activo"
        else:
            return "detenido"
    except Exception:
        return "desconocido"

# Actualizar indicador visual
def actualizar_estado():
    estado = estado_xampp()
    if estado == "activo":
        estado_label.config(text="XAMPP está ACTIVO", fg="green")
    elif estado == "detenido":
        estado_label.config(text="XAMPP está DETENIDO", fg="red")
    else:
        estado_label.config(text="Estado DESCONOCIDO", fg="gray")

# Iniciar XAMPP
def iniciar_xampp():
    resultado = ejecutar_con_sudo(['/opt/lampp/lampp', 'start'])
    if resultado.returncode == 0:
        messagebox.showinfo("Éxito", "XAMPP iniciado correctamente")
    else:
        messagebox.showerror("Error", f"No se pudo iniciar XAMPP:\n{resultado.stderr}")
    actualizar_estado()

# Detener XAMPP
def detener_xampp():
    resultado = ejecutar_con_sudo(['/opt/lampp/lampp', 'stop'])
    if resultado.returncode == 0:
        messagebox.showinfo("Éxito", "XAMPP detenido correctamente")
    else:
        messagebox.showerror("Error", f"No se pudo detener XAMPP:\n{resultado.stderr}")
    actualizar_estado()

# Abrir phpMyAdmin
def abrir_phpmyadmin():
    webbrowser.open("http://localhost/phpmyadmin")

# --- Interfaz gráfica ---
ventana = tk.Tk()
ventana.title("Panel XAMPP")
ventana.geometry("320x250")
ventana.configure(bg="#f0f0f0")

# Estilos
estilo_boton = {
    "bg": "#0078d7",
    "fg": "white",
    "activebackground": "#005fa3",
    "font": ("Arial", 11),
    "width": 20,
    "height": 2
}

# Título
tk.Label(ventana, text="Panel de Control XAMPP", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=10)

# Indicador de estado
estado_label = tk.Label(ventana, text="", font=("Arial", 12, "bold"), bg="#f0f0f0")
estado_label.pack(pady=5)

# Botones
tk.Button(ventana, text="Iniciar XAMPP", command=iniciar_xampp, **estilo_boton).pack(pady=5)
tk.Button(ventana, text="Detener XAMPP", command=detener_xampp, **estilo_boton).pack(pady=5)
tk.Button(ventana, text="Abrir phpMyAdmin", command=abrir_phpmyadmin, **estilo_boton).pack(pady=10)

# Mostrar estado inicial
actualizar_estado()

ventana.mainloop()
