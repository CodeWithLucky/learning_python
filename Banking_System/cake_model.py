from datetime import datetime


class Cake():

    name:str
    shape:str
    flavour:str
    size:int

    def __init__(self, name:str, shape:str, flavour:str, size:int):
        self.name = name
        self.shape = shape
        self.flavour = flavour
        self.size = size
            
    def to_json(cake):
            return {
                "name" : cake.name,
                "flavour" : cake.flavour,
                "shape" : cake.shape,
                "size" : cake.size,
                "created on" : str(datetime.now())
            }