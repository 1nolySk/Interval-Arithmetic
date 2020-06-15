class Ia():
    
    def __init__(self, a,b):
        self.x = float(min(a,b))
        self.y = float(max(a,b))
    
    def __add__(self, ob):
        if isinstance(ob, Ia):
            return Ia(self.x+ob.x , self.y+ob.y)
        return Ia(self.x+ob , self.y+ob)
        
    def __sub__(self, ob):
        if isinstance(ob, Ia):
            return Ia(self.x-ob.y , self.y-ob.x)
        return Ia(self.x-ob , self.y-ob)
    
    def __rsub__(self, ob):
        if isinstance(ob, Ia):
            return Ia(ob.y - self.x, ob.x-self.y)
        return Ia(ob-self.x , ob-self.y)
    
    def __mul__(self, ob):
        if isinstance(ob, Ia):
            t= [self.x*ob.x,
                self.y*ob.y,
                self.x*ob.y,
                self.y*ob.x]
            return Ia(min(t), max(t))
        
        t = [self.x*ob, self.y*ob]
        
        return Ia(min(t), max(t))
        
    def __truediv__(self, ob):
        
        if isinstance(ob, Ia):
            t= [self.x*(1/ob.x),
                self.y*(1/ob.y),
                self.x*(1/ob.y),
                self.y*(1/ob.x)]
            
            return Ia(min(t), max(t))
        
        t= [self.x/ob , self.y/ob]
        return Ia(min(t), max(t))
    
            
        
    def __rtruediv__(self, ob):
        
        if isinstance(ob, Ia):
            t= [ob.x*(1/self.x),
                ob.y*(1/self.y),
                ob.x*(1/self.y),
                ob.y*(1/self.x),]
            
            return Ia(min(t), max(t))
        
        t= [ob/self.x , ob/self.y]
        
        return Ia(min(t), max(t))
        

    def __eq__(self, ob):
        if isinstance(ob, Ia):
            if self.x == ob.x and self.y==ob.y:
                return True
        else:
            if self.x == ob or self.y==ob:
                return True
        return False
    
    def __str__(self):
        return (f"[{self.x}, {self.y}]")
        
