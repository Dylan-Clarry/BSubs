import settings, bsubs
from Episode import Episode

# getters and setters for global variables
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


# setting and getting the current episode object
def set_curr_ep():
	settings.curr_episode = Episode(get_directory(), get_sel_coll(), get_sel_ep())

def get_curr_ep():
	return settings.curr_episode


# setter and getter for keeping track of the current sub
def set_curr_subs():
	settings.curr_subs = bsubs.parse_srt(get_subtitle_file())
	settings.curr_subs[0].print_sub()

def get_curr_subs():
	return settings.curr_subs


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
	print('\nGlobal Variables')
	print("===================")
	print('directory: ', get_directory())
	print('collections: ', get_collections())
	print('episodes: ', get_episodes())
	print('sel_coll: ', get_sel_coll())
	print('sel_ep: ', get_sel_ep())
	print()
	get_curr_ep().print_paths()
	print()