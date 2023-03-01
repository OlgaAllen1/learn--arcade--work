class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():
# Creating the list of rooms and adding room 0
    room_list = []
    room = Room("You are in the Guest bedroom. \n"
                "There is a room to the North and the South Hall is to the East."
                , 3, 1, None, None)

# Adding room 1 to the list
    room_list.append(room)
    room = Room("You are in the South Hall. \n"
                " You can move to the North, East and West."
                , 4, 2, None, 0)

# Adding room 2 to the list
    room_list.append(room)
    room = Room("You are in the Dining Room. \n"
                " The kitchen is on the North and you can go to the West to reach South Hall."
                , 5, None, None, 1)

#Adding room 3 to the list
    room_list.append(room)
    room = Room("You are in the Master Bedroom. \n"
                "You can to to North Hall by heading East and the guest bedroom is to the South."
                , None, 4, 0, None)

#Adding room 4 to the list
    room_list.append(room)

#Create a variable called room. Set it equal to a new instance of the Room class
    room = Room("You are in the torch-lit hallway. \n "
                "You can go any direction."
                , 6, 5, 1, 3)

#Adding room 5 to the list
    room_list.append(room)
    room = Room("You are in the kitchen. \n "
                "You can go West or South."
                , None, None, 2, 4)

#Adding room 6 to the list
    room_list.append(room)
    room = Room("You are on the Balcony. \n"
                " You can only go the South."
                , None, None, 4, None)
    room_list.append(room)

    current_room = 0

# While loop
    done = False
    while not done:
        print()
        print(room_list[current_room].description)
        answer = input("What direction? (Q is for quit) ").upper()

        # Conditions for moving North
        if answer == 'N' or answer == "NORTH":
            next_room = room_list[current_room].north
            if next_room is None:
                print("There is no room on the North.")
            else:
                current_room = next_room

        # Conditions for moving East
        elif answer == 'E' or answer == "EAST":
            next_room = room_list[current_room].east
            if next_room is None:
                print("There is no room on the East.")
            else:
                current_room = next_room

        # Conditions for moving South
        elif answer == 'S' or answer == "SOUTH":
            next_room = room_list[current_room].south
            if next_room is None:
                print("There is no room on the South.")
            else:
                current_room = next_room

        # Conditions for moving West
        elif answer == 'W' or answer == "WEST":
            next_room = room_list[current_room].west
            if next_room is None:
                print("There is no room on the West.")
            else:
                current_room = next_room

        # Adding the option to quit the game
        elif answer == "Q":
            print("The end")
            done = True

if __name__ == "__main__":
main()

