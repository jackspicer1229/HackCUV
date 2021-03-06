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
		self.parse(text, None)

	def parse(self, text, nlp):
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
			return self.engine_update(user_input, nlp)

	def engine_update(self, user_input, nlp):
		global game_state, room, inventory, picture
		current_room = None

		# functions[verb][subject]
		# return engine_update(verb, subject)

		if room == "outside":
			current_room = r.Outside()
			song = 'https://www.youtube.com/watch?v=CvYqnmbDCpI&list=PLye9mcKwe2zy3KW8uK_3F7HVMjJjdqSqU&index=13'
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
		temp_room = room
		game_state, room, inventory, action_result, stage_graphics = current_room.evaluate(user_input, game_state, room, inventory, nlp, picture)
		
		scene_change = False
		if(temp_room != room):
			scene_change = True
		return action_result, stage_graphics, scene_change



# e = Engine()
