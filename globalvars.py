import settings

# getters and setters for all global variables
def set_directory(directory):
	settings.directory = directory

def set_collections(collections):
	settings.collections = collections

def set_episodes(episodes):
	settings.episodes = episodes

def get_directory():
	return settings.directory

def get_collections():
	return settings.collections

def get_episodes():
	return settings.episodes


# append to settings arrays
def add_to_collection(entry):
	settings.collections.append(entry)

def add_to_episodes(entry):
	settings.episodes.append(entry)


# tkinter global variables
def set_sel_coll(name):
	settings.sel_coll.set(name)

def set_sel_ep(name):
	settings.sel_ep.set(name)

def get_sel_coll():
	return settings.sel_coll.get()

def get_sel_ep():
	return settings.sel_ep.get()

# print all current global variables
def print_all_global():
	print('directory: ', get_directory())
	print('collections: ', get_collections())
	print('episodes: ', get_episodes())
	print('sel_coll: ', get_sel_coll())
	print('sel_ep: ', get_sel_ep())
	print()