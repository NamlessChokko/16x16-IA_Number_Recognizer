import tkinter as tk
from gridObject import Grid
import json
import os

class GridEditor:
    def __init__(self, root):  # El constructor recibe la ventana principal
        self.root = root
        self.root.title("Editor de Cuadrícula 16x16")

        # Parámetros de la cuadrícula
        self.grid_size = 16
        self.cell_size = 30
        self.canvas = tk.Canvas(root, width=self.grid_size * self.cell_size, height=self.grid_size * self.cell_size)
        self.canvas.pack()

        # Inicializa la cuadrícula vacía
        self.grid_data = Grid(self.grid_size)  # Usa el objeto Grid desde gridObject.py

        # Vincular clics en el canvas a las celdas de la cuadrícula
        self.canvas.bind("<Button-1>", self.toggle_cell)

        # Dibujar la cuadrícula
        self.draw_grid()

    def draw_grid(self):
        """Dibuja la cuadrícula en la interfaz"""
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                color = "black" if self.grid_data.grid[i][j] else "white"
                self.canvas.create_rectangle(
                    i * self.cell_size, j * self.cell_size,
                    (i + 1) * self.cell_size, (j + 1) * self.cell_size,
                    fill=color, outline="gray"
                )

    def toggle_cell(self, event):
        """Cambia el estado de la celda (blanca o negra) al hacer clic"""
        x = event.x // self.cell_size
        y = event.y // self.cell_size
        self.grid_data.toggle_cell(x, y)  # Cambia el estado de la celda en Grid
        self.draw_grid()

    def save_grid(self):
        """Guarda la cuadrícula en un archivo JSON"""
        if not os.path.exists("data/grids"):
            os.makedirs("data/grids")
        
        self.grid_data.save_to_json("data/grids")
