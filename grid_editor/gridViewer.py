import tkinter as tk
from gridObject import Grid
import json
import os

class GridViewer:
    def __init__(self, root):  # El constructor recibe la ventana principal
        self.root = root
        self.root.title("Visor de Cuadrículas")

        # Parámetros de la cuadrícula
        self.grid_size = 16
        self.cell_size = 30
        self.canvas = tk.Canvas(root, width=self.grid_size * self.cell_size, height=self.grid_size * self.cell_size)
        self.canvas.pack()

        # Botón para cargar una cuadrícula
        load_button = tk.Button(root, text="Cargar Cuadrícula", command=self.load_grid)
        load_button.pack()

    def draw_grid(self, grid_data):
        """Dibuja la cuadrícula en la interfaz a partir de los datos"""
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                color = "black" if grid_data[i][j] else "white"
                self.canvas.create_rectangle(
                    i * self.cell_size, j * self.cell_size,
                    (i + 1) * self.cell_size, (j + 1) * self.cell_size,
                    fill=color, outline="gray"
                )

    def load_grid(self):
        """Carga una cuadrícula desde un archivo JSON"""
        file_path = tk.filedialog.askopenfilename(initialdir="data/grids", title="Seleccionar archivo JSON",
                                                  filetypes=(("Archivos JSON", "*.json"),))
        if file_path:
            with open(file_path, "r") as file:
                grid_data = json.load(file)["grid"]
                self.draw_grid(grid_data)
