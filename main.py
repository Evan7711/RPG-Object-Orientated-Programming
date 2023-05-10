
 
class Self:
    def __init__(self, row, column):
        self.row = row
        self.column = column
    def Movement(row, column):
        Direction = input("Would you like to travel North, South, East, West: ")       
        if Direction == "north" or Direction == "North":
            if row > 0:
                row -= 1
            else:
                print("you can't go that way")
        elif Direction == "south" or Direction == "South":
            if row < 3:
                row += 1
            else:
                print("you can't go that way")
        elif Direction == "East" or Direction == "east":
            if column > 0:
                column -= 1
            else:
                print("you can't go that way")
        elif Direction == "west" or Direction == "West":
            if column < 3:
                column += 1
            else:
                print("you can't go that way")

s = Self.Movement(2, 0)
print(s.row)
print(s.column)