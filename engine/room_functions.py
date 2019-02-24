def evaluateRoomFunction(function, game_state, room, inventory):
	print(function)
	if room == "outside":
		if function == "lookAround":
			text_output = "You see a large mansion"
			picture_path = "dog.png"
			return game_state, "outside", inventory, text_output, picture_path
		elif function == "readLetter":
			#do stuff
			text_output = "These are the contents of the letter"
			picture_path = "dog.png"
			return game_state, "outside", inventory, text_output, picture_path
		elif function == "enterHouse":
			#do stuff
			text_output = "You are now inside the house. You stand in a large foyer with many people and a large computer in the middle."
			picture_path = "cat.png"
			return game_state, "outside", inventory, text_output, picture_path
	elif room == "foyer":
		#TODO
		pass
	elif room == "dining_room":
		#TODO
		pass			
	elif room == "kitchen":
		#TODO		
		pass		
	elif room == "coat_room":
		#TODO		
		pass		
	elif room == "hallway":
		#TODO
		pass