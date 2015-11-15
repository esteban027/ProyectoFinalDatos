
class Cola:

 
    def __init__(self):
        self.items=[]
        
    def encolar(self, x):
        if len(self.items) <=15:
            self.items.append(x)
        else:
            return False
        
    
    def desEncolar(self):
        
        try:
            return self.items.pop(0)
        except:
            raise ValueError("La cola esta vacia")
    
    def esVacia(self):
        
        return self.items == []





        
    
