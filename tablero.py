import random
import numpy as np
#Función que crea un tablero inicial
#def tablero_inicial():
    #board = []
    #for i in range(0, 8):
        #line = []
        #for j in range(0, 8):
            #line.append(0)
        #board.append(line)
    #return board

# Tablero inicial
tablero_inicial = np.array([  [0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0]])
# Arreglo para almacenar el número total de items, donde items[1] la cantidad de césped, 
# items[2] la cantidad de flores e items[3] la cantidad de manzanas                     
items = [14, 5, 2]
                       
def randomObjects(objetos, cantidad, item):
     while objetos < cantidad:
        x = random.randint(0,7)
        y = random.randint(0,7)
        if tablero_inicial[x][y] == 0:
            tablero_inicial[x][y] = item
            objetos += 1

def randomPlayers(numJugador):
    while True:
        x = random.randint(0,7)
        y = random.randint(0,7)
        if tablero_inicial[x][y] == 0:
            tablero_inicial[x][y] = numJugador
            return False

def tablero():
    cesped = flores = manzanas = 0
    randomPlayers(1)
    randomPlayers(2)
    randomObjects(cesped, items[0], 3)
    randomObjects(flores, items[1], 4)
    randomObjects(manzanas, items[2], 5)

    return tablero_inicial    
