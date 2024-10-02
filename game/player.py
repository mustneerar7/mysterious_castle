class Player:

    """
    Represents a player in the game.
    Attributes:
        current_room (Room): The room where the player is currently located.
        inventory (list): A list of items the player is carrying.
        solved_riddles (list): A list of riddles that the player has solved.
    Methods:
        __init__(current_room):
            Initializes the player with the current room and empty inventory and solved riddles list.
        move(direction):
            Moves the player to a different room based on the given direction.
            Handles restrictions for entering certain rooms.
        drop_item(item):
            Drops an item from the player's inventory into the current room.
        examine(object_name):
            Examines an object in the current room and reveals collectible items.
    """

    def __init__(self, current_room):
        self.current_room = current_room
        self.inventory = []
        self.solved_riddles = []


    def take_item(self, item):
        # Check for item with underscore
        if item in self.current_room.items:
            self.inventory.append(item)
            self.current_room.items.remove(item)
            print(f"You took the {item.replace('_', ' ')}.")  # Display in human-readable format
        else:
            print(f"There is no {item.replace('_', ' ')} here.")

    def move(self, direction):
        if direction in self.current_room.exits:
            next_room = self.current_room.exits[direction]

            # Restriction for entering the Library (requires old_key)
            if next_room.name == "Library" and "old_key" not in self.inventory:
                print("The door to the library is locked. You need the old key to enter.")
                return

            # Restriction for entering the Basement (riddle-locked)
            if next_room.name == "Basement" and "math problem solved" not in self.solved_riddles:
                print("The door to the basement is locked. Solve this riddle to enter:")
                riddle_answer = input("What is 5 + 7? = ")
                if riddle_answer == "12":
                    print("Correct! You can now enter the basement.")
                    self.solved_riddles.append("math problem solved")
                else:
                    print("Incorrect answer. You cannot enter the basement.")
                    return

            self.current_room = next_room
            print(self.current_room.description)
        else:
            print("You can't go that way.")

    def drop_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            self.current_room.items.append(item)
            print(f"You dropped the {item.replace('_', ' ')}.")
        else:
            print(f"You don't have a {item.replace('_', ' ')}.")

    def examine(self, object_name):
        if object_name in self.current_room.examineables:
            print(self.current_room.examineables[object_name])  

            items_list = ", ".join(self.current_room.items) if self.current_room.items else "None"
            print(f"You notice the following items: {items_list.replace('_', ' ')}")
        else:
            print(f"There is no {object_name.replace('_', ' ')} to examine.")
