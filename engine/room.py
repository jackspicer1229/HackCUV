from room_functions import evaluateRoomFunction

# class Room():
# 	def __init__(self, things):
# 		self.things = things
# 		self.functions = []

# 	def getActions(self):
# 		for t in self.things:
# 			self.functions[v] = self.functions.get(v, [])
# 			self.functions[v].append(k)

class Outside():
	def __init__(self):
		self.valid_actions = {
		"look around search near observe": "lookAround",
		"open letter read letter look at letter": "readLetter",
		"enter house go in house open door to house": "enterHouse"
		}
	def updateState(self, game_state):
		return 1

	def evaluate(self, user_input, game_state, room, inventory, nlp, picture):
		#user_score = nlp(user_input)
		#for key in valid_actions.keys():
		#	highest score = compare(user_score with nlp(key))
		#evaluateRoomFunction()
		actions = [*self.valid_actions.keys()]
		nlpactions = [nlp(i) for i in actions]

		usernlp = nlp(user_input)
		similarities = [usernlp.similarity(i) for i in nlpactions]
		best_action = actions[similarities.index(max(similarities))]	

		if(max(similarities) > 0.7):
			return evaluateRoomFunction(self.valid_actions[best_action], game_state, room, inventory)
		else:
			return game_state, room, inventory, "not a valid action", picture


class Foyer():
	def __init__(self, things):
		super().__init__(things)

class DiningRoom():
	def __init__(self, things):
		super().__init__(things)

class Kitchen():
	def __init__(self, things):
		super().__init__(things)

class CoatRoom():
	def __init__(self, things):
		super().__init__(things)

class Hallway():
	def __init__(self, things):
		super().__init__(things)
