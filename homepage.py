# imports
from PyQt5.QtWidgets import QMainWindow, QPushButton, QDialog, QWidget, QGridLayout, QVBoxLayout
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

		# episode actions layout
		actions_layout = QGridLayout()
		actions_layout.setSpacing(0)
		
		single_btn = QPushButton("Condense single episode")
		all_btn = QPushButton("Condense all episodes")
		mine_btn = QPushButton("Sentence mine episode")

		actions_layout.addWidget(single_btn, 0, 0) # widget, row, col
		actions_layout.addWidget(all_btn, 1, 0)
		actions_layout.addWidget(mine_btn, 2, 0)

		self.setLayout(actions_layout)

		# actions_widget = QWidget()
		# actions_widget.setLayout(actions_layout)
		# self.setCentralWidget(actions_widget)


	def createBtn(self):
		button = QPushButton(settings.return_hello(), self)
		#button.move(50, 50)
		button.setGeometry(QRect(100, 100, 200, 50))
		# button.setIcon(QtGui.QIcon('logo.png'))
		# button.setIconSize(QtCore.QSize(40, 40))
		button.setToolTip("<h2>Close Application</h2>")
		button.clicked.connect(self.clickMe)