import tkinter as tk
from tkinter import filedialog, Text, Label
from tkinter.messagebox import showinfo
import os, settings
import globalvars as gv
from Navigator import Navigator

# initialize global variables
settings.init()

# set working directory if one exists from save file
if os.path.isfile('./save.txt'):
	with open('save.txt', 'r') as f:
		line = f.read()
		if line != '':
			gv.set_directory(line)

# set the wordbank from file
if os.path.isfile('./wordbank.txt'):
	with open('./wordbank.txt', 'r') as f:
		line = f.read()
		if line != '':
			gv.set_wordbank_str(line)

if __name__ == '__main__':
	
	# tkinter root
	root = tk.Tk()

	app = Navigator(root)
	app.pack(side="top", fill="both", expand=True)

	# start tkinter mainloop
	root.title("BSubs")
	root.minsize(960, 640)
	root.mainloop()

	# write current directory to save file
	directory = gv.get_directory()
	with open('./save.txt', 'w') as f:
		f.write(directory)
	f.close()

	# write wordbank to wordbank file
	wordbank = gv.get_wordbank_str()
	with open('./wordbank.txt', 'w') as f:
		f.write(wordbank)
	f.close()
#皕