#Se define la clase Node, usada para implementar el algoritmo minimax
class Node:
  #Se define el método constructor
  def __init__(self, status, parent, player, depth, utility):
    self.status = status
    self.parent = parent
    if(player==1):
        self.type="MIN"
    else:
        self.type="MAX"
    
    self.depth = depth
    if(player==1):
        self.utility=999999
    else:
        self.utility=-999999
    self.expanded=False

  #Método bobo
  def ImNode(self):
    return "Hola, soy un nodo"


#Getter del estado del nodo
  def getStatus(self):
    return self.status

    #Getter del padre del nodo
  def getParent(self):
    return self.parent

    #Getter del tipo del nodo
  def getType(self):
    return self.type

  #Getter de la profundidad del nodo
  def getDepth(self):
    return self.depth

    #Getter de la utilidad del nodo
  def getUtility(self):
    return self.utility

    #Getter de la expansión del nodo
  def getExpanded(self):
    return self.expanded
    
    #Setter de la expansión del nodo
  def setExpanded(self, bool):
    self.expanded=bool
    return bool

    #Setter de la utilidad del nodo
  def setUtility(self, uti):
    self.utility=uti
    return uti
