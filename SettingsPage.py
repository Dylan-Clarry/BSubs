# imports
from PyQt5.QtWidgets import QMainWindow, QPushButton, QDialog, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QButtonGroup, QListWidget, QToolBar, QMenuBar, QAction, QLabel, QLineEdit, QFormLayout, QComboBox
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QRect
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


		# ==============================
		# Bottom Bar
		# ==============================
		bott_bar_left_layout = QHBoxLayout()

		new_coll_btn = QPushButton("New Collection")

		bott_bar_left_layout.addWidget(new_coll_btn)

		# ==============================
		# Bottom Bar right
		# ==============================
		bott_bar_layout = QHBoxLayout()

		condense_btn = QPushButton("Condenser")
		miner_btn = QPushButton("Sentence Miner")

		condense_btn.clicked.connect(saying)

		bott_bar_layout.addWidget(condense_btn)
		bott_bar_layout.addWidget(miner_btn)

		bg = QButtonGroup()
		bg.addButton(condense_btn)
		bg.addButton(miner_btn)

		# ==============================
		# Bind Layouts
		# ==============================
		settings_grid = QGridLayout()

		settings_grid.addLayout(form_box, 0, 0)
		settings_grid.addLayout(bott_bar_layout, 1, 0)

		# settings_grid.setRowStretch(0, 3)
		# settings_grid.setColumnStretch(0, 1)
		# settings_grid.setColumnStretch(1, 3)

		self.setCentralWidget(QWidget())
		self.centralWidget().setLayout(settings_grid)

def saying():
	print("asdfasdfdsfdsaf")

