import tkinter as tk
from tkinter import simpledialog
from gridObject import Grid

class GridEditor:
    def __init__(self, master, grid_label, gridScale):
        self.master = master
        self.master.title(f"Editor de Grid: {grid_label}")
        
        self.gridScale = gridScale
        self.grid_data = Grid(grid_label)  # Crea una nueva instancia de Grid con la etiqueta dada
        self.canvas = tk.Canvas(self.master, width=16 * 30, height=16 * 30)
        self.canvas.pack()

        self.save_buttom = tk.Button(self.master, text="Save Grid", command=self.save_grid)
        self.save_buttom.pack()

        self.clean_buttom = tk.Button(self.master, text="Clean Grid", command=lambda: self.clean_grid(gridScale, ""))
        self.clean_buttom.pack()

        # Dibuja la grid en el canvas
        self.draw_grid(gridScale)

        # Vincula los eventos
        self.canvas.bind("<Button-1>", lambda event: self.on_canvas_click(event, gridScale))  # Para cambiar el estado de la celda al hacer clic
        

    def draw_grid(self, gridScale):
        self.canvas.delete("all")  # Limpia el canvas antes de redibujar
        for i in range(28):
            for j in range(28):
                color = "black" if self.grid_data.grid_data[i][j] == 1 else "white"
                self.canvas.create_rectangle(i * gridScale, j * gridScale, (i + 1) * gridScale, (j + 1) * gridScale, fill=color, outline="gray")

    def on_canvas_click(self, event, gridScale):
        x = event.x // gridScale
        y = event.y // gridScale
        self.grid_data.toggle_cell(x, y)
        self.draw_grid(gridScale)

    def save_grid(self):

        try:
            # Llama a la función para guardar la grid
            self.grid_data.label = tk.simpledialog.askstring("Label", "Cual es la etiqueta?")
            self.grid_data.save_to_file()
            print(f"Grid {self.grid_data.label} guardada con éxito.")
        except: 
            print("Ha ocurrido un error mientras se llamaba la funcion de guardado desde gridEditor.py")


    def clean_grid(self, gridScale, grid_label=""):
        self.grid_data = Grid(grid_label)
        self.draw_grid(gridScale)
