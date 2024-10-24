import os
import json
import gridObject


"""
Este programa fue creado solamente para convertir los valores booleanos de las antiguas grillas
a valores numericos que los modelos pueden procesar, no se supone que deba de tener algun uso de ahora
en adelante.
"""



def convert_bool_to_numeric(file_path):
    
    # Abre el archivo y carga los datos JSON
    with open(file_path, "r") as file:
        data = json.load(file)
    
    # Accede a la grilla y convierte los valores
    grid_data = data.get("grid", [])
    numeric_grid = [[1 if cell else 0 for cell in row] for row in grid_data]
    
    # Actualiza los datos originales con los valores numéricos
    data["grid"] = numeric_grid
    
    # Sobrescribe el archivo con los nuevos datos
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def process_all_grids(directory):
    # Recorre todos los archivos en el directorio
    for filename in os.listdir(directory):
        if filename.endswith(".json"):  # Solo procesar archivos .json
            file_path = os.path.join(directory, filename)
            convert_bool_to_numeric(file_path)
            print(f"Archivo {filename} convertido correctamente.")

# Ejecutar la funcion principal
process_all_grids("grid_editor/data/grids/")
