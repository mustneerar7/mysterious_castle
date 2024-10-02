import os
import json
from game.room import Room
from game.player import Player

class Game:
    """
    A class to represent the game.
    Attributes
    ----------
    rooms : dict
        A dictionary to store the rooms in the game.
    player : Player
        The player object.
    puzzles : dict
        A dictionary to store the puzzles in the game.
    Methods
    -------
    __init__():
        Initializes the game by setting up rooms, player, and puzzles.
    init_game():
        Sets up the initial state of the game, including rooms and their connections.
    save_game():
        Saves the current game state to a file.
    load_game():
        Loads the game state from a file.
    """
    def __init__(self):
        self.rooms = {}
        self.player = None
        self.puzzles = {}
        self.init_game()

    def init_game(self):
        entrance = Room("Entrance", 
                        "You are at the entrance of a mysterious castle.", 
                        {"north": None}, 
                        ["old_key"],
                        examineables={"suit_of_armor": "An old suit of armor. It seems to hide something."})
        
        hall = Room("Grand Hall", 
                    "You are in the grand hall. Dusty portraits surround you.", 
                    {"south": entrance, "east": None, "west": None}, 
                    ["torch"],
                    examineables={"portraits": "Dusty portraits line the walls, their eyes seem to follow you."})
        
        library = Room("Library", 
                    "Books line the walls. A strange book catches your eye.", 
                    {"west": hall}, 
                    ["ancient_tome"],
                    examineables={"strange_book": "A book with a lock. It seems important."})
        
        kitchen = Room("Kitchen", 
                    "The smell of old bread lingers. You see a dusty recipe book.", 
                    {"east": hall, "south": None}, 
                    ["recipe_book"],
                    examineables={"old_bread": "A loaf of bread that looks very stale."})
        
        basement = Room("Basement", 
                        "It's dark and damp. You feel a chill. There is a lantern here.", 
                        {"north": hall}, 
                        ["lantern"], 
                        locked=True, 
                        riddle="What is 5 + 7?",
                        examineables={"dark_corner": "In the corner, you see shadows dancing in the dark."})
        
        tower = Room("Tower", 
                    "The tower is tall and dark. You can see something shiny at the top.", 
                    {"south": hall}, 
                    ["treasure"],
                    examineables={"shiny_object": "A glimmering treasure at the top of the tower."})
        
        secret_passage = Room("Secret Passage", 
                            "A narrow, dark passage. Something glows faintly ahead.", 
                            {"north": tower}, 
                            ["magic_amulet"],
                            examineables={"glow": "A faint glow emanating from an amulet."})

        # Set room exits
        entrance.exits["north"] = hall
        hall.exits["east"] = library
        hall.exits["west"] = kitchen
        hall.exits["south"] = entrance
        library.exits["west"] = hall
        kitchen.exits["east"] = hall
        hall.exits["north"] = basement
        tower.exits["south"] = hall
        secret_passage.exits["north"] = tower

        # Initialize rooms dictionary
        self.rooms = {
            "Entrance": entrance,
            "Grand Hall": hall,
            "Library": library,
            "Kitchen": kitchen,
            "Basement": basement,
            "Tower": tower,
            "Secret Passage": secret_passage
        }

        self.player = Player(self.rooms["Entrance"])
        self.puzzles = {"riddle": "I have cities but no houses. What am I?"}



    def save_game(self):
        # Ensure the 'data' directory exists
        if not os.path.exists('data'):
            os.makedirs('data')

        game_state = {
            "current_room": self.player.current_room.name,
            "inventory": self.player.inventory,
            "solved_riddles": self.player.solved_riddles  # Store solved riddles
        }

        # Save game state to 'data/savegame.txt'
        with open("data/savegame.txt", "w") as file:
            json.dump(game_state, file)
        print("Game saved.")

    def load_game(self):
        if os.path.exists("data/savegame.txt"):
            with open("data/savegame.txt", "r") as file:
                game_state = json.load(file)

                # Restore player's current room
                self.player.current_room = self.rooms[game_state["current_room"]]
                self.player.inventory = game_state["inventory"]
                self.player.solved_riddles = game_state.get("solved_riddles", [])

            print(f"Game loaded. You are in the {self.player.current_room.name}.")
        else:
            print("No saved game found.")

