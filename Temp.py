import tkinter as tk
from tkinter import filedialog, Text, Label
from tkinter.messagebox import showinfo
import os, settings, helper
import globalvars as gv
import homepage as hp
import homepage_functions as hpf
import subprocess as sp
import condenser as cd

class Temp(tk.Frame):
	def __init__(self, *args, **kwargs):
		tk.Frame.__init__(self, *args, **kwargs)

		framef = tk.Frame(self)
		framef.pack()

		btn = tk.Button(framef, text="textt")
		btn.pack(side="left")