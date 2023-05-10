#------------------------------------------------------------------------------
# Title: Home Invasion
# Assignment: OOP
# Date: 09/05/23
# Student; Evan Smart
# Version: 1.0
#------------------------------------------------------------------------------
"""
Assignment for using OOp to create an rpg

This file is used for actions and to combine all other files
"""
import inventory
import map

map.Location.current_location = map.LivingRoom
print(map.Location.current_location.description)
