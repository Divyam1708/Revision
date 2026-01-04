import pyttsx3 as tts

class Vehicle():
    vehicle_count=1
    def __init__(self,company='Unknown',model='Unknown',wheels=0,size='Small',trailer=False,engine_capacity=0):
        self.id=Vehicle.vehicle_count
        self.wheels=wheels
        self.size=size
        self.trailer=trailer
        self.engine_capacity=engine_capacity
        self.company=company
        self.model=model
        Vehicle.vehicle_count=Vehicle.vehicle_count+1
        
    def __str__(self):
        Info=(f'Vehicle_no. ={self.id}\n{self.model} belongs to {self.company} and has an engine capicity of {self.engine_capacity}cc with {self.wheels} wheels.')
        return Info
    
    def __repr__(self):
        Info=f'Vehicle_count={self.vehicle_count}. Model= {self.model} => Company= {self.company}'
        return Info
    
    def speak_features():
        tts.speak()