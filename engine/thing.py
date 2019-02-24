class Object():
    def __init__(self, loc):
        self.loc = loc

    def inspect(self):
        pass



class Item():
    def __init__(self, loc):
        super().__init__(loc)
        self.actions = ["ask"]

    def inspect(self):
        pass

class NPC():
    def __init__(self, loc, name, dialogue):
        super().__init__(loc)
        self.actions = ["talk"]

    def talk(game_state):
        return dialogue[game_state]

    def inspect(self):
        pass
