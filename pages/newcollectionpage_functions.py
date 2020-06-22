# module imports
from gsettings import Settings

from helper import raise_message

# set global settings
settings = Settings.instance()

# creates new collection
def create_new_collection(obj, name):
	if name.text() == "":
		title = "Empty name error"
		msg = "name field empty, please enter a collection name"
		raise_message(title, msg)
	#obj.close()