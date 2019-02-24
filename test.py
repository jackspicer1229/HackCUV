from tkinter import *
from tkinter import ttk
import tkinter as tki
# import tkinter as tki
# from PIL import ImageTk, Image

def calculate(*args):
	try:
		value = float(feet.get())
		meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
	except ValueError:
		pass

def test_func():
	root = Tk()
	root.title("Feet to Meters")

	mainframe = ttk.Frame(root, padding="3 3 12 12")
	mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
	root.columnconfigure(0, weight=1)
	root.rowconfigure(0, weight=1)

	feet = StringVar()
	meters = StringVar()

	feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
	feet_entry.grid(column=2, row=1, sticky=(W, E))

	ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
	ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

	ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
	ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
	ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)


	for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

	feet_entry.focus()
	root.bind('<Return>', calculate)

	root.mainloop()

def display_func():
	root = Tk()
	root.title("Crypto Game")

	mainframe = ttk.Frame(root, padding="3 3 12 12")
	mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
	root.columnconfigure(0, weight=1)
	root.rowconfigure(0, weight=1)

	# create a IMAGE widget ??????

	# create a Text widget
	txt = ttk.Text(txt_frm, borderwidth=3, relief="sunken")
	txt.config(font=("consolas", 12), undo=True, wrap='word')
	txt.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)

	# create a Scrollbar and associate it with txt
	scrollb = ttk.Scrollbar(txt_frm, command=self.txt.yview)
	scrollb.grid(row=1, column=1, sticky='nsew')
	txt['yscrollcommand'] = scrollb.set

	root.mainloop()


def main():
	# test_func()

	# root = Tk()
	# root.title("The Prophecy")

	# mainframe = ttk.Frame(root, padding="3 3 12 12")

	# root.columnconfigure(0, weight=1)
	# root.rowconfigure(0, weight=1)	

	# root.mainloop()

	# class App(object):

	# 	def __init__(self):
	# 		self.root = tki.Tk()

	# 	# create a Frame for the Text and Scrollbar
	# 		txt_frm = tki.Frame(self.root, width=500, height=700)
	# 		txt_frm.pack(fill="both", expand=True)
	# 		# ensure a consistent GUI size
	# 		txt_frm.grid_propagate(False)
	# 		# implement stretchability
	# 		txt_frm.grid_rowconfigure(0, weight=1)
	# 		txt_frm.grid_columnconfigure(0, weight=1)


	# 	# create an Image widget
	# 		img = ImageTk.PhotoImage(Image.open("cat.jpeg"))
	# 		self.canvas = tki.Canvas(txt_frm, width = 300, height = 300)
	# 		self.canvas.grid(row=0, column=0, padx=2, pady=2)
	# 		self.canvas.create_image(20, 20, image=img) 

	# 		# self.label = tki.Label(txt_frm, image=img)
	# 		# self.label.grid(row=0, column=0, padx=2, pady=2)
	# 		# self.label.pack(side = "bottom", fill = "both", expand = "yes")


	# 	# create a Text widget
	# 		self.txt = tki.Text(txt_frm, borderwidth=3, relief="sunken")
	# 		self.txt.config(font=("consolas", 12), undo=True, wrap='word')
	# 		self.txt.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)

	# 	# create a Scrollbar and associate it with txt
	# 		scrollb = tki.Scrollbar(txt_frm, command=self.txt.yview)
	# 		scrollb.grid(row=1, column=1, sticky='nsew')
	# 		self.txt['yscrollcommand'] = scrollb.set

	# 	# create a Entry widget
	# 		self.username = tki.StringVar()
	# 		self.name = tki.Entry(txt_frm, textvariable=self.username)
	# 		self.name.grid(row=2, column=0, padx=2, pady=2)

	# 	def command(self):
	# 		self.entry.delete(0, END)


	# app = App()
	# app.root.mainloop()

	display_func()

if __name__ == '__main__':
	main()
