class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():

    room_list = []
    room = Room("You are in the guest bedroom. \n"
                "There is a room to the North and the South Hall is to the East."
                , 3, 1, None, None)
    room_list.append(room)
    room = Room("You are in the South Hall. \n"
                " You can move to the North, East and West."
                , 4, 2, None, 0)
    room_list.append(room)
    room = Room("You are in the Dining Room. \n"
                " The kitchen is up North and you can go west to reach South Hall."
                , 5, None, None, 1)
    room_list.append(room)
    room = Room("You are in the Master Bedroom. \n"
                "You can to to North Hall by heading East and the guest bedroom is to the south."
                , None, 4, 0, None)
    room_list.append(room)
    room = Room("You are in the torch-lit hallway. \n "
                "You can go all 4 directions."
                , 6, 5, 1, 3)
    room_list.append(room)
    room = Room("You are in the kitchen. \n "
                "You can go West or South."
                , None, None, 2, 4)
    room_list.append(room)
    room = Room("You are on the Balcony. \n"
                " You can only go South."
                , None, None, 4, None)
    room_list.append(room)

    current_room = 0

    done = False
    while not done:
        print()
        print(room_list[current_room].description)
        answer = input("What direction? (Q is for quit) ").upper()

        # North
        if answer == 'N' or answer == "NORTH":
            next_room = room_list[current_room].north
            if next_room is None:
                print("There is no room on the North.")
            else:
                current_room = next_room

        # East
        elif answer == 'E' or answer == "EAST":
            next_room = room_list[current_room].east
            if next_room is None:
                print("There is no room on the East.")
            else:
                current_room = next_room

        # South
        elif answer == 'S' or answer == "SOUTH":
            next_room = room_list[current_room].south
            if next_room is None:
                print("There is no room on the South.")
            else:
                current_room = next_room

        # West
        elif answer == 'W' or answer == "WEST":
            next_room = room_list[current_room].west
            if next_room is None:
                print("There is no room on the West.")
            else:
                current_room = next_room

        elif answer == "Q":
            print("The end")
            done = True
main()

