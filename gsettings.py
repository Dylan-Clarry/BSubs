from decorators.Singleton import Singleton

@Singleton
class Settings:

	__directory = ""
	__output_dir = ""
	__curr_coll = ""
	__curr_ep = ""
	__exports = []
	__wordbank = set()
	__language = ""

	def __init__(self):
		print('Settings created')

	# setters
	def set_directory(self, directory):
		self.__directory = directory

	def set_output_dir(self, output_dir):
		self.__output_dir = output_dir

	def set_curr_coll(self, curr_coll):
		self.__curr_coll = curr_coll

	def set_curr_ep(self, curr_ep):
		self.__curr_ep = curr_ep

	def set_exports(self, exports):
		self.__exports = exports

	def set_wordbank(self, wordbank):
		self.__wordbank = wordbank

	def set_language(self, language):
		self.__language = language

	# getters
	def get_directory(self):
		return self.__directory

	def get_output_dir(self):
		return self.__output_dir

	def get_curr_coll(self):
		return self.__curr_coll

	def get_curr_ep(self):
		return self.__curr_ep

	def get_exports(self):
		return self.__exports

	def get_wordbank(self):
		return self.__wordbank\

	def get_language(self):
		return self.__language

	def print_all(self):
		print("============")
		print("All Settings")
		print("============")
		print("directory :", self.__directory)
		print("output_dir:", self.__output_dir)
		print("curr_coll :", self.__curr_coll)
		print("curr_ep   :", self.__curr_ep)
		print("exports   :", self.__exports)
		print("wordbank  :", self.__wordbank)
		print("language  :", self.__language)

# create settings singleton object
settings = Settings.instance()