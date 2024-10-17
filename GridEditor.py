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
grid_data = [[False for_in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
#En la linea 19 se crea una lista bidimencional, en donde cada elemento de la lista toma de tamano el valor de GRID_SIZE.
#Cada elemento de la lista podra tener dos valores: true para encendida (negra) y false para apagada (blanca)... Si, lo se, no preguntes... >:(


#Aca se define la funcion que usaremos para cambiar el estado de cada cuadricula.
def toggle_cell (x, y):#Define la funcion con dos parametros los cuales determinan los valores x, y de la celda.
    grid_data[x][y] = not grid_data[x][y]#con los valores x, y de que se le introdujeron a la funcion entonces las celdas con los correspondientes valores cambiara de estado.
    draw_grid()#Dibuja de nuevo la celda

def draw_grid():
    for i in range (GRID_SIZE):
        for j in range(GRID_SIZE):
            color = "black" if grid_data[i][j] else "white"
            canvas.create_rectangle(i * CELL_SIZE, j * CELL_SIZE
            (i+1) * CELL_SIZE, (j + 1) * CELL_SIZE,
            fill=color, outline="gray")

