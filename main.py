import re
from shutil import move
from xml.etree.ElementPath import find
import numpy as np
from board import board
from stack import Stack
from node import Node

# environment=np.array([[0,0,0,3,0,4,0,0],
#                     [0,3,0,4,0,3,0,0],
#                     [3,0,0,0,0,0,0,0],
#                     [0,3,0,1,2,0,0,4],
#                     [3,0,0,0,3,0,3,0],
#                     [3,0,0,0,4,0,0,3],
#                     [0,4,3,0,0,5,0,0],
#                     [0,3,0,0,0,0,3,0]])
# print(environment)
 
#Función que genera el estado inicial del juego, el cual llevará el nodo raíz
#El estado está representado así:
#[ambienteActual, puntosHumano, puntosCPU]
def initStatus():
    status=[board(), 0, 0]
    return status

##Momentaneamente, esta función recibe un entero que representa al jugador para el cuál se quieren obtener los movimientos posibles
##1 = jugador Humano - caballo negro
##2 = jugador cpu - caballo blanco
##La función retorna una lista llena de booleanos que representan todas los movimientos posibles por el jugador determinado:
##u=casilla hacia arriba, l=casilla hacia la izquierda, r=casilla hacia la derecha, d=casilla hacia abajo 
##[1u2l, 2u1l, 1u2r, 2u1r, 1d2r, 2d1r, 1d2l, 2d1l]
def possibleMoves(player, environment):
    actualEnvironment=environment.copy()
    moves = [False, False, False, False, False, False, False, False]
    playerPos = findPlayer(player, actualEnvironment)
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
        if(actualEnvironment[auxPos[0]][auxPos[1]]!=rival): #Se revisa que la casilla no esté ocupada por el otro jugador
            moves[0]= True #Si no está ocupada, se dice que se puede mover ahí
    #dos arriba una izquierda:
    if (playerPos[0]-2>=0 and playerPos[1]-1>=0): #Se revisa que caiga dentro del tablero
        #Se guarda momentaneamente la posición en la que quedaría
        auxPos=[playerPos[0]-2, playerPos[1]-1]
        if(actualEnvironment[auxPos[0]][auxPos[1]]!=rival): #Se revisa que la casilla no esté ocupada por el otro jugador
            moves[1]= True #Si no está ocupada, se dice que se puede mover ahí
    #una arriba dos derecha:
    if (playerPos[0]-1>=0 and playerPos[1]+2<=7): #Se revisa que caiga dentro del tablero
        #Se guarda momentaneamente la posición en la que quedaría
        auxPos=[playerPos[0]-1, playerPos[1]+2]
        if(actualEnvironment[auxPos[0]][auxPos[1]]!=rival): #Se revisa que la casilla no esté ocupada por el otro jugador
            moves[2]= True #Si no está ocupada, se dice que se puede mover ahí
    #dos arriba una derecha:
    if (playerPos[0]-2>=0 and playerPos[1]+1<=7): #Se revisa que caiga dentro del tablero
        #Se guarda momentaneamente la posición en la que quedaría
        auxPos=[playerPos[0]-2, playerPos[1]+1]
        if(actualEnvironment[auxPos[0]][auxPos[1]]!=rival): #Se revisa que la casilla no esté ocupada por el otro jugador
            moves[3]= True #Si no está ocupada, se dice que se puede mover ahí
    #una abajo dos derecha:
    if (playerPos[0]+1<=7 and playerPos[1]+2<=7): #Se revisa que caiga dentro del tablero
        #Se guarda momentaneamente la posición en la que quedaría
        auxPos=[playerPos[0]+1, playerPos[1]+2]
        if(actualEnvironment[auxPos[0]][auxPos[1]]!=rival): #Se revisa que la casilla no esté ocupada por el otro jugador
            moves[4]= True #Si no está ocupada, se dice que se puede mover ahí
    #dos abajo una derecha:
    if (playerPos[0]+2<=7 and playerPos[1]+1<=7): #Se revisa que caiga dentro del tablero
        #Se guarda momentaneamente la posición en la que quedaría
        auxPos=[playerPos[0]+2, playerPos[1]+1]
        if(actualEnvironment[auxPos[0]][auxPos[1]]!=rival): #Se revisa que la casilla no esté ocupada por el otro jugador
            moves[5]= True #Si no está ocupada, se dice que se puede mover ahí
    #una abajo dos izquierda:
    if (playerPos[0]+1<=7 and playerPos[1]-2>=0): #Se revisa que caiga dentro del tablero
        #Se guarda momentaneamente la posición en la que quedaría
        auxPos=[playerPos[0]+1, playerPos[1]-2]
        if(actualEnvironment[auxPos[0]][auxPos[1]]!=rival): #Se revisa que la casilla no esté ocupada por el otro jugador
            moves[6]= True #Si no está ocupada, se dice que se puede mover ahí
    #dos abajo una izquierda:
    if (playerPos[0]+2<=7 and playerPos[1]-1>=0): #Se revisa que caiga dentro del tablero
        #Se guarda momentaneamente la posición en la que quedaría
        auxPos=[playerPos[0]+2, playerPos[1]-1]
        if(actualEnvironment[auxPos[0]][auxPos[1]]!=rival): #Se revisa que la casilla no esté ocupada por el otro jugador
            moves[7]= True #Si no está ocupada, se dice que se puede mover ahí
    return moves


