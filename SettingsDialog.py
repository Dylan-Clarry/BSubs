# imports
from PyQt5.QtWidgets import QPushButton, QDialog, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QButtonGroup, QListWidget, QToolBar, QMenuBar, QAction
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QRect
import sys

# BSubs imports
from gsettings import settings

class Homepage(QMainWindow):
	def __init__(self):
		super().__init__()

		
