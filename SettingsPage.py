# imports
from PyQt5.QtWidgets import QMainWindow, QPushButton, QDialog, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QButtonGroup, QListWidget, QToolBar, QMenuBar, QAction
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
		self.setWindowTitle("BSubs")
		#self.setGeometry(100, 100, 960, 640)
		self.move(100, 100)

		# ==============================
		# Toolbar
		# ==============================

		toolbar = QToolBar("the toolbar")
		self.addToolBar(toolbar)

		set_directory_btn = QAction(QIcon("./assets/icons/blue-folder.png"), "Set Directory", self)
		set_directory_btn.triggered.connect(saying)
		toolbar.addAction(set_directory_btn)

		set_output_btn = QAction(QIcon("./assets/icons/blue-folder-export.png"), "Set Output Folder", self)
		set_output_btn.triggered.connect(saying)
		toolbar.addAction(set_output_btn)

		wordbank_btn = QAction(QIcon("./assets/icons/sort-alphabet-column.png"), "Open Wordbank", self)
		wordbank_btn.triggered.connect(saying)
		toolbar.addAction(wordbank_btn)

		edit_exports_btn = QAction(QIcon("./assets/icons/inbox--pencil.png"), "Edit Exports", self)
		edit_exports_btn.triggered.connect(saying)
		toolbar.addAction(edit_exports_btn)

		export_btn = QAction(QIcon("./assets/icons/document-export.png"), "Export Cards", self)
		export_btn.triggered.connect(saying)
		toolbar.addAction(export_btn)

		settings_btn = QAction(QIcon("./assets/icons/gear.png"), "Settings", self)
		settings_btn.triggered.connect(saying)
		toolbar.addAction(settings_btn)

		# ==============================
		# SideBar
		# ==============================
		side_layout = QVBoxLayout()

		side_list = QListWidget()
		side_list.insertItem(0, '流星')
		side_list.insertItem(1, '歌手')
		side_list.insertItem(2, '刺客')

		side_layout.addWidget(side_list)

		# ==============================
		# Episodes
		# ==============================
		ep_layout = QGridLayout()

		ep_list = QListWidget()
		ep_list.insertItem(0, '第一集')
		ep_list.insertItem(1, '第二集')
		ep_list.insertItem(2, '第三集')

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

		home_grid.addLayout(side_layout, 0, 0)
		home_grid.addLayout(ep_layout, 0, 1)
		home_grid.addLayout(bott_bar_left_layout, 1, 0)
		home_grid.addLayout(bott_bar_right_layout, 1, 1)

		home_grid.setRowStretch(0, 3)
		home_grid.setColumnStretch(0, 1)
		home_grid.setColumnStretch(1, 3)

		self.setCentralWidget(QWidget())
		self.centralWidget().setLayout(home_grid)

def saying():
	print("asdfasdfdsfdsaf")

