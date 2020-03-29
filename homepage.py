from PyQt5.QtWidgets import QMainWindow, QPushButton, QDialog
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect
import sys

class Homepage(QMainWindow):
	def __init__(self):
		super().__init__()

		self.title = "BSubs"
		self.top = 100
		self.left = 100
		self.width = 400
		self.height = 300

		self.createBtn()

		self.initWindow()


	def initWindow(self):
		self.setWindowIcon(QtGui.QIcon('./logo.png'))
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)

		self.show()

	def createBtn(self):
		button = QPushButton("Close Application", self)
		#button.move(50, 50)
		button.setGeometry(QRect(100, 100, 200, 50))
		# button.setIcon(QtGui.QIcon('logo.png'))
		# button.setIconSize(QtCore.QSize(40, 40))
		button.setToolTip("<h2>Close Application</h2>")
		button.clicked.connect(self.clickMe)

	def clickMe(self):
		sys.exit()