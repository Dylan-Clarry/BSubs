from PyQt5.QtWidgets import QApplication
import sys

from Navigator import Navigator

def main():
	App = QApplication(sys.argv)
	navigator = Navigator()
	navigator.show_homepage()
	sys.exit(App.exec())

if __name__ == "__main__":
	main()