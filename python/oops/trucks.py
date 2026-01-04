from vehicle import Vehicle as v

class Truck(v):
    pass

    def __str__(self):
        Info1=super().__str__()
        if(self.trailer):
            Info2=f'It requires trailer'
        else:
            Info2=f"It doesn't require a trailer."
            
        return f'{Info1}\n{Info2}'
            
        
    