##Método que recibe un entero que representa al jugador y retorna la posición de este en una lista
##1 = jugador Humano - caballo negro
##2 = jugador cpu - caballo blanco
##playePos=[xPos, yPos]
def findPlayer(player, environment):
    actualEnvironment=environment.copy()
    playerPos = [-1,-1]
    ##Se recorre el arreglo hasta que lo que hay en una posición del ambiente sea igual a lo que se busca 
    for i in range(len(actualEnvironment)):
        for j in range(len(actualEnvironment[i])):
            if(actualEnvironment[i][j]==player):
                playerPos[0]=i
                playerPos[1]=j
    return playerPos

##Metodo que recibe un jugador y una direccion para poder moverlo
def movePlayer(player, move, status):
    newStatus=[status[0].copy(), status[1], status[2]]
    playerPos = findPlayer(player, status[0])
    #Se hara el movimiento segun la direccion dada 
    if(move == 0):
        newStatus[0][playerPos[0],playerPos[1]] = 0
        playerPos = [playerPos[0]-1,playerPos[1]-2]
    if(move == 1):
        newStatus[0][playerPos[0],playerPos[1]] = 0
        playerPos = [playerPos[0]-2,playerPos[1]-1]
    if(move == 2):
        newStatus[0][playerPos[0],playerPos[1]] = 0
        playerPos = [playerPos[0]-1,playerPos[1]+2]
    if(move == 3):
        newStatus[0][playerPos[0],playerPos[1]] = 0
        playerPos = [playerPos[0]-2,playerPos[1]+1]
    if(move == 4):
        newStatus[0][playerPos[0],playerPos[1]] = 0
        playerPos = [playerPos[0]+1,playerPos[1]+2]
    if(move == 5):
        newStatus[0][playerPos[0],playerPos[1]] = 0
        playerPos = [playerPos[0]+2,playerPos[1]+1]
    if(move == 6):
        newStatus[0][playerPos[0],playerPos[1]] = 0
        playerPos = [playerPos[0]+1,playerPos[1]-2]
    if(move == 7):
        newStatus[0][playerPos[0],playerPos[1]] = 0
        playerPos = [playerPos[0]+2,playerPos[1]-1]
    
    auxPos = playerPos
    #Si al moverse recoge un objeto adicionar los puntos necesarios
    #Cesped = 3,flores = 4, manzanas = 5
    #Valen 1,3 y 5 puntos respectivamente
    if(newStatus[0][auxPos[0]][auxPos[1]]==3):
        if(player == 1):
            newStatus[1] = newStatus[1] + 1
        else:
            newStatus[2] = newStatus[2] + 1
    if(newStatus[0][auxPos[0]][auxPos[1]]==4):
        if(player == 1):
           newStatus[1] = newStatus[1] + 3
        else:
            newStatus[2] = newStatus[2] + 3
    if(newStatus[0][auxPos[0]][auxPos[1]]==5):
        if(player == 1):
            newStatus[1] = newStatus[1] + 5
        else:
            newStatus[2] = newStatus[2] + 5
    newStatus[0][auxPos[0],auxPos[1]]=player
    return newStatus

