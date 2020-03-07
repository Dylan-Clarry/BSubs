import tkinter as tk
from tkinter import filedialog, Text, Label
from tkinter.messagebox import showinfo
import os, settings, helper
import globalvars as gv
import homepage_functions as hpf
import subprocess as sp
import condenser as cd
from SentencePage import SentencePage

# sets up homepage on root
class Homepage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		# global tkinter variables
		settings.tkinit()

		# global variables
		directory = gv.get_directory()
		collections = gv.get_directory()

		# ===============
		# canvas
		# ===============

		# tkinter canvas
		canvas = tk.Canvas(self, height=640, width=960)
		canvas.grid(row=1, column=0, columnspan=2, sticky='w')

		# ===============
		# frames
		# ===============

		dirframe = tk.Frame(canvas)
		dirframe.grid(row=0, column=0, sticky='w')

		coll_col = tk.Frame(canvas, width=20)
		coll_col.grid(row=1, column=0, sticky='nw', pady=25)

		ep_col = tk.Frame(canvas)
		ep_col.grid(row=1, column=1, sticky='nw', pady=25)

		options_col = tk.Frame(canvas)
		options_col.grid(row=1, column=2, sticky='nw', pady=25)

		# ===============
		# directory
		# ===============

		# set directory button
		set_dir = tk.Button(dirframe, text='Set Directory', padx=10, pady=5, fg="black", bg="#263D42", command=lambda: hpf.set_directory(dir_lbl, collframe, epframe))
		set_dir.pack(side=tk.LEFT)

		# current directory label
		dir_lbl = Label(dirframe, text=directory)
		dir_lbl.pack(side=tk.LEFT)

		# ===============
		# collections
		# ===============

		# collections label
		coll_lbl = Label(coll_col, text="Collections")
		coll_lbl.pack()
		
		# new collection button
		new_coll = tk.Button(coll_col, text='New Collection', padx=10, pady=5, fg="black", bg="#263D42", command=lambda: hpf.new_collection(root, collframe, epframe))
		new_coll.pack()
		
		# frame holding collections
		collframe = tk.Frame(coll_col)
		collframe.pack()


		# ===============
		# episodes
		# ===============

		# episode label
		ep_lbl = Label(ep_col, text="Episodes")
		ep_lbl.pack(anchor='w')

		# frame holding episodes
		epframe = tk.Frame(ep_col)
		epframe.pack()

		# ===============
		# options
		# ===============

		# episode label
		options_lbl = Label(options_col, text="Options")
		options_lbl.pack(anchor='w')

		options_btn_frame = tk.Frame(options_col)
		options_btn_frame.pack()

		# condense selected episode into audio button
		condense_single_btn = tk.Button(options_btn_frame, text="Condense single episode", padx=10, pady=5, fg="black", bg="#263D42", command=lambda: cd.produce_single_audio())
		condense_single_btn.grid(row=0, column=0, sticky='nw')

		# condense all episodes into audio button
		condense_all_btn = tk.Button(options_btn_frame, text="Condense all episodes", padx=10, pady=5, fg="black", bg="#263D42", command=lambda: cd.produce_collection_audio())
		condense_all_btn.grid(row=1, column=0, sticky='nw')

		# go to sentence miner for currently selected episode
		sentence_mine_btn = tk.Button(options_btn_frame, text="Sentence mine episode", padx=10, pady=5, fg="black", bg="#263D42", command=lambda: [f() for f in [gv.set_curr_subs(), controller.show_frame(SentencePage)]])
		sentence_mine_btn.grid(row=2, column=0, sticky='nw')

		# load inital directory
		hpf.load_directory(collframe, epframe)





