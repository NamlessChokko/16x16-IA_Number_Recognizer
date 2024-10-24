import tkinter as tk # Importar tkinter para las ventanas
from gridEditor import GridEditor  # Importar el editor de grids
from gridViewer import GridViewer  # Importar el visualizador de grids
from gridObject import gridScale


# Función para abrir el editor
def open_editor(gridScale):
    print("Abriendo Editor de grillas...")
    editor_window = tk.Toplevel(root)  # Crear una nueva ventana 
    GridEditor(editor_window, "...", gridScale)  # Inicializar el editor, como parametros: la ventana recien creada y un texto vacio para la etiqueta

# Función para abrir el visualizador
def open_visualizer(gridScale):
    print("Abriendo Visualizador de grillas...")
    visualizer_window = tk.Toplevel(root)  # Crear una nueva ventana
    GridViewer(visualizer_window, gridScale)  # Inicializar el visualizador, como parametro: la ventana recien creada


# Crear la ventana principal
root = tk.Tk()
root.title("Grid Manager") # Define el titulo de la ventana

# Configurar el tamaño de la ventana principal
root.geometry("300x150")

# Crear una etiqueta para indicar qué hacer
label = tk.Label(root, text="¿Qué te gustaría hacer?", font=("Helvetica", 14))
label.pack(pady=15)

# Botón para abrir el editor
editor_button = tk.Button(root, text="Abrir Editor de Grids", command=lambda: open_editor(gridScale), width=25)
editor_button.pack(pady=5)

# Botón para abrir el visualizador
visualizer_button = tk.Button(root, text="Abrir Visualizador de Grids", command=lambda: open_visualizer(gridScale), width=25)
visualizer_button.pack(pady=5)

# Iniciar la ventana principal
root.mainloop()