def expandNode(node):
    actualPlayer=-1
    nextPlayer=-1
    newStatus=[node.getStatus()[0].copy(), node.getStatus()[1], node.getStatus()[2]]
    #print(newStatus[0])
    if node.getType()=="MAX":
        actualPlayer=2
        nextPlayer=1
    else:
        actualPlayer=1
        nextPlayer=2
    allowedMoves=possibleMoves(actualPlayer, newStatus[0]) #Determinamos en qué direcciones debería poderse mover el agente
    children = [None, None, None, None, None, None, None, None]
    for i in range(0,8):
        if allowedMoves[i]:
            children[i]=Node(movePlayer(actualPlayer, i, newStatus), node, nextPlayer, node.getDepth()+1, "xd", i)
    return children

def distanceToObject(status):
    cpuPos=findPlayer(2,status[0])
    auxDis=999999
    for i in range(len(status[0])):
        for j in range(len(status[0][i])):
            if(status[0][i][j]!=1 and status[0][i][j]!=2 and status[0][i][j]!=0):
                newDis=manhattan(cpuPos[0], cpuPos[1], i, j)
                auxDis=min(newDis, auxDis)
    return auxDis
def manhattan(x0,y0,x1,y1):
    distance=abs(x1-x0)+abs(y1-y0)
    return distance

#Funcion para calcular la utilidad
def deepestNodeUtility(stack, depth):
    for i in range (len(stack.elements)):
        if goalNode(stack.elements[i]):
            #stack.elements[i].setUtility(stack.elements[i].getStatus()[2])#*1/distanceToObject(stack.elements[i].getStatus()))
            stack.elements[i].setUtility(stack.elements[i].getStatus()[2]*1/distanceToObject(stack.elements[i].getStatus()))
        if stack.elements[i].getDepth()==depth:
            #print("El nodo a verificar tiene profundidad: "+str(stack.elements[i].getDepth()))
            #stack.elements[i].setUtility(stack.elements[i].getStatus()[2])
            stack.elements[i].setUtility(stack.elements[i].getStatus()[2]*1/distanceToObject(stack.elements[i].getStatus()))
    return stack

#Funcion para ver si un nodo es meta
def goalNode(node):
    aux_board = node.getStatus()[0]
    objCounter = 0
    goal = False
    for i in range(len(aux_board)):
        for j in range(len(aux_board[i])):
            if(aux_board[i][j]==3 or  aux_board[i][j]==4 or aux_board[i][j]==5):
                objCounter+=1
    if(objCounter>=1):
        goal = False
    else:
        goal = True
    return goal

def sorter(node):
    return node.getDepth()

def utility(stack):
    auxStack=stack
    auxStack.elements.sort(key=sorter)
    maxDepth=getMaxDepth(auxStack)
    for i in range (maxDepth, 0, -1):
        print ("Profundidad: "+str(i))
        for j in range(len(auxStack.elements)):
            if i==1:

                if auxStack.elements[j].getDepth() == 1:
                    print("Caso profundidad 1: Utilidad del nodo hijo: "+ str(auxStack.elements[j].getUtility())+", La utilidad del nodo padre es: "+str(auxStack.elements[i].getParent().getUtility()))
                    if auxStack.elements[j].getParent().getType() == 'MAX':
                        if auxStack.elements[j].getUtility() >  auxStack.elements[j].getParent().getUtility():
                            auxStack.elements[j].getParent().setUtility(auxStack.elements[j].getUtility())
                            print("Se subió "+ str( auxStack.elements[j].getUtility() ))
                            auxStack.elements[j].getParent().setOperator(auxStack.elements[j].getOperator())
                    else:
                        if auxStack.elements[j].getUtility() <  auxStack.elements[j].getParent().getUtility():
                            auxStack.elements[j].getParent().setUtility(auxStack.elements[j].getUtility())
                            print("Se subió "+ str( auxStack.elements[j].getUtility() ))
                            auxStack.elements[j].getParent().setOperator(auxStack.elements[j].getOperator())


            elif (j!=0 and auxStack.elements[j].getDepth() == i):
                if auxStack.elements[j].getParent().getType() == 'MAX':
                    print("Utilidad del nodo hijo: "+ str(auxStack.elements[j].getUtility())+", La utilidad del nodo padre es: "+str(auxStack.elements[j].getParent().getUtility()))
                    auxStack.elements[j].getParent().setUtility(max(auxStack.elements[j].getUtility(), auxStack.elements[j].getParent().getUtility()))
                    print("Se subió "+ str(max(auxStack.elements[j].getUtility(), auxStack.elements[j].getParent().getUtility())) )
                else:
                    print("Utilidad del nodo hijo: "+ str(auxStack.elements[j].getUtility())+", La utilidad del nodo padre es: "+str(auxStack.elements[j].getParent().getUtility()))
                    auxStack.elements[j].getParent().setUtility(min(auxStack.elements[j].getUtility(), auxStack.elements[j].getParent().getUtility()))
                    print("Se subió "+ str(min(auxStack.elements[j].getUtility(), auxStack.elements[j].getParent().getUtility())) )
    print("La utilidad calculada es de: "+ str(auxStack.elements[0].getUtility())+ ", el movimiento a realizar es: "+str(auxStack.elements[0].getOperator()))
    return auxStack


