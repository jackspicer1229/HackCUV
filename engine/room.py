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
		"enter house go in house open door to house": "enterHouse",
		"start": "start"
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
			return game_state, room, inventory, "I don't understand that command", picture


class Foyer():
	def __init__(self):
		self.valid_actions = {
		"continue": "continue"
		}
	def updateState(self, game_state):
		if(game_state>=1):
			self.valid_actions["look around search near observe"] = "lookAround"
			self.valid_actions["talk to Timmy talk with Timmy ask Timmy say Timmy"] = "talk_timmy_1"
			self.valid_actions["talk to Lisa talk with Lisa ask Lisa say Lisa"] = "talk_lisa_1"
			self.valid_actions["eat cookie"] = "eatCookie"
			self.valid_actions["pick up cookie grab cookie add cookie"] = "grabCookie"

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
			return game_state, room, inventory, "I don't understand that command", picture

class DiningRoom():
	def __init__(self):
		self.valid_actions = {
		"move to kitchen walk to kitchen go back to kitchen leave dining room": "move_to_kitchen",
		"move to hallway walk to hallway go back to hallway leave dining room": "move_to_hallway",
		"talk to Reed talk with Reed ask Reed say Reed": "talk_adam_0",
		"talk to Adam talk with Adam ask Adam say Adam": "talk_reed_0",
		"talk to Tod talk with Tod ask Tod say Tod": "talk_tod_1"
		}
	def updateState(self, game_state):
		if(game_state==2):
			self.valid_actions["talk to Adam talk with Adam ask Adam say Adam"] = "talk_adam_1"
		if(game_state==3):
			self.valid_actions["talk to Reed talk with Reed ask Reed say Reed"] = "talk_reed_1"
		if(game_state==4):
			self.valid_actions["talk to Reed talk with Reed ask Reed say Reed"] = "talk_reed_2"
		if(game_state==5):
			self.valid_actions["talk to Tod talk with Tod ask Tod say Tod"] = "talk_tod_2"
		if(game_state==6):
			self.valid_actions["talk to Adam talk with Adam ask Adam say Adam"] = "talk_adam_2"
		if(game_state==7):
			self.valid_actions["talk to Tod talk with Tod ask Tod say Tod"] = "talk_tod_3"
			self.valid_actions["move to coat room walk to coat room go back to coat room leave dining room"] = "move_to_coat_room"


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
			return game_state, room, inventory, "I don't understand that command", picture

class Kitchen():
	def __init__(self):
		self.valid_actions = {
			"talk to Chef talk with Chef ask Chef say Chef": "talk_to_chef",
			"open fridge look in fridge use fridge": "open_fridge",
			"look around search near observe": "lookAround",
			"move to dining room walk to dining room go back to dining room leave kitchen": "move_to_dining_room",
			"grab chips on counter take chips ": "check_counter"
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
			return game_state, room, inventory, "I don't understand that command", picture

class CoatRoom():
	def __init__(self, things):
		super().__init__(things)

class Hallway():
	def __init__(self, things):
		super().__init__(things)
