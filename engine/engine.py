import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

game_state = 0
room = 'outside'
inventory = ["letter"]


class Engine():
	def __init__(self):
		text = "go to the pantry Jim"
		self.parse(text)

	def parse(self, text):
		# tag text
		text = word_tokenize(text)
		tag = nltk.pos_tag(text)
		tag_dict = {elem[0]: elem[1] for elem in tag}
		print(tag)
		tag_cts = Counter(elem[1] for elem in tag) # nltk.help.upenn_tagset()
		print(tag_cts)
		pos = [elem[1] for elem in tag]

		inv_map = {}
		for k, v in tag_dict.items():
			inv_map[v] = inv_map.get(v, [])
			inv_map[v].append(k)
		print(inv_map)

		if text[0] != 'inspect' or text[0] != 'go' or text[0] != 'talk' or text[0] != 'use':
			print("invalid action")
		else:
			verb = text[0]

		if 'NN' in inv_map.keys():
			subject = inv_map['NN'][0]
		elif 'NNP' in inv_map.keys():
			subject = inv_map['NNP'][0]

		return engine_update(verb, subject)

	def engine_update(verb, subject):
		if room == "outside":
			current_room = Outside()
		else if room == "foyer":
			current_room = Foyer()
		else if room == "dining_room":
			current_room = DiningRoom()
		else if room == "kitchen":
			current_room = Kitchen()
		else if room == "coat_room":
			current_room = CoatRoom()
		else if room == "hallway":
			current_room = Hallway()

		current_room.updateState(game_state)
		game_state, room, inventory, action_result, stage_graphics = current_room.evaluate(game_state, current_room, inventory)
		return action_result, stage_graphics

		

e = Engine()
