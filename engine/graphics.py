from tkinter import *
from tkinter import ttk
import tkinter as tki
import tkinter.messagebox as msg
from PIL import ImageTk, Image
import spacy
import engine

e = engine.Engine()
path_to_image = 'cat.png'

def display_func(nlp, nlpactions, actions):
	root = Tk()
	root.title("Crypto Game")

	mainframe = ttk.Frame(root, padding="3 3 12 12")
	mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
	root.columnconfigure(0, weight=1)
	root.rowconfigure(0, weight=1)


	# create a Image widget
	# pathToImage = 'cat.png'
	im = Image.open(path_to_image)
	resized = im.resize((600, 300),Image.ANTIALIAS)
	ph = ImageTk.PhotoImage(resized.convert('RGBA'))

	game_display = tki.Label(mainframe, image = ph)
	game_display.grid(row=0, column=0, sticky='new',padx=2, pady=20)
	game_display.image=ph

	# create a Text widget
	text = tki.Text(mainframe, borderwidth=3, relief="sunken")
	# text = tki.Label(mainframe, background='#a0ffa0')
	text.config(font=("consolas", 12), undo=True, wrap='word', state=DISABLED)
	text.grid(row=1, column=0, sticky='nsew', padx=2, pady=2)

	# create a Scrollbar and associate it with txt
	scrollb = tki.Scrollbar(mainframe, command=text.yview)
	scrollb.grid(row=1, column=1, sticky='nsew')
	text['yscrollcommand'] = scrollb.set

	# create a Entry widget
	def action_event(event): # handler
		####*********************** TO DO *************************************#####
		#### Pass entry into text processor
		usernlp = nlp(user_entry.get())
		similarities = [usernlp.similarity(i) for i in nlpactions]
		print(actions[similarities.index(max(similarities))], max(similarities))
		print(similarities)
		#### Update Textbox
		#### Update Picture

		##Engine Processing
		new_text, new_picture = e.parse(user_entry.get())

		#Make the text-box writeable
		text.config(state=NORMAL)
		text.delete(1.0, END)

		#change picture
		result = new_text + "\n"
		text.insert(INSERT, result)
		action_entry_box.delete(0, END)

		#change image
		global path_to_image
		path_to_image = new_picture

		#Make the text-box read-only
		text.config(state=DISABLED)

	user_entry = tki.StringVar()
	action_entry_box = tki.Entry(mainframe, textvariable=user_entry)
	action_entry_box.grid(row=2, column=0, padx=2, pady=2, sticky='nsew')
	action_entry_box.bind('<Return>', action_event)




	root.mainloop()


def main():
	nlp = spacy.load('en_core_web_lg')
	actions = ['Talk to Jane', 'Talk to Michael', 'Talk to Francis', 'Talk to the Cook',
	'Open Dining Room Door 3', 'Open Foyer Door 2', 'Open Kitchen Door 1', 'Enter Hallway', 'Go Inside']
	nlpactions = [nlp(i) for i in actions]
	display_func(nlp, nlpactions, actions)






if __name__ == '__main__':
	main()
