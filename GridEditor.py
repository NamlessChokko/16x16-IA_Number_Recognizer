import tkinter as tk
from tkinter import simpledialog
import json 
import os 

# Importamos las librerías necesarias:
# tkinter es para crear ventanas interactivas y es la que usaremos para hacer la cuadrícula editable.
# simpledialog es un módulo de tkinter que usaremos para solicitar al usuario la etiqueta (el número que representa la cuadrícula) al momento de guardar.
# json es para guardar las cuadrículas y sus etiquetas como archivos independientes.
# os es una libreria de python que te permite usar comandos del sistema como los de crear carpetas.

# Crear la ventana principal
root = tk.Tk()  # root será la ventana principal.
root.title("Editor de cuadrícula 16x16")  # Este es el nombre de la ventana.

# Parámetros de la cuadrícula
GRID_SIZE = 16  # Esta variable define las dimensiones de la cuadrícula.
CELL_SIZE = 30  # Esta variable determina el tamaño de cada celda.

# Inicializa la estructura de datos de la cuadrícula
grid_data = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
# En esta línea se crea una lista bidimensional, donde cada elemento representa el estado de una celda (encendida o apagada).

# Función para cambiar el estado de cada celda
def toggle_cell(x, y):  # Define la función con dos parámetros que representan las coordenadas de la celda.
    grid_data[x][y] = not grid_data[x][y]  # Cambia el estado de la celda.
    draw_grid()  # Redibuja la cuadrícula para reflejar el cambio.

# Función para dibujar la cuadrícula
def draw_grid():
    for i in range(GRID_SIZE):  # Itera sobre las filas de la cuadrícula.
        for j in range(GRID_SIZE):  # Itera sobre las columnas de la cuadrícula.
            color = "black" if grid_data[i][j] else "white"  # Define el color de la celda.
            canvas.create_rectangle(
                i * CELL_SIZE, j * CELL_SIZE,  # Esquina superior izquierda.
                (i + 1) * CELL_SIZE, (j + 1) * CELL_SIZE,  # Esquina inferior derecha.
                fill=color, outline="gray"  # Establece el color de relleno y el contorno.
            )

# Función para guardar los datos de la cuadrícula en un archivo JSON
def save_grid():
    # Verifica si la carpeta "Grids" existe; si no, la crea
    if not os.path.exists("Grids"):
        os.makedirs("Grids")

    # Solicita al usuario la etiqueta para el archivo
    label = simpledialog.askstring("Etiqueta", "Introduzca la etiqueta del número")
    if label:  # Asegúrate de que la etiqueta no esté vacía
        grid_info = {"grid": grid_data, "label": label}  # Estructura de datos a guardar
        # Guarda la información en un archivo JSON dentro de la carpeta "Grids"
        with open(f"Grids/grid_{label}.json", "w") as file:
            json.dump(grid_info, file, indent=4)  # Escribe la estructura de datos en el archivo JSON

        root.quit()  # Cierra la aplicación

# Configurar el canvas donde dibujaremos la cuadrícula
canvas = tk.Canvas(root, width=GRID_SIZE * CELL_SIZE, height=GRID_SIZE * CELL_SIZE)
canvas.pack()

# Agregar el evento de clic en las celdas
canvas.bind("<Button-1>", lambda event: toggle_cell(event.x // CELL_SIZE, event.y // CELL_SIZE))

# Dibujar la cuadrícula por primera vez
draw_grid()

# Asociar la tecla Enter para guardar el archivo
root.bind("<Return>", lambda event: save_grid())

# Ejecutar la ventana
root.mainloop()
