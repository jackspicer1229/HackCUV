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

# Adam Ceo (Butler)
#
# Chef Dubois
#
# Timmy (Kid next door)
#
# Sam (comp sci nerd)
#
# Lisa (old woman)
#
# Todd (coat check)

# Credits
# Music from OpenSourceMusic.com by Penn Pierson Creative Commons
