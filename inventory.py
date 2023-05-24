"""
This is my inventory file
"""

#class for inventory
class Inventory:
    def __init__(self, name, description):
        self.name = name
        self.description = description

Gun = Inventory("Gun", "A weapon used for fighting")
Food = Inventory("Food", "An item used to restore health")
Key = Inventory("Key", "An item used to unlock a door")
Bandage = Inventory("Bandage", "An item used to restore health")
