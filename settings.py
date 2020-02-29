import tkinter as tk

# initialize global variables
def init():
	global directory
	global collections
	global episodes
	directory = "Not Set"
	collections = []
	episodes = []

# initialize global tkinter variables
def tkinit():
	global sel_coll
	global sel_ep
	sel_coll = tk.StringVar()
	sel_ep = tk.StringVar()