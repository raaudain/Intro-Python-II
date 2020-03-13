# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, name, current_room: Room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
    
    def move(self, direction):
        # From docs: getattr(x, 'foobar') is equivalent to x.foobar
        if getattr(self.current_room, f"{direction}_to") is not None:
            self.current_room = getattr(self.current_room, f"{direction}_to")
        else:
            print("You cannot go in that direction.")

    def item_inventory(self):
        if len(self.inventory) == 0:
            print("You have no items.")
        else:
            print("Your inventory")
            for i in self.inventory:
                print(i.name)
    def add_item(self, item):
        self.inventory.append(item)


    def drop_item(self, item):
        self.inventory.remove(item)