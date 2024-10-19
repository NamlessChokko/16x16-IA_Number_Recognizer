import tkinter as tk
from gridEditor import GridEditor  # Importar el editor de grids
from gridViewer import GridViewer  # Importar el visualizador de grids

# Función para abrir el editor
def open_editor():
    editor_window = tk.Toplevel(root)  # Crear una nueva ventana
    GridEditor(editor_window)  # Inicializar el editor en esa ventana

# Función para abrir el visualizador
def open_visualizer():
    visualizer_window = tk.Toplevel(root)  # Crear una nueva ventana
    GridViewer(visualizer_window)  # Inicializar el visualizador en esa ventana

# Crear la ventana principal
root = tk.Tk()
root.title("Grid Manager - Selecciona una opción")

# Configurar el tamaño de la ventana principal
root.geometry("300x150")

# Crear una etiqueta para indicar qué hacer
label = tk.Label(root, text="¿Qué te gustaría hacer?", font=("Helvetica", 14))
label.pack(pady=10)

# Botón para abrir el editor
editor_button = tk.Button(root, text="Abrir Editor de Grids", command=open_editor, width=25)
editor_button.pack(pady=5)

# Botón para abrir el visualizador
visualizer_button = tk.Button(root, text="Abrir Visualizador de Grids", command=open_visualizer, width=25)
visualizer_button.pack(pady=5)

# Iniciar la ventana principal
root.mainloop()
