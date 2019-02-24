class Object():
    def __init__(self, loc):
        self.loc = loc
        self.actions = ["ask"]

    def inspect(self):
        pass

class Actors(Object):
    def __init__(self):
        self.loc = ""
        self.actions = ["ask"]

    def use(self):
        pass

class Items():
    def __init__(self, loc):
        super().__init__(loc)
        self.actions = ["ask"]

    def inspect(self):
        pass

class npc():
    def __init__(self, loc):
        super().__init__(loc)
        self.actions = ["talk"]

    def inspect(self):
        pass
