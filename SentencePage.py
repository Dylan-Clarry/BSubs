import tkinter as tk
from tkinter import filedialog, Text, Label
from tkinter.messagebox import showinfo
import os, settings, helper
import globalvars as gv
import homepage_functions as hpf
import sentence_page_functions as spf
import exporter as xp
import subprocess as sp
import condenser as cd

class SentencePage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		# circular imports
		from Homepage import Homepage

		# ===============
		# canvas
		# ===============

		# tkinter canvas
		canvas = tk.Canvas(self, height=640, width=960)
		canvas.grid(row=1, column=0, columnspan=2, sticky='we')

		# ===============
		# frames
		# ===============

		toolbar = tk.Frame(canvas)
		toolbar.grid(row=0, column=0, sticky='w')

		photo_row = tk.Frame(canvas, width=20)
		photo_row.grid(row=1, column=0, columnspan=2, sticky='we', pady=25)

		sentence_row = tk.Frame(canvas)
		sentence_row.grid(row=2, column=0, columnspan=2, sticky='we', pady=25)

		nav_row = tk.Frame(canvas)
		nav_row.grid(row=3, column=0, sticky='we', pady=25)

		# ===============
		# toolbar
		# ===============

		homebtn = tk.Button(toolbar, text="Back to homepage", padx=10, pady=5, fg="black", bg="#263D42", command=lambda: controller.show_frame(Homepage))
		homebtn.pack()

		testbtn = tk.Button(toolbar, text="Export to Deck", padx=10, pady=5, fg="black", bg="#263D42", command=lambda: xp.export_to_deck())
		testbtn.pack(anchor='w')

		# ===============
		# photo row
		# ===============

		photo = tk.Label(photo_row)
		photo.pack()

		# ===============
		# sentence row
		# ===============
		sentence_lbl = tk.Label(sentence_row, text=">> to start")
		sentence_lbl.pack()

		# ===============
		# nav row
		# ===============
		back_btn = tk.Button(nav_row, text="<<", command=lambda: spf.card_back(sentence_lbl, photo, photo_row))
		back_btn.grid(row=0, column=0)

		play_sound_btn = tk.Button(nav_row, text="Play", command=lambda: spf.play_sound())
		play_sound_btn.grid(row=0, column=1)

		save_card_btn = tk.Button(nav_row, text="Save Card", command=lambda: spf.save_sub())
		save_card_btn.grid(row=0, column=2)

		zero_t_btn = tk.Button(nav_row, text="Zero Targets", command=lambda: spf.zero_t())
		zero_t_btn.grid(row=0, column=3)

		fwd_btn = tk.Button(nav_row, text=">>", command=lambda: spf.card_forward(sentence_lbl, photo, photo_row))
		fwd_btn.grid(row=0, column=4)

# spf.card_forward(sentence_lbl, photo, photo_row)
# [f() for f in [spf.card_forward(sentence_lbl, photo, photo_row), spf.play_sound()]]


