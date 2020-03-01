import tkinter as tk

# initialize global variables
def init():
	global directory
	global collections
	global episodes
	directory = "Not Set"
	collections = []
	episodes = []

	global collection_dir
	global audio_dir
	global temp_dir
	global condensed_dir
	global episode_suffix
	global episode_file
	global subtitle_file
	global audio_file
	collection_dir = ""
	audio_dir = ""
	temp_dir = ""
	condensed_dir = ""
	episode_suffix = ""
	episode_file = ""
	subtitle_file = ""
	audio_file = ""

# initialize global tkinter variables
def tkinit():
	global sel_coll
	global sel_ep
	sel_coll = tk.StringVar()
	sel_ep = tk.StringVar()