from tkinter import Tk

locs_list = [
    {
    "loc_name": "Spawn point",
    "desc": "Spawn point of the player",
    "items": "None",
    "next_loc": "B"
},
{
    "loc_name": "Point B",
    "desc": "Area lies a hidden chest.",
    "items": "a sword",
    "next_loc": "C"
}
]
class Map:
    def __init__(self):
        self.map = [] 

class Location:
    #next_loc is the node and is set to 'None' by default — node will not lead to anywhere by default.
    def __init__(self,loc_name,desc,items=None,next_loc=None,): 
        self.loc_name = loc_name 
        self.desc = desc
        self.items = items
        self.next_loc = next_loc
    
    def __repr__(self): 
        """
            Prints out location name, description and the next locations
        """
        return f"{self.loc_name} {self.desc} {self.items} {self.next_loc}" 
    
location = [Location(**locations) for locations in locs_list]

class Player:
    """ 
    Player's attributes. 
    """
    def __init__(self, name, health, dmg, location):
        self._name = name
        self._health = health
        self._dmg = dmg
        self._location = location #current
    
    @property
    def location(self): return self._location

    #sets the current location -- sets the changed location.
    @location.setter
    def location(self, new_loc): self._location = new_loc

    def move(self):
        """
            A method so the player can move from locatioon to the other, based on the player's input.
        """
        dest = input(str("Where would you like to go? ")).upper()
        for loc in locs_list:
            if loc["loc_name"] == self._location:
                if dest == loc["next_loc"]:
                    self._location = dest
                    return dest
        return "This is not a valid location."
    
    def __repr__(self): 
        """
            Prints out location name, description and the next locations
        """
        return f"{self._name} {self._health} {self._dmg} {self._location}" 

    
