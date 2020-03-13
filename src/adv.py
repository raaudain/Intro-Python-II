from room import Room
from player import Player
from item import Item
from os import system
import random


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer",
    """Dim light filters in from the south. Dusty
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


items = {
    "shoe": Item("Shoe", "Old, smelly shoe. It's foul stench can kill the Undead."),
    "torch": Item("Torch", "A torch to light the way."),
    "key": Item("Key", "An old key.")
}

# Randomly place items in random rooms
for i in range(0, 4):
    # List method converts sequence types to lists
    random_room = random.choice(list(room.keys()))
    random_item = random.choice(list(items.keys()))
    room[random_room].add_item(random_item) 


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


system("clear")

player_name = input("Enter player's name: ")
user = Player(player_name, room["outside"])


def take(x):
    if x in user.current_room.items:
        # Take item from room
        user.current_room.drop_item(x)
        # User adds item to inventory
        user.add_item(x)
        items[x].on_take()
    else:
        print(f"Nothing here.")

def drop(x):
    if x in user.current_room.items:
        # Leave item in room
        user.current_room.add_item(x)
        # Item is removed from user's inventory
        user.drop_item(x)
        items[x].on_drop()
        # print(f"")


instructions = "Enter n (North), s (South), e (East), or w (West) to move. Pressing q will quit the game: \n"

while True:
    print(f"\nLocation: {user.current_room.name}\n")
    print(f"{user.current_room.description}\n")

    moveUser = input(instructions).lower()

    if moveUser == "q":
        print(f"\nGoodbye, {player_name}.\n")
        exit(0)
    elif moveUser in ("n", "s", "e", "w"):
        user.move(moveUser)
        # If the user's inventory is greater than zero,
        # print the inventory
        if len(user.current_room.items) > 0:
            print(f"Inventory: {user.inventory}")
            for items in user.current_room.items:
                print(f"New: {random_item}")
    # Take
    elif moveUser.split(" ") in ("take", "t"):
        if len(user.current_room.items) > 0:
            take(random_item)
        else:
            print("No item to take.")
    # Drop
    elif moveUser.split()[0] in ("drop", "d"):
        if len(user.inventory) > 0:
            drop(random_item)
            print(f"You dropped the this item: {random_item}")
        else:
            print("You have no items to drop.")
    # Inventory
    elif moveUser.split() in ("inventory", "i"):
        if len(user.inventory) > 0:
            print(f"{user.inventory}")
        else:
            print("You have not items in your inventory.")
    else:
        input(instructions).lower()

