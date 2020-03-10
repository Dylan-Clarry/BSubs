import subprocess as sp
from bsubs import parse_srt

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
	def set_subs(self):
		self.subs = parse_srt(self.get_subtitle_file())
		self.size = len(self.subs)

	# returns a sub at a given index
	def get_index(self, index):
		return self.subs[index]

	# gets the current sub
	def get_curr_sub(self):
		return self.subs[self.curr_sub]

	# sets the current sub to the next sub
	def next_sub(self):
		if self.curr_sub < self.size - 1:
			self.curr_sub += 1

	# sets the current sub to the previous sub
	def prev_sub(self):
		if self.curr_sub != 0:
			self.curr_sub -= 1

	# returns the current sentence
	def get_curr_sentence(self):
		return self.get_curr_sub().get_content()

	# prints the current sub info
	def print_sub(self):
		curr = self.get_curr_sub()
		curr.print_sub()

	# plays the sound clip for the current sub
	def play_sub(self):
		curr = self.get_curr_sub()
		sp.call(['ffplay', '-nodisp', '-autoexit', self.get_audio_file(), '-ss', curr.get_start(), '-t', curr.get_dur()])

	# creates an image for the current sub in the temp folder
	def create_image(self):
		curr = self.get_curr_sub()
		temp_image = self.get_temp_dir() + 'temp.jpg'
		sp.call(['rm', temp_image])
		sp.call(['ffmpeg', '-ss', curr.get_end(), '-i', self.get_episode_file(), '-vframes', '1', '-q:v', '2', temp_image])
		return temp_image


	# getters for episode pathways
	def get_collection_dir(self):
		return self.collection

	def get_audio_dir(self):
		return self.collection + '/audio/'

	def get_temp_dir(self):
		return self.collection + '/temp/'

	def get_condensed_dir(self):
		return self.collection + '/condensed/'

	def get_deck_dir(self):
		return self.collection + '/deck/'

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


