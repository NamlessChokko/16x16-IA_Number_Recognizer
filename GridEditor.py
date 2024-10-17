import tkinter as tk
from tkinter import simpledialog
import json 

#En lineas 1, 2 y 3 se importan las librerias que vamos a usar:
#tkinder es para crear ventanas interacticas y es la que usaremos para hacer la cuadricula editable.
#simpledialg es un modulo de tkinder que es lo que usaremos para cuando se valla a guardar la cuadricula, le pregunte al usuario por la etiqueta (el numero que representa la cuadricula).
#json es para guardar las cuadriculas y sus etiquetas como archivos independientes.


#Esto crea una ventana usando la libreria tkinder
root = tk.Tk()#root sera como la ventana principal.
root.title("Editor de cuadricula 16x16")#Este es el nombre de la ventana.


#Aqui estan los parametros de la cuadricula:
GRID_SIZE = 16 #Esta variable sera para las dimensiones de la cuadricula.
CELL_SIZE = 30 #Y esta otra determinara el tamano de cada celda. No se bien que tan grande o pequenas sean, puse 30 solo porque no se me ocurria nada mas.
grid_data = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
#En la linea 19 se crea una lista bidimencional, en donde cada elemento de la lista toma de tamano el valor de GRID_SIZE.
#Cada elemento de la lista podra tener dos valores: true para encendida (negra) y false para apagada (blanca)... Si, lo se, no preguntes... >:(


#Aca se define la funcion que usaremos para cambiar el estado de cada cuadricula.
def toggle_cell (x, y):#Define la funcion con dos parametros los cuales determinan los valores x, y de la celda.
    grid_data[x][y] = not grid_data[x][y]#con los valores x, y de que se le introdujeron a la funcion entonces las celdas con los correspondientes valores cambiara de estado.
    draw_grid()#Dibuja de nuevo la celda

def draw_grid():#Se define la funcion draw_grid para que se dibujen las celdas de un color o otro.
    for i in range (GRID_SIZE):#Esta linea junto con la linea 31 basicamente lo qeu dicen es que para cada celdita que verifique si esta en true o false.
        for j in range(GRID_SIZE):
            color = "black" if grid_data[i][j] else "white"#Dibuja la celda de negro si es true.
            canvas.create_rectangle(i * CELL_SIZE, j * CELL_SIZE,#crea un rectangulo de largo y ancho igual a CELL_SIZE.
            (i+1) * CELL_SIZE, (j + 1) * CELL_SIZE,#Establece los bordes del rectangulo.
            fill=color, outline="gray")#Pinta de color gris los bordes.



#Esta funcion es para guardar todos los datos de la cuadricula (cuadriculas activadas, desactivadas y etiqueta) como un archivo .json
def save_grid():
    label = simpledialog.askstring("Etiqueta", "Introduzca la etiqueta del numero")
    if label:
        grid_info = {"grid": grid_data, "label": label}
        with open (f"grid_{label}.json", "w") as file:
            json.dump(grid_info, file)
        root.quit()
        


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
            

