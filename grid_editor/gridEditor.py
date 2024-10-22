import tkinter as tk
from tkinter import simpledialog
from gridObject import Grid

class GridEditor:
    def __init__(self, master, grid_label):
        self.master = master
        self.master.title(f"Editor de Grid: {grid_label}")
        
        self.grid_data = Grid(grid_label)  # Crea una nueva instancia de Grid con la etiqueta dada
        self.canvas = tk.Canvas(self.master, width=16 * 30, height=16 * 30)
        self.canvas.pack()

        # Dibuja la grid en el canvas
        self.draw_grid()

        # Vincula los eventos
        self.canvas.bind("<Button-1>", self.on_canvas_click)  # Para cambiar el estado de la celda al hacer clic
        self.master.bind("<Return>", self.save_grid)  # Vincula la tecla Enter para guardar la grid

    def draw_grid(self):
        self.canvas.delete("all")  # Limpia el canvas antes de redibujar
        for i in range(16):
            for j in range(16):
                color = "black" if self.grid_data.grid_data[i][j] == 1 else "white"
                self.canvas.create_rectangle(i * 30, j * 30, (i + 1) * 30, (j + 1) * 30, fill=color, outline="gray")

    def on_canvas_click(self, event):
        x = event.x // 30
        y = event.y // 30
        self.grid_data.toggle_cell(x, y)
        self.draw_grid()

    def save_grid(self, event):
        # Llama a la función para guardar la grid
        self.grid_data.label = tk.simpledialog.askstring("Label", "Cual es la etiqueta?")
        self.grid_data.save_to_file()
        print(f"Grid {self.grid_data.label} guardada con éxito.")
