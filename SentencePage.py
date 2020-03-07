import tkinter as tk
from tkinter import filedialog, Text, Label
from tkinter.messagebox import showinfo
import os, settings, helper
import globalvars as gv
import homepage_functions as hpf
import sentence_page_functions as spf
import subprocess as sp
import condenser as cd

class SentencePage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		# circular imports
		from Homepage import Homepage

		print("yaa");

		# ===============
		# canvas
		# ===============

		# tkinter canvas
		canvas = tk.Canvas(self, height=640, width=960)
		canvas.grid(row=1, column=0, columnspan=2, sticky='w')

		# ===============
		# frames
		# ===============

		toolbar = tk.Frame(canvas)
		toolbar.grid(row=0, column=0, sticky='w')

		photo_row = tk.Frame(canvas, width=20)
		photo_row.grid(row=1, column=0, sticky='nw', pady=25)

		nav_row = tk.Frame(canvas)
		nav_row.grid(row=2, column=0, sticky='nw', pady=25)

		# ===============
		# toolbar
		# ===============

		homebtn = tk.Button(toolbar, text="Back to homepage", padx=10, pady=5, fg="black", bg="#263D42", command=lambda: controller.show_frame(Homepage))
		homebtn.pack()

		testbtn = tk.Button(toolbar, text="Test button", padx=10, pady=5, fg="black", bg="#263D42", command=lambda: spf.test())
		testbtn.pack()

		# ===============
		# photo row
		# ===============



		# ===============
		# nav row
		# ===============
		back_btn = tk.Button(nav_row, text="<<")
		play_sound_btn = tk.Button(nav_row, text="Play", command=lambda: spf.play_sound(gv.get_curr_subs()[5], gv.get_audio_file()))
		fwd_btn = tk.Button(nav_row, text=">>")
		back_btn.grid(row=0, column=0)
		play_sound_btn.grid(row=0, column=1)
		fwd_btn.grid(row=0, column=2)



		
