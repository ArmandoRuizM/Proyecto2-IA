import numpy as np
#Variable global para almacenar y tratar el ambiente del juego
environment=np.array([  [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,3,5,0,0,0,0],
                        [0,0,0,0,1,2,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0]])

#Variables globales para llevar el conteo del puntaje de los jugadores, blanco=cpu y negro=humano
blackHorseScore=0
whiteHorseScore=0

# environment=np.array([  [0,0,0,0,0,0,0,0],
#                         [0,0,0,0,0,0,0,0],
#                         [0,0,0,0,0,0,0,0],
#                         [0,0,0,1,2,0,0,0],
#                         [0,0,0,0,0,0,0,0],
#                         [0,0,0,0,0,0,0,0],
#                         [0,0,0,0,0,0,0,0],
#                         [0,0,0,0,0,0,0,0]])

##Momentaneamente, esta función recibe un entero que representa al jugador para el cuál se quieren obtener los movimientos posibles
##1 = jugador Humano - caballo negro
##2 = jugador cpu - caballo blanco
##La función retorna una lista llena de booleanos que representan todas los movimientos posibles por el jugador determinado:
##u=casilla hacia arriba, l=casilla hacia la izquierda, r=casilla hacia la derecha, d=casilla hacia abajo 
##[1u2l, 2u1l, 1u2r, 2u1r, 1d2r, 2d1r, 1d2l, 2d1l]
def possibleMoves(player):
    moves = [False, False, False, False, False, False, False, False]
    playerPos = findPlayer(player)
    rival=-1
    if(player==1):
        rival=2
    else:
        rival=1
    ##Se analiza movimiento a movimiento:
    #una arriba dos izquierda:
    if (playerPos[0]-1>=0 and playerPos[1]-2>=0): #Se revisa que caiga dentro del tablero
        #Se guarda momentaneamente la posición en la que quedaría
        auxPos=[playerPos[0]-1, playerPos[1]-2]
        if(environment[auxPos[0]][auxPos[1]]!=rival): #Se revisa que la casilla no esté ocupada por el otro jugador
            moves[0]= True #Si no está ocupada, se dice que se puede mover ahí
    #dos arriba una izquierda:
    if (playerPos[0]-2>=0 and playerPos[1]-1>=0): #Se revisa que caiga dentro del tablero
        #Se guarda momentaneamente la posición en la que quedaría
        auxPos=[playerPos[0]-2, playerPos[1]-1]
        if(environment[auxPos[0]][auxPos[1]]!=rival): #Se revisa que la casilla no esté ocupada por el otro jugador
            moves[1]= True #Si no está ocupada, se dice que se puede mover ahí
    #una arriba dos derecha:
    if (playerPos[0]-1>=0 and playerPos[1]+2<=7): #Se revisa que caiga dentro del tablero
        #Se guarda momentaneamente la posición en la que quedaría
        auxPos=[playerPos[0]-1, playerPos[1]+2]
        if(environment[auxPos[0]][auxPos[1]]!=rival): #Se revisa que la casilla no esté ocupada por el otro jugador
            moves[2]= True #Si no está ocupada, se dice que se puede mover ahí
    #dos arriba una derecha:
    if (playerPos[0]-2>=0 and playerPos[1]+1<=7): #Se revisa que caiga dentro del tablero
        #Se guarda momentaneamente la posición en la que quedaría
        auxPos=[playerPos[0]-2, playerPos[1]+1]
        if(environment[auxPos[0]][auxPos[1]]!=rival): #Se revisa que la casilla no esté ocupada por el otro jugador
            moves[3]= True #Si no está ocupada, se dice que se puede mover ahí
    #una abajo dos derecha:
    if (playerPos[0]+1<=7 and playerPos[1]+2<=7): #Se revisa que caiga dentro del tablero
        #Se guarda momentaneamente la posición en la que quedaría
        auxPos=[playerPos[0]+1, playerPos[1]+2]
        if(environment[auxPos[0]][auxPos[1]]!=rival): #Se revisa que la casilla no esté ocupada por el otro jugador
            moves[4]= True #Si no está ocupada, se dice que se puede mover ahí
    #dos abajo una derecha:
    if (playerPos[0]+2<=7 and playerPos[1]+1<=7): #Se revisa que caiga dentro del tablero
        #Se guarda momentaneamente la posición en la que quedaría
        auxPos=[playerPos[0]+2, playerPos[1]+1]
        if(environment[auxPos[0]][auxPos[1]]!=rival): #Se revisa que la casilla no esté ocupada por el otro jugador
            moves[5]= True #Si no está ocupada, se dice que se puede mover ahí
    #una abajo dos izquierda:
    if (playerPos[0]+1<=7 and playerPos[1]-2>=0): #Se revisa que caiga dentro del tablero
        #Se guarda momentaneamente la posición en la que quedaría
        auxPos=[playerPos[0]+1, playerPos[1]-2]
        if(environment[auxPos[0]][auxPos[1]]!=rival): #Se revisa que la casilla no esté ocupada por el otro jugador
            moves[6]= True #Si no está ocupada, se dice que se puede mover ahí
    #dos abajo una izquierda:
    if (playerPos[0]+2<=7 and playerPos[1]-1>=0): #Se revisa que caiga dentro del tablero
        #Se guarda momentaneamente la posición en la que quedaría
        auxPos=[playerPos[0]+2, playerPos[1]-1]
        if(environment[auxPos[0]][auxPos[1]]!=rival): #Se revisa que la casilla no esté ocupada por el otro jugador
            moves[7]= True #Si no está ocupada, se dice que se puede mover ahí
    return moves


