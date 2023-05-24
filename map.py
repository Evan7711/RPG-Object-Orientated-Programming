"""
This is my map file
"""
import inventory

# class for rooms in the map
class Rooms:
  
    def __init__(self, room, description, directions = None, items = None):
        self.room = room
        self.description = description
        self.directions = directions
        self.items = []
        self.exits = {}
    
    def add_item(self, items):
        self.items.append(inventory)

Kitchen = Rooms("Kitchen", "You enter the main location for all food in the house")
Bedroom = Rooms("Bedroom", "You enter a place to rest perhaps")
Bathroom = Rooms("Bathroom", "You enter a room that should be private")
LivingRoom = Rooms("Living Room", "You are in a public room for socializing")
Basement = Rooms("The Basement", "You enter a dark and scary place")
Attic = Rooms("The Attic", "You enter a creepy place that can only be accessed via ladder")
places = [Kitchen, Bedroom, Bathroom, LivingRoom, Attic, Basement]         
# adds items from inventory file to specific rooms
Kitchen.add_item(inventory.Food)
Bedroom.add_item(inventory.Gun)
Bathroom.add_item(inventory.Bandage)
Basement.add_item(inventory.Key)

# adds possible directions to go in each room
Kitchen.directions = {"right": LivingRoom.room}
LivingRoom.directions = {"left": Kitchen.room, "right": Bedroom.room, "down": Basement.room}
Bedroom.directions = {"left": LivingRoom.room, "right": Bathroom.room, "up": Attic.room}
Bathroom.directions = {"left": Bedroom.room}
Attic.directions = {"down": Bedroom.room}
Basement.directions = {"up": LivingRoom.room}