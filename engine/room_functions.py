def evaluateRoomFunction(function, game_state, room, inventory):
	print(function)
	if room == "outside":
		if function == "lookAround":
			text_output = "In front of you stands the doors to the mansion. Not much else is out here."
			picture_path = "assets/entrance.png"
			return game_state, "outside", inventory, text_output, picture_path
		elif function == "readLetter":
			text_output = "The letter reads - \n 'Dear Special guest, \n You're invited! To a very special reveal of Trojan Tech's latest and greatest invention! We call it 'The Creeper'. This device will be revealed on the night of November 18th, at the house of Trojan Tech's CEO: Professor Anna Kournikova. Distiguished guests from around the world will be present at this reveal. Please join us on this monumentous occasion.'"
			picture_path = "assets/envelopepixel.png"
			return game_state, "outside", inventory, text_output, picture_path
		elif function == "enterHouse":
			text_output = "You push open the massive doors and find yourself in a grand entrance hall. The room is filled with many people you don't recognize. In the center of the room is a large computer screen mounted on a pedestal. After you enter, the screen turns on: \n\n Welcome guests to the reveal of The Creeper! (type continue)"
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
			text_output = "Suddenly, the locks to the door behind you latch shut! The AI has trapped you inside the mansion! A shadowy figure appears on the screen and chuckles. \n\n 'Now that I have all the industry professionals in cybersecurity trapped in my mansion, I can execute my master plan. You see, The Creeper is actual a sophisticated rogue AI I have developed to take over the world. Unless you can escape my mansion, it will wreak havoc on every network in the entire world! Muahahahah' \n\n The screen disappears into thin air, and people scurry from the room. You are left standing in the grand entrance hall alone with two other people."
			picture_path = "assets/foyer2.png"
			return game_state+1, "foyer", inventory, text_output, picture_path
		elif function == "talk_timmy_1":
			text_output = "Teeeheeehee im a little boy"
			picture_path = "assets/blondpixel.png"
			return game_state, "foyer", inventory, text_output, picture_path
		elif function == "talk_lisa_1":
			text_output = "I used to know a lot about cryptography... I think the door in the dining room has a puzzle on it. You should check it out"
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
		elif function == "move_to_dining_room":
			text_output = "You look walk through the door into the dining room. Maybe you should look around"
			picture_path = "assets/DiningRoom.png"
			return game_state, "dining_room", inventory, text_output, picture_path
	elif room == "dining_room":
		if function == "talk_adam_0":
			text_output = "Go check out the puzzle door in the hallway"
			picture_path = "assets/butlerpixel.png"
			return game_state, "dining_room", inventory, text_output, picture_path
		elif function == "lookAround":
			text_output = "In front of you is a hallway leading to a door. There are three people in the room, Tod, Reed, and Adam. Their is a door leading to the kitchen to your right and Tod is blocking the door to the coat room on your left. Behind is the door back to the grand hall"
			picture_path = "assets/DiningRoom.png"
			return game_state, "dining_room", inventory, text_output, picture_path
		elif function == "talk_reed_0":
			text_output = "Go check out the puzzle door in the hallway"
			picture_path = "assets/compscistudent.png"
			return game_state, "dining_room", inventory, text_output, picture_path
		elif function == "talk_adam_1_a":
			text_output = "Ah it looks like my lord has left us with a puzzle. You know he mentioned something about Caeser. Maybe ask around"
			picture_path = "assets/butlerpixel.png"
			return game_state+1, "dining_room", inventory, text_output, picture_path
		elif function == "talk_adam_1_b":
			text_output = "Ah it looks like my lord has left us with a puzzle. You know he mentioned something about Caeser. Maybe ask around"
			picture_path = "assets/butlerpixel.png"
			return game_state, "dining_room", inventory, text_output, picture_path
		elif function == "talk_reed_1":
			text_output = "What do you want? Caeser? Like a Caeser cypher? Yeah I know that but I can think about that right now. Man if I had my favorite thinking foods I may be able to help"
			picture_path = "assets/compscistudent.png"
			return game_state+1, "dining_room", inventory, text_output, picture_path
		elif function == "talk_tod_1":
			text_output = "This is crazy!! What do we do?"
			picture_path = "assets/coatcheckin.png"
			return game_state, "dining_room", inventory, text_output, picture_path
		elif function == "talk_reed_2_a":
			if("cookie" in inventory and "redbull" in inventory and "chips" in inventory):
				text_output = "Oh you brought me my food. Thanks. Glug glug glug glug glug. Munch munch munch. Ah okay I guess i'll tell you about Caeser Cyphers huh? Basically, imagine you have 2 lines of alphabet. ABCD... on both the top and bottom. And then you shift the bottom alphabet by some amount. Now A may be corresponding with D, B with E, and so on and so forth. The trick is to know how much it's shifted by. Look around. Now that I think about it, I saw the CEO near the coat rack earlier.\n (to read more about a caeser cipher, go to http://practicalcryptography.com/ciphers/caesar-cipher/)"
				picture_path = "assets/compscistudent.png"
				return game_state+1, "dining_room", inventory, text_output, picture_path
			else:
				text_output = "Man I am hungry"
				picture_path = "assets/compscistudent.png"
				return game_state, "dining_room", inventory, text_output, picture_path
		elif function == "talk_reed_2_b":
			if("cookie" in inventory and "redbull" in inventory and "chips" in inventory):
				text_output = "Oh you brought me my food. Thanks. Glug glug glug glug glug. Munch munch munch. Ah okay I guess i'll tell you about Caeser Cyphers huh? Basically, imagine you have 2 lines of alphabet. ABCD... on both the top and bottom. And then you shift the bottom alphabet by some amount. Now A may be corresponding with D, B with E, and so on and so forth. The trick is to know how much it's shifted by. Look around. Now that I think about it, I saw the CEO near the coat rack earlier.\n (to read more about a caeser cipher, go to http://practicalcryptography.com/ciphers/caesar-cipher/)"
				picture_path = "assets/compscistudent.png"
				return game_state, "dining_room", inventory, text_output, picture_path
			else:
				text_output = "Man I am hungry"
				picture_path = "assets/compscistudent.png"
				return game_state, "dining_room", inventory, text_output, picture_path
		elif function == "talk_tod_2_a":
			text_output = "Let you into the coatroom? I don't know. What if you steal someone. If you bring someone above me, then i'm totally fine to letting you in"
			picture_path = "assets/coatcheckin.png"
			return game_state+1, "dining_room", inventory, text_output, picture_path
		elif function == "talk_tod_2_b":
			text_output = "Let you into the coatroom? I don't know. What if you steal someone. If you bring someone above me, then i'm totally fine to letting you in"
			picture_path = "assets/coatcheckin.png"
			return game_state, "dining_room", inventory, text_output, picture_path
		elif function == "talk_adam_2_a":
			text_output = "What is it? Oh you need to get into the coat room. Sure I can talk to Tod for you"
			picture_path = "assets/butlerpixel.png"
			return game_state+1, "dining_room", inventory, text_output, picture_path
		elif function == "talk_adam_2_b":
			text_output = "What is it? Oh you need to get into the coat room. Sure I can talk to Tod for you"
			picture_path = "assets/butlerpixel.png"
			return game_state, "dining_room", inventory, text_output, picture_path
		elif function == "talk_tod_3":
			text_output ="Adam says you are good to go. Go in."
			picture_path = "assets/coatrack.png"
			return game_state, "dining_room", inventory, text_output, picture_path
		elif function == "move_to_kitchen":
			text_output = "you move into the kitchen"
			picture_path = "assets/kitchen.png"
			return game_state, "kitchen", inventory, text_output, picture_path
		elif function == "move_to_hallway_0":
			text_output ="you move into the hallway"
			picture_path = "assets/cipher.png"
			return game_state+1, "hallway", inventory, text_output, picture_path
		elif function == "move_to_hallway_1":
			text_output ="you move into the hallway"
			picture_path = "assets/cipher.png"
			return game_state, "hallway", inventory, text_output, picture_path
		elif function == "move_to_coat_room":
			text_output = "you move into the coat room"
			picture_path = "assets/coatroom.png"
			return game_state, "coat_room", inventory, text_output, picture_path
		elif function == "move_to_foyer":
			text_output = "you move into the foyer"
			picture_path = "assets/foyer2.png"
			return game_state, "foyer", inventory, text_output, picture_path
	elif room == "kitchen":
		if function == "talk_to_chef":
			text_output = "Ah the master has gone insane. Oh, ensomnia cookies? We left those out during the event."
			picture_path = "assets/chefpixel.png"
			return game_state, "kitchen", inventory, text_output, picture_path
		elif function =="lookAround":
			text_output = "you see a chef in the corner, a fridge, and some chips on the counter. The only door leads back to the dining room"
			picture_path = "assets/kitchen.png"
			return game_state, "kitchen", inventory, text_output, picture_path
		elif function == "open_fridge":
			text_output = "you found redbull!"
			picture_path = "assets/redbullpixel.png"
			if ("redbull" not in inventory):
				inventory.append("redbull")
			return game_state, "kitchen", inventory, text_output, picture_path
		elif function == "check_counter":
			text_output = "you found chips!"
			picture_path = "assets/chipspixel.png"
			if ("chips" not in inventory):
				inventory.append("chips")
			return game_state, "kitchen", inventory, text_output, picture_path
		elif function == "move_to_dining_room":
			text_output = "you move into the dining room"
			picture_path = "assets/DiningRoom.png"
			return game_state, "dining_room", inventory, text_output, picture_path 
		#TODO		
		pass		
	elif room == "coat_room":
		if function == "inspect_coats":
			text_output = "how interesting. Each of the coats are labels with a number. There are 26 coats. However, instead of going from 1 to 26, numbers 21-26 are first and 1 through 20 come next. What come it mean?"
			picture_path = "coatrack.png"
			return game_state, "coat_room", inventory, text_output, picture_path
		elif function == "move_to_dining_room":
			text_output = "you move into the dining room"
			picture_path = "assets/DiningRoom.png"
			return game_state, "dining_room", inventory, text_output, picture_path
		elif function == "lookAround":
			text_output = "There are 26 numbered coat racks in a strange order. Perhaps you should take a closer look."
			picture_path = "assets/coatroom.png"
			return game_state, "dining_room", inventory, text_output, picture_path
	elif room == "hallway":
		if function == "entered_code":
			text_output = "You did it. The first door clicks open. Onward, let's defeat the Creeper"
			picture_path = "assets/correctpassword.png"
			return game_state, "hallway", inventory, text_output, picture_path	
		elif function == "lookAround":
			text_output = "In front of you is a door with a series of letters and blanks below them. It seems you need to enter the password to continue. (hint: once you find the password, just enter it as a command)"
			picture_path = "assets/cipher.png"
			return game_state, "hallway", inventory, text_output, picture_path
		elif function == "move_to_dining_room":
			text_output = "you move into the dining room"
			picture_path = "assets/DiningRoom.png"
			return game_state, "dining_room", inventory, text_output, picture_path	
	