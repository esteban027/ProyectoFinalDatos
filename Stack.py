class Stack:
    def __init__(self):
        self.items = []      

    
    def isEmpty(self):
        return self.items == []
        
    def push(self,item):
        if len(self.items) <=5:
            self.items.append(item)
        else: "algo"

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    
        
        
        
        
