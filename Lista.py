class Lista:
    
    def __init__(self):
        self.items=[]
    def agregarAlFinal(self,x):
        self.items.append(x)
    def agregarAlInicio(self,x):
        self.items.insert(0, x)
    def eliminarAlinicio(self):
        self.items.pop(0)
    def eliminarAlFinal(self):
        self.items.pop()
    
        
        
        
    