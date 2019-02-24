from tkinter import *
from tkinter import ttk
import tkinter as tki
import tkinter.messagebox as msg
from PIL import ImageTk, Image


def display_func():
	pathToImage = 'cat.png'
	im = Image.open(pathToImage)

	root = Tk()
	root.title("Crypto Game")

	mainframe = ttk.Frame(root, padding="3 3 12 12")
	mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
	root.columnconfigure(0, weight=1)
	root.rowconfigure(0, weight=1)


	# create a Image widget
	# pathToImage = 'cat.png'
	# im = Image.open(pathToImage)
	resized = im.resize((200, 200),Image.ANTIALIAS)
	ph = ImageTk.PhotoImage(resized.convert('RGB'))

	label = tki.Label(image = ph, width=200, height=200)
	label.grid(row=0, column=0, sticky = 'new')
	label.image=ph

	# create a Text widget
	txt = tki.Text(mainframe, borderwidth=3, relief="sunken")
	txt.config(font=("consolas", 12), undo=True, wrap='word')
	txt.grid(row=1, column=0, sticky="sew", padx=2, pady=2)

	# create a Scrollbar and associate it with txt
	scrollb = tki.Scrollbar(mainframe, command=txt.yview)
	scrollb.grid(row=1, column=1, sticky='nsew')
	txt['yscrollcommand'] = scrollb.set

	# create a Entry widget
	def action_event(event=None): # handler
		####*********************** TO DO *************************************#####
		#### Pass entry into text processor
		#### Update Textbox
		#### Update Picture
		action_entry_box.delete(0, END)

	user_entry = tki.StringVar()
	action_entry_box = tki.Entry(mainframe, textvariable=user_entry)
	action_entry_box.grid(row=2, column=0, padx=2, pady=2, sticky='nsew')
	action_entry_box.bind('<Return>', action_event)



	root.mainloop()


def main():

	display_func()

if __name__ == '__main__':
	main()
