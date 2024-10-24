import tkinter as tk
from tkinter import filedialog
import os
from gridObject import Grid  # Asegúrate de que el Grid esté correctamente importado

class GridViewer:
    def __init__(self, master, gridScale):
        self.master = master
        self.master.title("Grid Viewer")
        self.gridScale = gridScale

        self.canvas = tk.Canvas(self.master, width=28 * gridScale, height=28 * gridScale)
        self.canvas.pack()

        self.load_button = tk.Button(self.master, text="Load Grid", command=lambda: self.open_file(gridScale))
        self.load_button.pack()

    def open_file(self, gridScale):
        try:
            # Cambiar el directorio de trabajo al directorio de inicio del usuario
            os.chdir(os.path.expanduser("~"))

            # Abre el file browser para seleccionar un archivo de cuadrícula
            file_path = filedialog.askopenfilename(
                title="Select a grid file",
                filetypes=(("JSON files", "*.json"), ("All files", "*.*"))
            )
            if file_path:
                # Cargar la grid desde el archivo seleccionado
                self.display_grid(Grid.load(file_path), gridScale)

        except Exception as e:
            print(f"Error al abrir el archivo: {str(e)}")

    def display_grid(self, grid, gridScale):
        # Dibujar la cuadrícula en el canvas
        self.canvas.delete("all")  # Limpiar cualquier grid anterior
        for i in range(28):
            for j in range(28):
                color = "black" if grid.grid_data[i][j] == 1 else "white"
                self.canvas.create_rectangle(i * float(gridScale), j * float(gridScale), (i + 1) * float(gridScale), (j + 1) * float(gridScale), fill=color, outline="gray")
