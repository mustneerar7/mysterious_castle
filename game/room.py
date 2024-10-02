class Room:
    """
    Class representing a room in the game.
    Attributes:
        name (str): The name of the room.
        description (str): A description of the room.
        exits (dict): A dictionary of exits from the room, where keys are directions and values are the rooms they lead to.
        items (list, optional): A list of items present in the room. Defaults to an empty list.
        locked (bool, optional): Indicates if the room is locked. Defaults to False.
        riddle (str, optional): A riddle associated with the room. Defaults to None.
        examineables (dict, optional): A dictionary of examineable objects in the room, where keys are object names and values are their descriptions. Defaults to an empty dictionary.
    Methods:
        get_details():
            Returns a string containing the room's description, available exits, and examineable objects.
    """
    def __init__(
            self, name, description, 
            exits, items=None, locked=False, 
            riddle=None, examineables=None):
        self.name = name
        self.description = description
        self.exits = exits
        self.items = items if items else []
        self.locked = locked
        self.riddle = riddle
        self.examineables = examineables if examineables else {}

    def get_details(self):
        items_list = ", ".join(self.items) if self.items else "None"
        return f"{self.description}\nExits: {', '.join(self.exits.keys())}\nExaminables: {', '.join(self.examineables.keys()) if self.examineables else 'None'}"
