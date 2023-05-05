class Movement:
    def __init__(location, row, column):
        location.row = row
        location.column = column
    def row(location, row):
            if Direction == "north" or Direction == "North":
                if location.row > 0:
                    location.row -= 1
                else:
                    print("you can't go that way")
            elif Direction == "south" or Direction == "South":
                if location.row < 3:
                    location.row += 1
                else:
                    print("you can't go that way")
    def column(location, column):
            if Direction == "East" or Direction == "east":
                if location.column > 0:
                    location.column -= 1
                else:
                    print("you can't go that way")
            elif Direction == "west" or Direction == "West":
                if location.column < 3:
                    location.column += 1
                else:
                    print("you can't go that way")

Direction = input("Would you like to travel North, South, East, West: ")
m = Movement(0, 2)
print(m.row)
print(m.column)