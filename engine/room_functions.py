def evaluateRoomFunction(function, game_state, room, inventory):
	print("in evaluateRoomFunction")
	print(function, game_state, room, inventory)
	if room == "outside":
		if function == "lookAround":
			text_output = "You see a large mansion"
			picture_path = "dog.png"
			return game_state, "outside", inventory, text_output, picture_path
		elif function == "readLetter":
			#do stuff
			pass
		elif function == "enterHouse":
			#do stuff
			pass
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