##Método que recibe un entero que representa al jugador y retorna la posición de este en una lista
##1 = jugador Humano - caballo negro
##2 = jugador cpu - caballo blanco
##playePos=[xPos, yPos]
def findPlayer(player):
    playerPos = [-1,-1]
    ##Se recorre el arreglo hasta que lo que hay en una posición del ambiente sea igual a lo que se busca 
    for i in range(len(environment)):
        for j in range(len(environment[i])):
            if(environment[i][j]==player):
                playerPos[0]=i
                playerPos[1]=j
    return playerPos

##Metodo que recibe un jugador y una direccion para poder moverlo
def movePlayer(player,move):
    playerPos = findPlayer(player)
    global whiteHorseScore
    global blackHorseScore
    global environment
 
    #Se hara el movimiento segun la direccion dada 
    if(move == 0):
        environment[playerPos[0],playerPos[1]] = 0
        playerPos = [playerPos[0]-1,playerPos[1]-2]
    if(move == 1):
        environment[playerPos[0],playerPos[1]] = 0
        playerPos = [playerPos[0]-2,playerPos[1]-1]
    if(move == 2):
        environment[playerPos[0],playerPos[1]] = 0
        playerPos = [playerPos[0]-1,playerPos[1]+2]
    if(move == 3):
        environment[playerPos[0],playerPos[1]] = 0
        playerPos = [playerPos[0]-2,playerPos[1]+1]
    if(move == 4):
        environment[playerPos[0],playerPos[1]] = 0
        playerPos = [playerPos[0]+1,playerPos[1]+2]
    if(move == 5):
        environment[playerPos[0],playerPos[1]] = 0
        playerPos = [playerPos[0]+2,playerPos[1]+1]
    if(move == 6):
        environment[playerPos[0],playerPos[1]] = 0
        playerPos = [playerPos[0]+1,playerPos[1]-2]
    if(move == 7):
        environment [playerPos[0],playerPos[1]] = 0
        playerPos = [playerPos[0]+2,playerPos[1]-1]
    
    
    auxPos = playerPos
    #Si al moverse recoge un objeto adicionar los puntos necesarios
    #Cesped = 3,flores = 4, manzanas = 5
    #Valen 1,3 y 5 puntos respectivamente
    if(environment[auxPos[0]][auxPos[1]]==3):
        if(player == 1):
            blackHorseScore = blackHorseScore + 1
        else:
            whiteHorseScore = whiteHorseScore + 1
    if(environment[auxPos[0]][auxPos[1]]==4):
        if(player == 1):
            blackHorseScore = blackHorseScore + 3
        else:
            whiteHorseScore = whiteHorseScore + 3
    if(environment[auxPos[0]][auxPos[1]]==5):
        if(player == 1):
            blackHorseScore = blackHorseScore + 5
        else:
            whiteHorseScore = whiteHorseScore + 5
    environment[auxPos[0],auxPos[1]]=player
    return environment






print(blackHorseScore,whiteHorseScore)
print(environment)
print("----------------------------------------------------------------------------------------")
print(movePlayer(1,0))
print("----------------------------------------------------------------------------------------")
print(movePlayer(2,0))
print(blackHorseScore,whiteHorseScore)

