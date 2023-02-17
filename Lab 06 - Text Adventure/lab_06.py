class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():

    room_list = []
    room = Room("You are in the guest bedroom. "
                "There is a room to the North and the South Hall is to the East."
                "What direction?"
                , 3, 1, None, None)
    room_list.append(room)
    room = Room("You are in the South Hall."
                " You can move to the North, East and West."
                " What direction?"
                , 4, 2, None, 0)
    room_list.append(room)
    room = Room("You are in the Dining Room."
                " The kitchen is up North and you can go west to reach South Hall."
                " What direction?"
                , 5, None, None, 1)
    room_list.append(room)
    room = Room("You are in the Master Bedroom. "
                "You can to to North Hall by heading East and the guest bedroom is to the south."
                "What direction?"
                , None, 4, 0, None)
    room_list.append(room)
    room = Room("You are in the torch-lit hallway. "
                "You can go all 4 directions."
                "What direction?", 6, 5, 1, 3)
    room_list.append(room)
    room = Room("You are in the kitchen. "
                "You can go West or South."
                "What direction? ", None, None, 2, 4)
    room_list.append(room)
    room = Room("You are on the Balcony."
                " You can only go South."
                "What direction?", None, None, 4, None)
    room_list.append(room)

    current_room = 1
    print(room_list)
    print(room_list[current_room].description)
    done = False


main()

