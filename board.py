import random
import numpy as np
# Tablero inicial
environment = np.array([ [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0]])
# Arreglo para almacenar el número total de items, donde items[0] la cantidad de césped, 
# items[1] la cantidad de flores e items[2] la cantidad de manzanas                     
items = [14, 5, 2]
#Función que determina las posiciones de los items. 
def itemPosition(objetos, cantidad, item): #Recibe el contador de los objetos, la cantidad establecida que debe tener el objeto dentro del mapa y el número asociado a ese objeto.
     while objetos < cantidad: #Se ejecuta un ciclo hasta asegurarse que en el tablero estén la cantidad establecida de objetos. 
        x = random.randint(0,len(environment)-1) 
        y = random.randint(0,len(environment[0])-1)
        if environment[x][y] == 0: #Si encuentra una posición vacía en las coordenadas pseudo-aleatorias proporcionadas, pone el objeto ahí y se suma al contador. 
            environment[x][y] = item
            objetos += 1
#Función que determina las posiciones de los jugadores. 
def playerPosition(player): #Recibe el número de jugador a poner en el tablero. 
    while True: #Se ejecuta un ciclo que pone el jugador en una casilla aleatoria si la encuentra vacía.  
        x = random.randint(0,len(environment)-1)
        y = random.randint(0,len(environment[0])-1)
        if environment[x][y] == 0:
            environment[x][y] = player
            return False
# Función principal: Crea el ambiente en el que se ejecutará el juego. 
def board():
    cesped = flores = manzanas = 0 #Contador inicial de los items. 
    playerPosition(1)
    playerPosition(2)
    itemPosition(cesped, items[0], 3)
    itemPosition(flores, items[1], 4)
    itemPosition(manzanas, items[2], 5)
    return environment


#Función que crea un tablero inicial de cualquier tamaño. 
#def tablero_inicial(filas, columnas):
    #board = []
    #for i in range(0, filas):
        #line = []
        #for j in range(0, columnas):
            #line.append(0)
        #board.append(line)
    #return board