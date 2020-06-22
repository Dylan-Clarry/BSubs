# imports
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QPushButton, QDialog, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QButtonGroup, QListWidget, QToolBar, QMenuBar, QAction, QLabel, QLineEdit, QFormLayout, QComboBox, QLineEdit
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QRect
import sys

# module imports
import file_system as fs
from gsettings import Settings

# BSubs imports
import pages.newcollectionpage_functions as ncpf

# set global settings
settings = Settings.instance()

class NewCollectionPage(QDialog):
	def __init__(self):
		super().__init__()

		# set window
		self.setWindowIcon(QtGui.QIcon('./logo.png'))
		self.setWindowTitle("Settings")
		self.move(100, 100)

		# ==============================
		# New Collection Form
		# ==============================
		coll_form = QVBoxLayout()
		name_form = QHBoxLayout()

		name_lbl = QLabel("Name:")
		name_form.addWidget(name_lbl)

		name_textbox = QLineEdit()
		name_form.addWidget(name_textbox)

		coll_form.addLayout(name_form)

		create_btn = QPushButton("Create Collection")

		coll_form.addWidget(create_btn)

		create_btn.clicked.connect(lambda: ncpf.create_new_collection(self, name_textbox))

		# ==============================
		# Bind Layouts
		# ==============================
		newcoll_grid = QGridLayout()

		# add nested grid layouts
		newcoll_grid.addLayout(coll_form, 0, 0)

		# set grid proportions
		newcoll_grid.setRowStretch(0, 0)
		newcoll_grid.setColumnStretch(0, 0)

		self.setLayout(newcoll_grid)

		

