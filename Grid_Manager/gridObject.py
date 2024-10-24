import json  # Para cargar y guardar archivos JSON
import tkinter as tk  # Para visualizar las grids en una ventana
import os  # Para verificar la existencia de archivos y carpetas

# Variable global que ajusta la escala de cada pixel de la cuadricula 
gridScale = 20 

class Grid:
    def __init__(self, label, grid_data=None):
        """
        Constructor que inicializa la grid.
        :param label: Etiqueta para identificar la grid.
        :param grid_data: Datos opcionales para inicializar la grid (lista 2D). Si no se proporciona, se crea una nueva vacía.
        """


        self.label = label  # Asigna la etiqueta a la grid
        self.grid_data = grid_data if grid_data else [[0 for _ in range(28)] for _ in range(28)]
        # Si no se proporcionan datos de cuadrícula, se crea una nueva de 16x16 con todas las celdas apagadas.


    def toggle_cell(self, x, y):
        """
        Cambia el estado de una celda en la grid.
        :param x: Fila de la celda.
        :param y: Columna de la celda.
        """
        self.grid_data[x][y] = 1 if self.grid_data[x][y] == 0 else 0 # Cambia el estado de la celda (encendida/apagada)

    def save_to_file(self):

        try:

            """
            Guarda los datos de la grid en un archivo JSON.
            Crea una carpeta 'Grids' si no existe en el directorio actual.
            """

            print("Guardando archivo...")
            # Obtiene el directorio donde se encuentra el ejecutable
            base_dir = os.path.dirname(os.path.abspath(__file__))  

            # Define la ruta completa para la carpeta 'Grids'
            grids_dir = os.path.join(base_dir, "Grids")

            # Crea la carpeta 'Grids' si no existe
            if not os.path.exists(grids_dir):
                os.makedirs(grids_dir)

            base_filename = f"grid_{self.label}"  # Nombre del archivo basado en la etiqueta
            file_path = os.path.join(grids_dir, f"{base_filename}.json")
            counter = 1

            # Si el archivo ya existe, busca un nombre único
            while os.path.exists(file_path):
                file_path = os.path.join(grids_dir, f"{base_filename}({counter}).json")
                counter += 1

            # Guarda los datos en el archivo JSON
            with open(file_path, "w") as file:
                json.dump({"label": self.label, "grid": self.grid_data}, file, indent=4)

        except:
            print("Ha ocurrido un error mientras se guardaba el arcivo. :(")

    @classmethod
    def load(cls, file_path):
        """
        Carga una grid desde un archivo JSON.
        :param file_path: Ruta del archivo JSON.
        :return: Instancia de Grid con los datos cargados.
        """
        with open(file_path, "r") as file:
            data = json.load(file)
            return cls(data["label"], data["grid"])  # Crea y retorna una nueva instancia de Grid con los datos cargados

    def display(self):
        """
        Crea una ventana de tkinter para visualizar la grid.
        """
        root = tk.Tk()
        root.title(f"Visualización de la Grid: {self.label}")
        
        canvas = tk.Canvas(root, width=28 * gridScale, height=28 * gridScale)  # Crea un canvas para dibujar
        canvas.pack()

        for i in range(28):
            for j in range(28):
                color = "black" if self.grid_data[i][j] == 1 else "white"  # Define el color de la celda
                canvas.create_rectangle(i * gridScale, j * gridScale, (i + 1) * gridScale, (j + 1) * gridScale, fill=color, outline="gray")

        root.mainloop()  # Ejecuta la ventana

