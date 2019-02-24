class Room():
    def __init__(self, things):
        self.things = things
        self.functions = []

    def getActions(self):
        pass

class DiningRoom(Room):
    def __init__(self, things):
        super().__init__(things)
