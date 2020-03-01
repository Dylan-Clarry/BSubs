import tkinter as tk
from tkinter import filedialog, Text, Label
from tkinter.messagebox import showinfo
import os, settings, helper
import globalvars as gv
import homepage_functions as hpf
import subprocess as sp
import condenser as cd
from Homepage import Homepage
from SentencePage import SentencePage

# navigator class to handle loading different pages
class Navigator(tk.Frame):

	def __init__(self, *args, **kwargs):
		tk.Frame.__init__(self, *args, **kwargs)

		# main container that pages get raised to
		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		# initialize each page in the navigator
		self.frames = {}
		pages = (Homepage, SentencePage)

		for F in pages:

			frame = F(container, self)

			self.frames[F] = frame

			frame.grid(row=0, column=0, sticky="nsew")

		# show the homepage
		self.show_frame(Homepage)

	# load the page
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()