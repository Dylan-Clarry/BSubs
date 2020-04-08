# imports
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QPushButton, QDialog, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QButtonGroup, QListWidget, QToolBar, QMenuBar, QAction, QLabel, QLineEdit, QFormLayout, QComboBox
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QRect
import easygui
import sys

# BSubs imports
from gsettings import settings

class SettingsPage(QMainWindow):
	def __init__(self):
		super().__init__()

		# set window
		self.setWindowIcon(QtGui.QIcon('./logo.png'))
		self.setWindowTitle("Settings")
		#self.setGeometry(100, 100, 960, 640)
		self.move(100, 100)

		# ==============================
		# Form Layout
		# ==============================
		form_box = QFormLayout()

		# directory row
		dir_lbl = QLabel("Directory")
		dir_input = QLineEdit()

		form_box.addRow(dir_lbl, dir_input)

		# output directory row
		output_dir_lbl = QLabel("Directory")
		output_dir_input = QLineEdit()

		form_box.addRow(output_dir_lbl, output_dir_input)

		# language select row
		lang_lbl = QLabel("Language")
		lang_combox = QComboBox()
		lang_combox.addItem("Chinese (普通话)")

		form_box.addRow(lang_lbl, lang_combox)

		# buttons row
		cancel_btn = QPushButton("Cancel")
		save_btn = QPushButton("Save Changes")

		cancel_btn.clicked.connect(self.choose_directory)

		form_box.addRow(cancel_btn, save_btn)


		# fbox = QFormLayout()

		# l1 = QLabel("Name")
		# nm = QLineEdit()

		# fbox.addRow(l1,nm)

		# vbox = QVBoxLayout()

		# l2 = QLabel("Address")
		# add1 = QLineEdit()
		# add2 = QLineEdit()
		# vbox.addWidget(add1)
		# vbox.addWidget(add2)
		
		# fbox.addRow(l2,vbox)

		# hbox = QHBoxLayout()

		# r1 = QRadioButton("Male")
		# r2 = QRadioButton("Female")
		# hbox.addWidget(r1)
		# hbox.addWidget(r2)
		# hbox.addStretch()


		# fbox.addRow(QLabel("sex"),hbox)
		# fbox.addRow(QPushButton("Submit"), QPushButton("Cancel"))





		# formbox size policy
		# form_box_policy = form_box.sizePolicy()
		# policy.setHorizontalStretch(1)
		# form_box.setSizePolicy(form_box_policy)


		# ==============================
		# Bottom Bar
		# ==============================
		bott_bar_left_layout = QHBoxLayout()

		new_coll_btn = QPushButton("New Collection")

		bott_bar_left_layout.addWidget(new_coll_btn)

		# ==============================
		# Bottom Bar right
		# ==============================
		# bott_bar_layout = QHBoxLayout()

		# cancel_btn = QPushButton("Cancel")
		# save_changes_btn = QPushButton("Save Changes")

		# cancel_btn.clicked.connect(choose_directory)

		# bott_bar_layout.addWidget(cancel_btn)
		# bott_bar_layout.addWidget(save_changes_btn)

		# bg = QButtonGroup()
		# bg.addButton(cancel_btn)
		# bg.addButton(save_changes_btn)

		# ==============================
		# Bind Layouts
		# ==============================
		settings_grid = QGridLayout()

		settings_grid.addLayout(form_box, 0, 0)
		#settings_grid.addLayout(bott_bar_layout)

		settings_grid.setRowStretch(0, 6)
		settings_grid.setColumnStretch(0, 3)
		# settings_grid.setColumnStretch(1, 3)

		self.setCentralWidget(QWidget())
		self.centralWidget().setLayout(settings_grid)

	# lets the user select a directory
	def choose_directory(self):
		print("hellos from directory")
		directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
		print(directory)
		settings.set_directory(directory)
		settings.print_all()
		# return directory

def saying():
	print("asdfasdfdsfdsaf")



















