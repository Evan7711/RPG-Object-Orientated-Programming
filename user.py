"""
This is my user file that allows for movement
"""

from map import *

# class for movement for player
class Player:
    def __init__(self, current_location):
        self.current_location = current_location
        self.directions = {"left": Kitchen.room, "right": Bedroom.room, "down": Basement.room}

# function for moving the players location
    def Movement(self, direction):
      for key in self.directions:
          if direction == key:  
              self.current_location = self.directions[key]
