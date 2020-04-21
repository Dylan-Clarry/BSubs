# imports
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QPushButton, QDialog, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QButtonGroup, QListWidget, QToolBar, QMenuBar, QAction, QLabel, QLineEdit, QFormLayout, QComboBox
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QRect
import easygui
import sys

# BSubs imports
from gsettings import settings

class SettingsPage(QDialog):
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
		change_dir_btn.clicked.connect(lambda: self.choose_directory(dir_target_lbl))
		dir_layout.addWidget(change_dir_btn, 0, 2)

		# row 1
		output_dir_lbl = QLabel("Output Directory")
		dir_layout.addWidget(output_dir_lbl, 1, 0)

		output_dir_target_lbl = QLabel("/Users/dylanclarry/Documents/projects/BSubs")
		dir_layout.addWidget(output_dir_target_lbl, 1, 1)

		change_output_dir_btn = QPushButton("Change Output Directory")
		change_output_dir_btn.clicked.connect(lambda: self.choose_directory(output_dir_target_lbl))
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
		save_changes_btn.clicked.connect(lambda: self.save_settings(dir_target_lbl, output_dir_target_lbl, lang_combox))
		dir_layout.addWidget(save_changes_btn, 3, 2)

		# ==============================
		# Bind Layouts
		# ==============================
		settings_grid = QGridLayout()

		settings_grid.addLayout(dir_layout, 0, 0)

		settings_grid.setRowStretch(0, 0)
		settings_grid.setColumnStretch(0, 0)

		self.setLayout(settings_grid)

		# self.setCentralWidget(QWidget())
		# self.centralWidget().setLayout(settings_grid)

	# select directory prompt and updates label
	def choose_directory(self, lbl):
		print("hellos from directory")
		try:
			directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
			if directory != '':
				lbl.setText(directory)
		except:
			print("directory change cancelled.")

	# saves new settings to the global settings
	def save_settings(self, directory, output, lang):
		print("directory: ", directory.text())
		print("output: ", output.text())
		print("lang: ", str(lang.currentText()))
		settings.set_directory(directory.text())
		settings.set_output_dir(output.text())
		settings.set_language(str(lang.currentText()))
		settings.print_all()










