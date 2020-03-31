from decorators.Singleton import Singleton

@Singleton
class Settings:

	__directory = ""
	__curr_coll = ""
	__curr_ep = ""
	__exports = []
	__wordbank = set()

	def __init__(self):
		print('Settings created')

	def print_all(self):
		print("============")
		print("All Settings")
		print("============")
		print("directory:", self.__directory)
		print("curr_coll:", self.__curr_coll)
		print("curr_ep  :", self.__curr_ep)
		print("exports  :", self.__exports)
		print("wordbank :", self.__wordbank)

# create settings singleton object
settings = Settings.instance()