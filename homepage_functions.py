import tkinter as tk
from tkinter import filedialog, Text, Label
from tkinter.messagebox import showinfo
import os, settings, helper
import globalvars as gv
import subprocess as sp
import condenser as cd

# loads previously saved directory
def load_directory(frame, frame2):

	settings.tkinit()
	directory = gv.get_directory()
	collections = gv.get_collections()

	print('directory', directory)
	print('collections', collections)

	if(directory != "Not Set"):
		collections = list(os.walk(directory))[0][1]
		gv.set_collections(collections)
	set_collections(frame, frame2)

# sets the working directory
def set_directory(dir_lbl, frame, frame2):
	
	directory = filedialog.askdirectory()
	gv.set_directory()

	dir_lbl.config(text=directory)

	collections = list(os.walk(directory))[0][1]
	set_collections(frame, frame2)

# sets up a new collection in the current directory
def new_collection(root, frame, frame2):

	prompt = tk.Toplevel()
	prompt.wm_title("New Collection")

	# position prompt at root
	x = root.winfo_x()
	x_offset = 50
	y = root.winfo_y()
	y_offset = 50
	prompt.geometry("480x320+%d+%d" % (x + x_offset, y + y_offset))

	tk.Label(prompt, text="First Name").grid(row=0)
	name_entry = tk.Entry(prompt)
	name_entry.grid(row=0, column=1)

	finish_btn = tk.Button(prompt, text="Create Collection", command=lambda: new_collection_aux(frame, frame2, prompt, name_entry))
	finish_btn.grid(row=2, column=0)

def new_collection_aux(frame, frame2, prompt, name_entry):
	name = name_entry.get()
	print(name)
	gv.add_to_collection(name)

	set_collections(frame, frame2)

	prompt.destroy()

	name = '/' + name
	folder = gv.get_directory() + name
	media = gv.get_directory() + name + '/media'
	subtitles = gv.get_directory() + name + '/subtitles'
	condensed = gv.get_directory() + name + '/condensed'
	temp = gv.get_directory() + name + '/temp'
	audio = gv.get_directory() + name + '/audio'

	print(folder)
	print(media)
	print(subtitles)
	print(condensed)
	print(temp)
	print(audio)

	sp.call(['mkdir', folder])
	sp.call(['mkdir', media, subtitles, condensed, temp, audio])

# add collections to canvas
def set_collections(frame, frame2):

	collections = gv.get_collections()
	
	print('asdf: ', collections)
	print('qwer: ', gv.get_sel_coll())

	# clear current frame
	for widget in frame.winfo_children():
		widget.destroy()

	# if there are no entries in collections
	if len(collections) == 0:
		label = tk.Label(frame, text="No Collections")
		label.pack()
	else:

		# add all collections to frame
		for i in range(len(collections)):
			radio_btn = tk.Radiobutton(frame, text=collections[i], variable=settings.sel_coll, value=collections[i], command=lambda: set_episodes(frame2, settings.sel_coll.get()))
			radio_btn.pack(anchor='w')
		settings.sel_coll.set(0)

# add currently selected collections episodes to canvas
def set_episodes(frame, coll_name):
	
	directory = gv.get_directory() + '/' + settings.sel_coll.get() + '/media'
	
	print('coll_name: ', coll_name)
	print('directory: ', directory)
	print('settings:', settings.sel_coll.get())
	print('files: ', os.listdir(directory))

	# get episodes from current collection
	episodes = os.listdir(directory)

	# get rid of dsstore files
	i = 0
	count = len(episodes)
	while i < count:
		if episodes[i] == '.DS_Store':
			episodes.pop(i)
			count -= 1
		i += 1
	helper.mergesort(episodes)
	gv.set_episodes(episodes)
	print(episodes)

	# clear current frame
	for widget in frame.winfo_children():
		widget.destroy()

	# if there are no entries in collections
	if len(episodes) == 0:
		label = tk.Label(frame, text="No Episodes")
		label.pack()
	else:

		# add all episodes to frame
		for i in range(len(episodes)):
			radio_btn = tk.Radiobutton(frame, text=episodes[i].strip('.mp4'), variable=settings.sel_ep, value=episodes[i], command=lambda: gv.build_paths())
			radio_btn.pack(anchor='w')
		settings.sel_ep.set(0)