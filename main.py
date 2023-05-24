#------------------------------------------------------------------------------
# Title: Home Invasion
# Assignment: OOP
# Date: 09/05/23
# Student; Evan Smart
# Version: 1.0
#------------------------------------------------------------------------------
"""
Assignment for using OOP to create an rpg

This file is used for actions and to combine all other files
"""
# Importing files with classes
from inventory import *
from map import *
from user import *
player = Player(LivingRoom)
# empty inventory for items to be added to
inventory = []
# prints players intial location
print(player.current_location.description)
# main code for players choices
while True:
    Choice = (input("What would you like to do: Move, Check Inventory, or Quit: ").lower())
    if Choice == "move":
      print("What way would you like to go:")
      for option in player.directions.keys():
         print(f" - {option}")
      direction = input("Choice: ").lower()
      player.Movement(direction)
      if player.current_location == "Kitchen":
          print(Kitchen.description)
          player.directions = Kitchen.directions
          for item in Kitchen.items:
              while True:
                  Search = (input(f"There is some {Food.name} would you like it? ").lower())
                  if Search == "yes":
                      inventory.append("Food")
                      print(f"{Food.name} was added to inventory")
                      Kitchen.items.clear()
                      break
                  elif Search == "no":
                      print("It will still be here later if needed")
                      break
                  else:
                      print("That's not an option")
      elif player.current_location == "Bedroom":
          print(Bedroom.description)
          player.directions = Bedroom.directions
          for item in Bedroom.items:
              while True:
                  Search = (input(f"There is a {Gun.name} would you like it? ").lower())
                  if Search == "yes":
                      inventory.append("Gun")
                      print(f"{Gun.name} was added to inventory")
                      Bedroom.items.clear()
                      break
                  elif Search == "no":
                      print("It will still be here later if needed")
                      break
                  else:
                      print("That's not an option")
      elif player.current_location == "The Attic":
          print(Attic.description)
          player.directions = Attic.directions
      elif player.current_location == "The Basement":
          print(Basement.description)
          player.directions = Basement.directions
          for item in Basement.items:
              while True:
                  Search = (input(f"There is a {Key.name} would you like it? ").lower())
                  if Search == "yes":
                      inventory.append("Key")
                      print(f"{Key.name} was added to inventory")
                      Key.items.clear()
                      break
                  elif Search == "no":
                      print("It will still be here later if needed")
                      break
                  else:
                      print("That's not an option")
      elif player.current_location == "Bathroom":
          print(Bathroom.description)
          player.directions = Bathroom.directions
          for item in Bathroom.items:
              while True:
                  Search = (input(f"There is some {Bandage.name}'s would you like it? ").lower())
                  if Search == "yes":
                      inventory.append("Bandage")
                      print(f"{Bandage.name} was added to inventory")
                      Bathroom.items.clear()
                      break
                  elif Search == "no":
                      print("They will still be here later if needed")
                      break
                  else:
                      print("That's not an option")
      elif player.current_location == "Living Room":
          print(LivingRoom.description)
          player.directions = LivingRoom.directions
      else:
        print("Something went wrong")
    elif Choice == "quit":
        print("Thank you for playing")
        break
    elif Choice == "check inventory":
        print("Inventory: ")
        for item in inventory:
            print(f" - {item} ")
    else:
        print("YOu can't do that")
        