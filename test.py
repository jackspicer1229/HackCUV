from tkinter import *
from tkinter import ttk
import tkinter as tki
import tkinter.messagebox as msg
from PIL import ImageTk, Image


def display_func():
	root = Tk()
	root.title("Crypto Game")

	mainframe = ttk.Frame(root, padding="3 3 12 12")
	mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
	root.columnconfigure(0, weight=1)
	root.rowconfigure(0, weight=1)


	# create a Image widget
	pathToImage = 'cat.png'
	im = Image.open(pathToImage)
	resized = im.resize((200, 200),Image.ANTIALIAS)
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
		#### Update Textbox
		#### Update Picture

		#Make the text-box writeable
		text.config(state=NORMAL)
		text.delete(1.0, END)


		result = user_entry.get() + "\n"
		text.insert(INSERT, result)
		action_entry_box.delete(0, END)


		#Make the text-box read-only
		text.config(state=DISABLED)

	user_entry = tki.StringVar()
	action_entry_box = tki.Entry(mainframe, textvariable=user_entry)
	action_entry_box.grid(row=2, column=0, padx=2, pady=2, sticky='nsew')
	action_entry_box.bind('<Return>', action_event)



	root.mainloop()


def main():

	display_func()

if __name__ == '__main__':
	main()
