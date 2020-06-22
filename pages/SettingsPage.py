# imports
from PyQt5.QtWidgets import QDialog, QGridLayout, QFileDialog, QLabel, QPushButton, QComboBox
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QRect
import sys

# module imports
import file_system as fs
from gsettings import Settings

# set global settings
settings = Settings.instance()

class SettingsPage(QDialog):
	def __init__(self):
		super().__init__()

		# set window
		self.setWindowIcon(QtGui.QIcon('./logo.png'))
		self.setWindowTitle("Settings")
		self.move(100, 100)

		# ==============================
		# Dir Layout
		# ==============================
		dir_layout = QGridLayout()

		# ********************
		# row 0
		# ********************
		dir_lbl = QLabel("Directory")
		dir_layout.addWidget(dir_lbl, 0, 0)

		dir_target_lbl = QLabel(settings.get_directory())
		dir_layout.addWidget(dir_target_lbl, 0, 1)

		change_dir_btn = QPushButton("Change Directory")
		change_dir_btn.clicked.connect(lambda: self.choose_directory(dir_target_lbl))
		dir_layout.addWidget(change_dir_btn, 0, 2)

		# ********************
		# row 1
		# ********************
		output_dir_lbl = QLabel("Output Directory")
		dir_layout.addWidget(output_dir_lbl, 1, 0)

		output_dir_target_lbl = QLabel(settings.get_output_dir())
		dir_layout.addWidget(output_dir_target_lbl, 1, 1)

		change_output_dir_btn = QPushButton("Change Output Directory")
		change_output_dir_btn.clicked.connect(lambda: self.choose_directory(output_dir_target_lbl))
		dir_layout.addWidget(change_output_dir_btn, 1, 2)

		# ********************
		# row 2
		# ********************
		lang_lbl = QLabel("Language")
		dir_layout.addWidget(lang_lbl, 2, 0)

		lang_combox = QComboBox()
		lang_items = [
				"Chinese (简体中文)",
				"Japanese (日本語)"
				]
		lang_combox.addItems(lang_items)
		lang_combox.setCurrentIndex(lang_items.index(settings.get_language()))
		dir_layout.addWidget(lang_combox, 2, 1)

		# row 3
		save_changes_btn = QPushButton("Save Changes")
		save_changes_btn.clicked.connect(lambda: self.save_settings(dir_target_lbl, output_dir_target_lbl, lang_combox))
		dir_layout.addWidget(save_changes_btn, 3, 2)

		# ==============================
		# Bind Layouts
		# ==============================
		settings_grid = QGridLayout()

		# add nested grid layouts
		settings_grid.addLayout(dir_layout, 0, 0)

		# set grid proportions
		settings_grid.setRowStretch(0, 0)
		settings_grid.setColumnStretch(0, 0)

		self.setLayout(settings_grid)

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
		fs.write_settings_file()
		self.close()










