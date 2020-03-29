# class to be used as a decorator to make another class a singleton
class Singleton:

	# class constructor
	def __init__(self, decorated):
		self.__decorated = decorated

	# returns the singleton instance
	def instance(self):
		try:
			return self.__instance
		except AttributeError:
			self.__instance = self.__decorated()
			return self.__instance

	# if instance is called incorrectly raise error
	def __call__(self):
		raise TypeError('Singleton object must be accessed with `.instance()`')

	# check for current instance of object
	def __instancecheck__(self, inst):
		return isinstance(inst, self.__decorated)