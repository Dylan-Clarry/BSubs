# imports
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QButtonGroup, QListWidget, QToolBar, QAction
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QRect
import sys

# page imports
from pages.NewCollectionPage import NewCollectionPage
from pages.SettingsPage import SettingsPage

# BSubs imports
from gsettings import Settings
import pages.homepage_functions as hpf

# set global settings
settings = Settings.instance()

class Homepage(QMainWindow):
	
	# connection to other pages
	sig_settings = QtCore.pyqtSignal()
	sig_new_coll = QtCore.pyqtSignal()

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

		wordbank_btn = QAction(QIcon("./assets/icons/sort-alphabet-column.png"), "Open Wordbank", self)
		#wordbank_btn.triggered.connect(saying)
		toolbar.addAction(wordbank_btn)

		edit_exports_btn = QAction(QIcon("./assets/icons/inbox--pencil.png"), "Edit Exports", self)
		#edit_exports_btn.triggered.connect(saying)
		toolbar.addAction(edit_exports_btn)

		export_btn = QAction(QIcon("./assets/icons/document-export.png"), "Export Cards", self)
		#export_btn.triggered.connect(saying)
		toolbar.addAction(export_btn)

		settings_btn = QAction(QIcon("./assets/icons/gear.png"), "Settings", self)
		settings_btn.triggered.connect(self.settings_page)
		toolbar.addAction(settings_btn)

		# ==============================
		# SideBar
		# ==============================
		side_layout = QVBoxLayout()

		coll_list = QListWidget()
		
		# created early for update reference
		ep_list = QListWidget()

		hpf.set_collections(coll_list, ep_list)

		side_layout.addWidget(coll_list)

		# ==============================
		# Episodes
		# ==============================
		ep_layout = QGridLayout()

		ep_layout.addWidget(ep_list)

		# ==============================
		# Bottom Bar left
		# ==============================
		bott_bar_left_layout = QHBoxLayout()

		new_coll_btn = QPushButton("New Collection")

		new_coll_btn.clicked.connect(self.new_coll_page)

		bott_bar_left_layout.addWidget(new_coll_btn)

		# ==============================
		# Bottom Bar right
		# ==============================
		bott_bar_right_layout = QHBoxLayout()

		condense_btn = QPushButton("Condenser")
		miner_btn = QPushButton("Sentence Miner")

		#condense_btn.clicked.connect(saying)

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

	def settings_page(self):
		self.sig_settings.emit()

	def new_coll_page(self):
		self.sig_new_coll.emit()










