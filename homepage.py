# imports
from PyQt5.QtWidgets import QMainWindow, QPushButton, QDialog, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QButtonGroup, QListWidget, QToolBar, QMenuBar, QAction
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QRect
import sys

# BSubs imports
from gsettings import settings

class Homepage(QMainWindow):
	def __init__(self):
		super().__init__()

		# set window
		self.setWindowIcon(QtGui.QIcon('./logo.png'))
		self.setWindowTitle("BSubs")
		#self.setGeometry(100, 100, 960, 640)
		self.move(100, 100)

		# ==============================
		# Toolbar
		# ==============================
		# self.toolbar_layout = QMenuBar(self)
		# exit_menu = self.toolbar_layout.addMenu('File')
		# exit_action = QAction('Exit', self)
		# exit_menu.addAction(exit_action)

		toolbar = QToolBar("the toolbar")
		self.addToolBar(toolbar)

		set_directory_btn = QAction(QIcon("./assets/icons/blue-folder-horizontal.png"), "Set Directory", self)
		set_directory_btn.triggered.connect(saying)
		toolbar.addAction(set_directory_btn)

		settings_btn = QAction(QIcon("./assets/icons/gear.png"), "Settings", self)
		settings_btn.triggered.connect(saying)
		toolbar.addAction(settings_btn)

		# ==============================
		# SideBar
		# ==============================
		side_layout = QVBoxLayout()

		side_list = QListWidget()
		side_list.insertItem(0, '0')
		side_list.insertItem(1, '1')
		side_list.insertItem(2, '2')

		side_layout.addWidget(side_list)

		# ==============================
		# Episodes
		# ==============================
		ep_layout = QGridLayout()

		ep_list = QListWidget()
		ep_list.insertItem(0, 'aswdfasdfs')
		ep_list.insertItem(1, 'aswdfasdfs')
		ep_list.insertItem(2, 'aswdfasdfs')

		ep_layout.addWidget(ep_list)

		# ==============================
		# Bottom Bar left
		# ==============================
		bott_bar_left_layout = QHBoxLayout()

		new_coll_btn = QPushButton("New Collection")

		bott_bar_left_layout.addWidget(new_coll_btn)

		# ==============================
		# Bottom Bar right
		# ==============================
		bott_bar_right_layout = QHBoxLayout()

		condense_btn = QPushButton("Condenser")
		miner_btn = QPushButton("Sentence Miner")

		condense_btn.clicked.connect(saying)

		bott_bar_right_layout.addWidget(condense_btn)
		bott_bar_right_layout.addWidget(miner_btn)

		bg = QButtonGroup()
		bg.addButton(condense_btn)
		bg.addButton(miner_btn)

		# ==============================
		# Bind Layouts
		# ==============================
		home_grid = QGridLayout()

		home_grid.addLayout(side_layout, 1, 0)
		home_grid.addLayout(ep_layout, 1, 1)
		home_grid.addLayout(bott_bar_left_layout, 2, 0)
		home_grid.addLayout(bott_bar_right_layout, 2, 1)

		self.setCentralWidget(QWidget())
		self.centralWidget().setLayout(home_grid)

		print(settings.sayhello())


	def createBtn(self):
		button = QPushButton(settings.return_hello(), self)
		#button.move(50, 50)
		button.setGeometry(QRect(100, 100, 200, 50))
		# button.setIcon(QtGui.QIcon('logo.png'))
		# button.setIconSize(QtCore.QSize(40, 40))
		button.setToolTip("<h2>Close Application</h2>")
		button.clicked.connect(self.clickMe)

def saying():
	print("asdfasdfdsfdsaf")



