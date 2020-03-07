import tkinter as tk
from tkinter import filedialog, Text, Label
from tkinter.messagebox import showinfo
import os, settings, helper
import globalvars as gv
import homepage_functions as hpf
import subprocess as sp
import condenser as cd

def test():
	gv.build_paths()
	gv.print_all_global()


def card_forward():
	return

def card_backward():
	return

def play_sound(sub, file):
	sub.print_sub()
	sp.call(['ffplay', '-nodisp', '-autoexit', file, '-ss', sub.get_start(), '-t', sub.get_dur()])