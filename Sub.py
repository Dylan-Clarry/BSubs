'''
Sub.py
Dylan Clarry

subtitle object
'''

# subtitle object to hold each subtitles timestamps and content
class Sub:

	# constructor
	def __init__(self, index, start, end, dur, content, words):
		self.index = index
		self.start = start
		self.end = end
		self.dur = dur
		self.content = content
		self.words = words

	# print out all subtitle details
	def print_sub(self):
		print('index: ', self.index)
		print('start: ', self.start)
		print('end: ', self.end, type(self.end))
		print('dur: ', self.dur, type(self.dur))
		print('content: ', self.content)
		print('words: ', self.words)

	# get index of sub object
	def get_index(self):
		return self.index

	# get start of sub object
	def get_start(self):
		return self.start

	# get end of sub object
	def get_end(self):
		return self.end

	# get duration of sub object
	def get_dur(self):
		return self.dur

	# get content of sub object
	def get_content(self):
		return self.content

	# get words of sub object
	def get_words(self):
		return self.words