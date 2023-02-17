class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():

    room_list = []
    room = Room("Bedroom 2", 3, 1, None, None)
    room_list.append(room)
    room = Room("South Hall", 4, 2, None, 0)
    room_list.append(room)
    room = Room("Dining Room", 5, None, None, 1)
    room_list.append(room)
    room = Room("Bedroom 1", None, 4, 0, None)
    room_list.append(room)
    room = Room("North Hall", 6, 5, 1, 3)
    room_list.append(room)
    room = Room("Kitchen", None, None, 2, 4)
    room_list.append(room)
    room = Room("Balcony", None, None, 4, None)
    room_list.append(room)

    current_room = 1
    print(room_list)
    print(room_list[current_room].description)
    done = False


main()

