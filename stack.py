#Clase Pila, usada para la implementación del arbol minimax
class Stack: 
    def __init__(self): 
        self.elements = [] 
        
    def push(self, data): 
        self.elements.append(data) 
        return data 
    
    def pop(self): 
        return self.elements.pop() 
        
    def peek(self): 
        return self.elements[-1] 
        
    def is_empty(self): 
        return len(self.elements) == 0

    def showStack(self):
        print(self.elements)

    def length(self):
        return len(self.elements)