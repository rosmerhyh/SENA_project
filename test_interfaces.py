import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk  # pip install pillow

# -------- Ventana secundaria --------
def abrir_ventana_secundaria():
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Ventana secundaria")
    ventana_secundaria.geometry("400x300")

    tk.Label(ventana_secundaria, text="Escribe algo aquí:").pack(pady=10)
    entrada_secundaria = tk.Entry(ventana_secundaria)
    entrada_secundaria.pack()

    def mostrar_mensaje():
        valor = entrada_secundaria.get()
        messagebox.showinfo("Texto ingresado", f"Escribiste: {valor}")

    tk.Button(ventana_secundaria, text="Mostrar mensaje", command=mostrar_mensaje).pack(pady=10)

# -------- Seleccionar y mostrar imagen --------
def seleccionar_imagen():
    archivo = filedialog.askopenfilename(title="Selecciona una imagen", filetypes=[("Imagenes", "*.jpg *.png *.jpeg")])
    if archivo:
        imagen = Image.open(archivo)
        imagen = imagen.resize((200, 200))
        imagen_tk = ImageTk.PhotoImage(imagen)
        etiqueta_imagen.config(image=imagen_tk)
        etiqueta_imagen.image = imagen_tk  # mantener referencia

# -------- Ventana principal --------
ventana = tk.Tk()
ventana.title("Demo de Interfaz")
ventana.geometry("600x400")

# Frame superior
frame_superior = tk.Frame(ventana)
frame_superior.pack(pady=10)

tk.Label(frame_superior, text="Demo Interactiva con Tkinter", font=("Arial", 16)).pack()

# Frame del formulario
frame_form = tk.LabelFrame(ventana, text="Formulario de ejemplo", padx=10, pady=10)
frame_form.pack(pady=10)

tk.Label(frame_form, text="Nombre:").grid(row=0, column=0, sticky="e")
entrada_nombre = tk.Entry(frame_form)
entrada_nombre.grid(row=0, column=1)

tk.Label(frame_form, text="Correo:").grid(row=1, column=0, sticky="e")
entrada_correo = tk.Entry(frame_form)
entrada_correo.grid(row=1, column=1)

# Botón para abrir otra ventana
tk.Button(ventana, text="Abrir ventana secundaria", command=abrir_ventana_secundaria).pack(pady=10)

# Espacio para mostrar imagen
frame_imagen = tk.LabelFrame(ventana, text="Imagen seleccionada", padx=10, pady=10)
frame_imagen.pack(pady=10)
etiqueta_imagen = tk.Label(frame_imagen, text="Aquí irá la imagen", width=200, height=200, bg="gray")
etiqueta_imagen.pack()

# Botón para cargar imagen
tk.Button(ventana, text="Seleccionar imagen", command=seleccionar_imagen).pack(pady=5)

ventana.mainloop()
