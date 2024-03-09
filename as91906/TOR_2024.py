from tkinter import tk

#tutorial

locs_list = [
    {
    "name": "Spawn point",
    "desc": "Spawn point of the player",
    "next_loc": "B"
},
{
    "name": "Point B",
    "desc": "Area lies a hidden chest.",
    "next_loc": "C"
}
]

class Location:
    def __init__(self,name,desc,next_loc=None): #next_loc is the node and is set to 'None' by default — node will not lead to anywhere by default.
        self.name = name 
        self.desc = desc
        self.next_loc = next_loc
    
location = [Location(**locations) for locations in locs_list]

class Map:
    def __init__(self):
        self.map = [] 
    
    def add_locs():
        map.appen




