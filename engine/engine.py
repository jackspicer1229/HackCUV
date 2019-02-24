import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
import room as r

game_state = 0
room = 'outside'
inventory = ["letter"]
picture = "cat.png"


class Engine():
	def __init__(self):
		text = ""
		self.parse(text)

	def parse(self, text):
		# tag text
		# text = word_tokenize(text)
		# tag = nltk.pos_tag(text)
		# tag_dict = {elem[0]: elem[1] for elem in tag}
		# print(tag)
		# tag_cts = Counter(elem[1] for elem in tag) # nltk.help.upenn_tagset()
		# print(tag_cts)
		# pos = [elem[1] for elem in tag]

		# inv_map = {}
		# for k, v in tag_dict.items():
		# 	inv_map[v] = inv_map.get(v, [])
		# 	inv_map[v].append(k)
		# print(inv_map)

		# if text[0] != 'inspect' or text[0] != 'go' or text[0] != 'talk' or text[0] != 'use':
		# 	print("invalid action")
		# else:
		# 	verb = text[0]

		# if 'NN' in inv_map.keys():
		# 	subject = inv_map['NN'][0]
		# elif 'NNP' in inv_map.keys():
		# 	subject = inv_map['NNP'][0]
		user_input = text
		if user_input == "":
			return
		else:
			return self.engine_update(user_input)

	def engine_update(self, user_input):
		global game_state, room, inventory, picture
		current_room = None


		if room == "outside":
			current_room = r.Outside()
		elif room == "foyer":
			current_room = r.Foyer()
		elif room == "dining_room":
			current_room = r.DiningRoom()
		elif room == "kitchen":
			current_room = r.Kitchen()
		elif room == "coat_room":
			current_room = r.CoatRoom()
		elif room == "hallway":
			current_room = r.Hallway()

		current_room.updateState(game_state)
		game_state, room, inventory, action_result, stage_graphics = current_room.evaluate(user_input, game_state, room, inventory, picture)
		return action_result, stage_graphics

		

# e = Engine()
