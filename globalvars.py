import settings

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

# getters for global pathways
def get_collection_dir():
	return settings.collection_dir

def get_audio_dir():
	return settings.audio_dir

def get_temp_dir():
	return settings.temp_dir

def get_condensed_dir():
	return settings.condensed_dir

def get_episode_suffix():
	return settings.episode_suffix

def get_episode_file():
	return settings.episode_file

def get_subtitle_file():
	return settings.subtitle_file

def get_audio_file():
	return settings.audio_file


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

# set path variables using currently selected collection and episode
def build_paths():
	settings.collection_dir = get_directory() + '/' + get_sel_coll()
	settings.audio_dir = get_collection_dir() + '/audio/'
	settings.temp_dir = get_collection_dir() + '/temp/'
	settings.condensed_dir = get_collection_dir() + '/condensed/'
	settings.episode_suffix = get_sel_ep().strip('.mp4')
	settings.episode_file = get_collection_dir() + '/media/' + get_sel_ep()
	settings.subtitle_file = get_collection_dir() + '/subtitles/' + get_episode_suffix() + '.srt'
	settings.audio_file = get_audio_dir() + get_sel_ep().strip('.mp4') + '.mp3'

# return path variables using currently selected collection and episode
def get_paths():
	return settings.collection_dir, settings.audio_dir, settings.temp_dir, settings.condensed_dir, settings.episode_suffix, settings.episode_file, settings.subtitle_file, settings.audio_file

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
	print('collection_dir: ', get_collection_dir())
	print('audio_dir: ', get_audio_dir())
	print('temp_dir: ', get_temp_dir())
	print('condensed_dir: ', get_condensed_dir())
	print('episode_suffix: ', get_episode_suffix())
	print('episode_file: ', get_episode_file())
	print('subtitle_file: ', get_subtitle_file())
	print('audio_file: ', get_audio_file())
	print()