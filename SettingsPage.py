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
		# Dir Layout
		# ==============================
		dir_layout = QGridLayout()

		# row 0
		dir_lbl = QLabel("Directory")
		dir_layout.addWidget(dir_lbl, 0, 0)

		dir_target_lbl = QLabel("/Users/dylanclarry/Documents/projects/BSubs")
		dir_layout.addWidget(dir_target_lbl, 0, 1)

		change_dir_btn = QPushButton("Change Directory")
		change_dir_btn.clicked.connect(self.choose_directory)
		dir_layout.addWidget(change_dir_btn, 0, 2)

		# row 1
		output_dir_lbl = QLabel("Output Directory")
		dir_layout.addWidget(output_dir_lbl, 1, 0)

		output_dir_target_lbl = QLabel("/Users/dylanclarry/Documents/projects/BSubs")
		dir_layout.addWidget(output_dir_target_lbl, 1, 1)

		change_output_dir_btn = QPushButton("Change Output Directory")
		change_output_dir_btn.clicked.connect(self.choose_directory)
		dir_layout.addWidget(change_output_dir_btn, 1, 2)

		# row 2
		lang_lbl = QLabel("Language")
		dir_layout.addWidget(lang_lbl, 2, 0)

		lang_combox = QComboBox()
		lang_combox.addItem("Chinese (简体中文)")
		lang_combox.addItem("Japanese (日本語)")
		dir_layout.addWidget(lang_combox, 2, 1)

		# row 3
		save_changes_btn = QPushButton("Save Changes")
		#save_changes_btn.triggered.connect(self.settings_page)
		dir_layout.addWidget(save_changes_btn, 3, 2)

		# ==============================
		# Bind Layouts
		# ==============================
		settings_grid = QGridLayout()

		settings_grid.addLayout(dir_layout, 0, 0)

		settings_grid.setRowStretch(0, 0)
		settings_grid.setColumnStretch(0, 0)

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



















