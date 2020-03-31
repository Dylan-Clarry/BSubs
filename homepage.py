# imports
from PyQt5.QtWidgets import QMainWindow, QPushButton, QDialog, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect
import sys

# BSubs imports
from gsettings import settings

class Homepage(QWidget):
	def __init__(self):
		super().__init__()

		# set window
		self.setWindowIcon(QtGui.QIcon('./logo.png'))
		self.setWindowTitle("BSubs")
		self.setGeometry(100, 100, 960, 640)

		# ===============
		# Layouts
		# ===============

		# ===============
		# Toolbar
		# ===============
		toolbar_layout = QHBoxLayout()

		# ===============
		# SideBar
		# ===============
		side_layout = QVBoxLayout()

		# ===============
		# Episodes
		# ===============
		ep_layout = QGridLayout()

		# ===============
		# Bottom Bar
		# ===============
		bottbar_layout = QHBoxLayout()

		condense_btn = QPushButton("Condenser")
		miner_btn = QPushButton("Sentence Miner")

		bottbar_layout.addWidget(condense_btn)
		bottbar_layout.addWidget(miner_btn)

		# ===============
		# Bind Layouts
		# ===============
		home_grid = QGridLayout()

		home_grid.addLayout(toolbar_layout, 0, 0)
		home_grid.addLayout(side_layout, 1, 0)
		home_grid.addLayout(ep_layout, 1, 1)
		home_grid.addLayout(bottbar_layout, 2, 1)
		self.setLayout(home_grid)

		print(settings.sayhello())


	def createBtn(self):
		button = QPushButton(settings.return_hello(), self)
		#button.move(50, 50)
		button.setGeometry(QRect(100, 100, 200, 50))
		# button.setIcon(QtGui.QIcon('logo.png'))
		# button.setIconSize(QtCore.QSize(40, 40))
		button.setToolTip("<h2>Close Application</h2>")
		button.clicked.connect(self.clickMe)