import tkinter as tk
from tkinter import filedialog, Text, Label
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
import os, settings, helper
import globalvars as gv
import homepage_functions as hpf
import subprocess as sp
import condenser as cd
from Episode import Episode

def test():

	episode = gv.get_curr_ep()
	episode.print_paths()
	episode.subs[5].print_sub()


def card_forward(lbl, photo, row):

	# set the next sub from current
	episode = gv.get_curr_ep()
	episode.next_sub()
	episode.print_sub()

	# set sentence labels text to be next sentence
	lbl.config(text=episode.get_curr_sentence())








	#change the image
	img = generate_image()
	print(img)
	photo.config(image=img)
	photo.image = img

	# change the image
	# img = generate_image()
	# photo.grid_forget()

	# photo.configure(image=img)
	# photo.pack()

	












	# photo.create_image((50, 50), image=img)

	# print("IMAGEIMAGEIMAGE")
	# print("===============")
	# print(img)
	# print("===============")


def card_back(lbl, photo, row):

	# set the previous sub from current
	episode = gv.get_curr_ep()
	episode.prev_sub()
	episode.print_sub()

	# set sentence labels text to be previous sentence
	lbl.config(text=episode.get_curr_sentence())

	#change the image
	img = generate_image()
	print(img)
	photo.config(image=img)
	photo.image = img

def play_sound():
	episode = gv.get_curr_ep()
	episode.print_sub()
	episode.play_sub()

def generate_imager():
	episode = gv.get_curr_ep()
	image = tk.PhotoImage(file=episode.create_image())
	print(episode.create_image())

	return image

def generate_image():
	episode = gv.get_curr_ep()
	image = ImageTk.PhotoImage(Image.open(episode.create_image()))
	print(episode.create_image())

	return image



