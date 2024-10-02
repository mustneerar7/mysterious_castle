from game.game import Game

def start_game():
    """
    Starts the game loop for The Mysterious Castle Adventure.
    This function initializes the game and continuously prompts the player for commands.
    The player can perform various actions such as moving, taking items, dropping items,
    checking inventory, looking around, examining objects, saving the game, and loading
    the game. The loop continues until the player decides to quit.
    Commands:
        - "quit": Exit the game.
        - "go <direction>": Move the player in the specified direction.
        - "take <item>": Take the specified item.
        - "drop <item>": Drop the specified item.
        - "inventory": Display the player's current inventory.
        - "look": Display details of the current room.
        - "examine <object>": Examine the specified object.
        - "save": Save the current game state.
        - "load": Load a previously saved game state.
    Note:
        Commands that require a second parameter (e.g., direction, item, object) must be
        followed by the appropriate parameter. If the parameter is missing, an error message
        will be displayed.
    """
    game = Game()
    print("Welcome to The Mysterious Castle Adventure!")
    
    while True:
        command = input("What would you like to do? ").lower().strip()
        if command == "quit":
            print("Thanks for playing!")
            break
        
        # Handle commands that require a second parameter
        elif command.startswith("go"):
            parts = command.split()
            if len(parts) < 2:
                print("You need to specify a direction to go (e.g., 'go north').")
            else:
                direction = parts[1]
                game.player.move(direction)

        elif command.startswith("take"):
            parts = command.split()
            if len(parts) < 2:
                print("You need to specify an item to take (e.g., 'take torch').")
            else:
                item = parts[1].replace(" ", "_")
                game.player.take_item(item)

        elif command.startswith("drop"):
            parts = command.split()
            if len(parts) < 2:
                print("You need to specify an item to drop (e.g., 'drop old_key').")
            else:
                item = parts[1].replace(" ", "_")
                game.player.drop_item(item)

        elif command == "inventory":
            print(f"Inventory: {', '.join(game.player.inventory).replace('_', ' ')}")

        elif command == "look":
            print(game.player.current_room.get_details())

        elif command.startswith("examine"):
            parts = command.split()
            if len(parts) < 2:
                print("You need to specify an object to examine (e.g., 'examine suit_of_armor').")
            else:
                object_name = parts[1].replace(" ", "_")
                game.player.examine(object_name)

        elif command == "save":
            game.save_game()

        elif command == "load":
            game.load_game()
        
        else:
            print("Invalid command.")
