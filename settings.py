import tkinter as tk

# initialize global variables
def init():
	global directory
	global collections
	global episodes
	global exports
	global curr_episode
	global wordbank
	directory = "Not Set"
	collections = []
	episodes = []
	exports = []
	curr_episode = ""
	wordbank = set()

# initialize global tkinter variables
def tkinit():
	global sel_coll
	global sel_ep
	sel_coll = tk.StringVar()
	sel_ep = tk.StringVar()