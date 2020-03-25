import tkinter as tk
from tkinter import filedialog, Text, Label
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
import os, settings, helper
import globalvars as gv
import homepage_functions as hpf
import subprocess as sp
import condenser as cd
import exporter as xp
from Episode import Episode
from copy import deepcopy

def card_forward(lbl, photo, row):

	# set the next sub from current
	episode = gv.get_curr_ep()

	if lbl['text'] != ">> to start":
		episode.next_sub()
	episode.print_sub()

	# set sentence labels text to be next sentence
	lbl.config(text=episode.get_curr_sentence())

	#change the image
	img = generate_image()
	print(img)
	photo.config(image=img)
	photo.image = img

	print("image loaded")


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

def generate_image():
	episode = gv.get_curr_ep()
	image = ImageTk.PhotoImage(Image.open(episode.create_image()))
	print(episode.create_image())
	return image

def save_sub():
	sub = gv.get_curr_ep().get_curr_sub()
	sub.print_sub()

	gv.add_to_exports(sub)
	gv.print_exports()

def zero_t():
	words = gv.get_curr_ep().get_curr_sub().get_words()
	gv.append_to_wordbank(words)
	gv.print_wordbank()








