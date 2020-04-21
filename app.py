from PyQt5.QtWidgets import QApplication
import sys

# module imports
import file_system as fs
import gsettings as gs
from Navigator import Navigator

def main():
	
	# read settings from settings file
	fs.read_settings_file()

	# run app at homepage
	App = QApplication(sys.argv)
	navigator = Navigator()
	navigator.show_homepage()
	sys.exit(App.exec())

if __name__ == "__main__":
	main()





# def qsort(L):
#     if len(L) <= 1: return L
#     return qsort( [ lt for lt in L[1:] if lt < L[0] ] ) + [ L[0] ]  +  qsort( [ ge for ge in L[1:] if ge >= L[0] ] )


# IMHO this is almost as nice as the Haskell version from www.haskell.org:
# qsort [] = [] 
# qsort (x:xs) = qsort elts_lt_x ++ [x] ++ qsort elts_greq_x
#                 where 
#                   elts_lt_x = [y | y <- xs, y < x] 
#                   elts_greq_x = [y | y <- xs, y >= x]