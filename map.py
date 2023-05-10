"""
This is my map file
"""
import inventory
# class for the rooms
class Rooms:
    def __init__(self, room, description, directions=None, items=None):
        self.room = room
        self.description = description
        self.directions = directions
        self.items = []
        self.exits = {}
    
    def add_item(self, items):
        self.items.append(inventory)

    def remove_items(self, items):
        self.items.remove(inventory)

class Location:
    def __init__(self):
        self.current_location = None
        self.room = {}

    def add_room(self, room):
        self.rooms[Rooms.room] = room

    def movement(self, direction):
        if direction in self.current_location.directions:
            self.current_location = self.rooms[self.current_location.directions[direction]]
            print(self.current_location.description)
        else:
            print("There's nothing in that direction")


Kitchen = Rooms("Kitchen", "The main location for all food in the house")
Bedroom = Rooms("Bedroom", "A place to rest perhaps")
Bathroom = Rooms("Bathroom", "A room that should be private")
LivingRoom = Rooms("Living Room", "A public room for socializing")
Basement = Rooms("The Basement", "A dark and scary place")
Attic = Rooms("The Attic", "A creepy place that can only be accessed via ladder")

Kitchen.add_item(inventory.Food)
Bedroom.add_item(inventory.Gun)
Bathroom.add_item(inventory.Bandage)
Basement.add_item(inventory.Key)

Kitchen.directions = {"right": LivingRoom.room}
LivingRoom.directions = {"left": Kitchen.room, "right": Bedroom.room, "down": Basement.room}
Bedroom.directions = {"left": LivingRoom.room, "right": Bathroom.room, "up": Attic.room}
Bathroom.directions = {"left": Bedroom.room}
Attic.directions = {"down": Bedroom.room}
Basement.directions = {"up": LivingRoom.room}