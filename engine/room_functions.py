def evaluateRoomFunction(function, game_state, room, inventory):
	print(function)
	if room == "outside":
		if function == "lookAround":
			text_output = "In front of you stands the doors to the mansion. Not much else is out here."
			picture_path = "assets/entrance.png"
			return game_state, "outside", inventory, text_output, picture_path
		elif function == "readLetter":
			text_output = "The letter reads - \n 'Dear Special guest, \n You're invited! To a very special reveal of Trojan Tech's latest and greatest invention! We call it 'The Creeper'. This device will be revealed on the night of November 18th, at the house of Trojan Tech's CEO: Professor Anna Kournikova. Distiguished guests from around the world will be present at this reveal. Please join us on this monumentous occasion.'"
			picture_path = "assets/dog.png"
			return game_state, "outside", inventory, text_output, picture_path
		elif function == "enterHouse":
			text_output = "You push open the massive doors and find yourself in a large foyer. The room is filled with many people you don't recognize. In the center of the room is a large computer screen mounted on a pedestal. After you enter, the screen turns on: \n\n Welcome guests to the reveal of The Creeper! (type continue)"
			picture_path = "assets/foyer.png"
			return game_state, "foyer", inventory, text_output, picture_path
		# elif function == "start":
		# 	text_output = "You stand outside a large, exquisite mansion. In your hand is a gilded red letter. Two towering doors to the mansion stand before you"
		# 	picture_path = "assets/entrance.png"
		# 	return game_state, "outside", inventory, text_output, picture_path
	elif room == "foyer":
		if function == "lookAround":
			text_output = "The Creeper has locked all the doors except for the north one, leading to the dining room. There are two people in the room, Timmy and Lisa. There is a plate of cookies on the table."
			picture_path = "assets/foyer2.png"
			return game_state, "foyer", inventory, text_output, picture_path
		elif function == "continue":
			text_output = "Suddenly, the locks to the door behind you latch shut! The AI has trapped you inside the mansion! A shadowy figure appears on the screen and chuckles. \n\n 'Now that I have all the industry professionals in cybersecurity trapped in my mansion, I can execute my master plan. You see, The Creeper is actual a sophisticated rogue AI I have developed to take over the world. Unless you can escape my mansion, it will wreak havoc on every network in the entire world! Muahahahah' \n\n The screen disappears into thin air, and people scurry from the room. You are left standing in the foyer alone with two other people."
			picture_path = "assets/foyer2.png"
			return game_state+1, "foyer", inventory, text_output, picture_path
		elif function == "talk_timmy_1":
			text_output = "FILLER"
			picture_path = "assets/blondpixel.png"
			return game_state, "foyer", inventory, text_output, picture_path
		elif function == "talk_lisa_1":
			text_output = "FILLER"
			picture_path = "assets/grandmapixel.png"
			return game_state, "foyer", inventory, text_output, picture_path
		elif function == "eatCookie":
			text_output = "You eat the cookie. Yum!"
			picture_path = "assets/cookiepixel.png"
			return game_state, "foyer", inventory, text_output, picture_path
		elif function == "grabCookie":
			text_output = "You add the cookie to your inventory"
			picture_path = "assets/cookiepixel.png"
			if("cookie" not in inventory):
				inventory.append("cookie")
			return game_state, "foyer", inventory, text_output, picture_path
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