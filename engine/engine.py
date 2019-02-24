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
		# functions = {
		#     'inspect': {
		#         'Sam': Sam.inspect()
		#     },
		#     'inspect': {
		#         'Sam': Sam.inspect()
		#     },
		#     'inspect': {
		#         'Sam': Sam.inspect()
		#     }
		# }

		# if verb in functions.keys() and subject in functions[verb].keys():
		#     print("valid action")

		# functions[verb][subject]

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

		current_room.update(game_state)
		gameState, room, inventory, action_result, stage_graphics = current_room.evaluate()
		return action_result, stage_graphics

		# if subject not in self.curRoom.objects:
		#     print("invalid action")

		# check validity
		# if pos.index('VB') < pos.index('NN') or pos.index('VBP') < pos.index('NN') or pos.index('VB') < pos.index('NNP') or pos.index('VBP') < pos.index('NNP'):
		#     print("poo")

		# if tag_cts['VB'] || tag_cts['VBP']: # number of verbs
		#     pass
		# if tag_cts['TO']: # did something TO something else
		#     pass
		# if tag_cts['NN']: # normal item
		#     pass
		# if tag_cts['NNP']: # interact with person
		#     pass

# def printss(txt):
#     print(txt)
#
# gang = {"poo": printss("hallO")}
# gang["poo"]


#CC: conjunction, coordinating
#     & 'n and both but either et for less minus neither nor or plus so
#     therefore times v. versus vs. whether yet
# CD: numeral, cardinal
#     mid-1890 nine-thirty forty-two one-tenth ten million 0.5 one forty-
#     seven 1987 twenty '79 zero two 78-degrees eighty-four IX '60s .025
#     fifteen 271,124 dozen quintillion DM2,000 ...
# DT: determiner
#     all an another any both del each either every half la many much nary
#     neither no some such that the them these this those

# IN: preposition or conjunction, subordinating
#     astride among uppon whether out inside pro despite on by throughout
#     below within for towards near behind atop around if like until below
#     next into if beside ...
# PDT: pre-determiner
#     all both half many quite such sure this
# POS: genitive marker
#     ' 's
# PRP: pronoun, personal
#     hers herself him himself hisself it itself me myself one oneself ours
#     ourselves ownself self she thee theirs them themselves they thou thy us
# PRP$: pronoun, possessive
#     her his mine my our ours their thy your

# RP: particle
#     aboard about across along apart around aside at away back before behind
#     by crop down ever fast for forth from go high i.e. in into just later
#     low more off on open out over per pie raising start teeth that through
#     under unto up up-pp upon whole with you

# TO: "to" as preposition or infinitive marker
#     to

# NN noun, singular ‘desk’
# NNS noun plural ‘desks’
# NNP proper noun, singular ‘Harrison’
# NNPS proper noun, plural ‘Americans’

e = Engine()
