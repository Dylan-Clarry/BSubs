import tkinter as tk
from tkinter import filedialog, Text, Label
from tkinter.messagebox import showinfo
import os, settings, helper
import globalvars as gv
import homepage_functions as hpf
import subprocess as sp
import condenser as cd

class SentencePage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		# circular imports
		from Homepage import Homepage

		print("sentence page")

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


		homebtn = tk.Button(dirframe, text="Back to homepage", padx=10, pady=5, fg="black", bg="#263D42", command=lambda: controller.show_frame(Homepage))
		homebtn.pack()