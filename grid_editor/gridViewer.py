import tkinter as tk
from tkinter import filedialog
from gridObject import Grid  # Asegúrate de que el Grid esté correctamente importado

class GridViewer:
    def __init__(self, master):
        self.master = master
        self.master.title("Grid Viewer")

        self.canvas = tk.Canvas(self.master, width=16 * 30, height=16 * 30)
        self.canvas.pack()

        self.load_button = tk.Button(self.master, text="Load Grid", command=self.open_file)
        self.load_button.pack()

    def open_file(self):
        # Abre el file browser para seleccionar un archivo de cuadrícula
        file_path = filedialog.askopenfilename(
            title="Select a grid file",
            filetypes=(("JSON files", "*.json"), ("All files", "*.*"))
        )
        if file_path:
            # Cargar la grid desde el archivo seleccionado
            self.display_grid(Grid.load(file_path))

    def display_grid(self, grid):
        # Dibujar la cuadrícula en el canvas
        self.canvas.delete("all")  # Limpiar cualquier grid anterior
        for i in range(16):
            for j in range(16):
                color = "black" if grid.grid_data[i][j] else "white"
                self.canvas.create_rectangle(i * 30, j * 30, (i + 1) * 30, (j + 1) * 30, fill=color, outline="gray")