def deleteDepth(stack):
    newStack= Stack()
    for i in range(len(stack.elements)):
        maxDepth=getMaxDepth(stack)
        if stack.elements[i].getDepth() != maxDepth:
            newStack.push(stack.elements[i])
    return newStack

def getMaxDepth(stack):
    maxDepth=-1
    for i in range(len(stack.elements)):
        auxDepth=stack.elements[i].getDepth()
        maxDepth=max(auxDepth, maxDepth)
    return maxDepth

def createTree(depth, root):
    actualDepth=0
    minmaxTree = Stack()
    minmaxTree.push(root)
    #print(minmaxTree.peek().getStatus()[0])
    #print("Nodos de profundidad 0: 1")
    while True:
        counter = 0
        actualDepth=actualDepth+1
        for i in range (minmaxTree.length()):
            if(not minmaxTree.elements[i].getExpanded()):
                n=minmaxTree.elements[i]
                createdNodes = expandNode(n)
                for j in range(0,8):
                    if not createdNodes[j] is None:
                        counter+=1
                        # if actualDepth==3:
                        #     print(createdNodes[j].getStatus()[0])
                        minmaxTree.push(createdNodes[j])
                
                minmaxTree.elements[i].setExpanded(True)
        #print("Nodos de profundidad "+ str(actualDepth)+": "+str(counter))
        if(actualDepth==depth):
            minmaxTree=deepestNodeUtility(minmaxTree, depth)
            break
    return minmaxTree


# print(distanceToObject([np.array([  [0,0,0,0,0,0,0,0],
#                                     [0,3,0,0,0,0,0,0],
#                                     [3,0,0,0,0,0,0,0],
#                                     [0,0,0,1,2,0,0,0],
#                                     [3,0,0,0,0,0,0,0],
#                                     [3,0,0,0,0,0,0,3],
#                                     [0,4,3,0,0,0,0,0],
#                                     [0,3,0,0,0,0,3,0]]), 0, 0]))
# prueba=createTree(6, Node(initStatus(), None, 2, 0, "xd", -1))
# print(len(prueba.elements))
# prueba = utility(prueba)
# print(prueba.elements[0].getOperator())
#prueba=createTree(6, Node(movePlayer(2, prueba.elements[0].getOperator(), prueba.elements[0].getStatus()), None, 2, 0, "xd", -1))
# print(len(prueba.elements))
# prueba = utility(prueba)
# print(prueba.elements[0].getOperator())
# prueba=createTree(6, Node(movePlayer(2, prueba.elements[0].getOperator(), prueba.elements[0].getStatus()), None, 2, 0, "xd", -1))
# print(len(prueba.elements))
# prueba = utility(prueba)
# print(prueba.elements[0].getOperator())
#utility(prueba)
#print(prueba.peek())
# print(prueba.peek().getUtility())
# auxStatus=[environment,0,0]
# print(movePlayer(1, 0, auxStatus))
# print(movePlayer(1, 0))
# print(blackHorseScore)
# print(movePlayer(2, 2))
# print(whiteHorseScore)
# print(movePlayer(1, 2))
# print(blackHorseScore)
# print(movePlayer(2, 5))
# print(whiteHorseScore)