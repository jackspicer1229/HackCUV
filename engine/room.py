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
		"look around": "lookAround", 
		"open letter": "readLetter", 
		"read letter": "readLetter",
		"open door": "enterHouse",
		"enter house": "enterHouse"
		}
	def updateState(self, game_state):
		print("we good")
		return 1

	def evaluate(self, user_input, game_state, room, inventory):
		if(user_input in self.valid_actions.keys()):
			print("we good")
			return evaluateRoomFunction(self.valid_actions[user_input], game_state, room, inventory)
		else:
			return 1,1,1,1,1



		
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