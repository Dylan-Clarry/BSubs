import tkinter as tk
from tkinter import filedialog, Text, Label
from tkinter.messagebox import showinfo
import os, settings
import globalvars as gv
import homepage as hp

# initialize global variables
settings.init()

# set working directory if one exists from save file
if os.path.isfile('./save.txt'):
	with open('save.txt', 'r') as f:
		line = f.read()
		if line != '':
			gv.set_directory(line)

if __name__ == '__main__':
	
	# tkinter root
	root = tk.Tk()
	root.title("BSubs")
	root.minsize(960, 640)

	# global tkinter variables
	settings.tkinit()

	# set homepage
	hp.homepage(root)

	# start tkinter mainloop
	root.mainloop()

	# write current directory to save file
	directory = gv.get_directory()
	with open('save.txt', 'w') as f:
		f.write(directory)
#皕