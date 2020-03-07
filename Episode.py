class Episode:

	# contructor
	def __init__(self, directory, collection, episode):
		self.subs = []
		self.curr_sub = 0
		self.size = len(self.subs)
		self.collection = directory + '/' + collection
		self.episode = episode
		self.extension = '.mp4'

	# populates the episodes subs with sub objects
	def set_subs(self, subarr):
		self.subs = subarr

	# populates the episodes subs with sub objects
	def set_subs(self, subarr):
		self.subs = subarr
		self.size = len(subarr)

	# returns a sub at a given index
	def get_sub_at_index(self, index):
		return self.subs[index]

	# gets the current sub
	def get_curr_sub(self):
		return self.subs[self.curr_sub]

	# sets the current sub to the next sub
	def next_sub(self):
		if self.curr_sub != self.size:
			self.curr_sub += 1

	# sets the current sub to the previous sub
	def next_sub(self):
		if self.curr_sub != 0:
			self.curr_sub -= 1




	# getters for episode pathways
	def get_collection_dir(self):
		return self.collection

	def get_audio_dir(self):
		return self.collection + '/audio/'

	def get_temp_dir(self):
		return self.collection + '/temp/'

	def get_condensed_dir(self):
		return self.collection + '/condensed/'

	def get_episode_suffix(self):
		return self.episode.strip(self.extension)

	def get_episode_file(self):
		return self.collection + '/media/' + self.episode

	def get_subtitle_file(self):
		return self.collection + '/subtitles/' + self.get_episode_suffix() + '.srt'

	def get_audio_file(self):
		return self.get_audio_dir() + self.get_episode_suffix() + '.mp3'

	# prints all of the episodes paths to folders
	def print_paths(self):
		print()
		print('\nEpisode Paths')
		print("===================")
		print('collection_dir: ', self.get_collection_dir())
		print('audio_dir: ', self.get_audio_dir())
		print('temp_dir: ', self.get_temp_dir())
		print('condensed_dir: ', self.get_condensed_dir())
		print('episode_suffix: ', self.get_episode_suffix())
		print('episode_file: ', self.get_episode_file())
		print('subtitle_file: ', self.get_subtitle_file())
		print('audio_file: ', self.get_audio_file())
		print()


