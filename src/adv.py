from room import Room
from player import Player
from os import system

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

directions = [
    {
        "direction": "n",
        "deadend": "There is no room to the north.",
        "move_to": f".n_to"
    },
    {
        "direction": "s",
        "deadend": "There is no room to the south.",
        "move_to": ".s_to"
    },
    {
        "direction": "e",
        "deadend": "There is no room to the east.",
        "move_to": ".e_to"
    },
    {
        "direction": "w",
        "deadend": "There is no room to the west.",
        "move_to": ".w_to"
    }
]

system("clear")

user = Player(room["outside"])
instructions = "Enter n (North), s (South), e (East), or w (West) to move. Pressing q will quit the game: \n"

while True:
    print(f"\nLocation: {user.current_room.name}\n")
    print(f"{user.current_room.description}\n")

    moveUser = input(instructions)

    # for i in directions:
    #     for k,v in i.items():

    if moveUser == "q":
        print("\nGoodbye, adventurer.\n")
        quit()
    elif moveUser == "n":
        if user.current_room.n_to:
            user.current_room = user.current_room.n_to
        else:
            print("There is no room to the north.")
    elif moveUser == "s":
        if user.current_room.s_to:
            user.current_room = user.current_room.s_to
        else:
            print("There is no room to the south.")
    elif moveUser == "e":
        if user.current_room.e_to:
            user.current_room = user.current_room.e_to
        else:
            print("There is no room to the east.")
    elif moveUser == "w":
        if user.current_room.w_to:
            user.current_room = user.current_room.w_to
        else:
            print("There is no room to the west.")
    else:
        input(instructions)

