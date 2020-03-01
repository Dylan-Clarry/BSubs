# python audio condenser
# condenser.py
# Dylan Clarry
# dylanclarry.ca https://github.com/Dylan-Clarry

# imports
import os, subprocess, settings, bsubs
import globalvars as gv

def produce_single_audio(collection, episode):

	#if collection != '' and collection != 0 and episode != '' and episode != 0:

	print('single\n======')

	collection_dir = gv.get_directory() + '/' + collection
	audio_dir = collection_dir + '/audio/'
	temp_dir = collection_dir + '/temp/'
	condensed_dir = collection_dir + '/condensed/'

	subtitle = episode.strip('.mp4') + '.srt'
	episode_file = collection_dir + '/media/' + episode
	subtitle_file = collection_dir + '/subtitles/' + subtitle
	audio_file = audio_dir + episode.strip('.mp4') + '.mp3'

	print('collection: ', collection)
	print('episode: ', episode, episode_file)
	print('subtitle: ', subtitle, subtitle_file)

	print('exists: ', os.path.isfile(audio_file))

	file_exists = os.path.isfile(audio_file)
	if file_exists is False:
		video_to_audio(episode_file, audio_file)

	# parse srt file into subtitle object list
	subs = bsubs.parse_srt(subtitle_file)

	size = len(subs)
	for i in range(0, size):
		sub = subs[i]
		sub.print_sub()
		output = temp_dir + '' + str(i) + '.mp3'
		subprocess.call(['ffmpeg', '-i', audio_file, '-ss', sub.get_start(), '-t', sub.get_dur(), '-q:a', '0', '-map', 'a', output])

	build = sh_build_command(temp_dir, condensed_dir, episode.strip('.mp4') + '.mp3', size)

	# build condensed audio file
	subprocess.call(build)

	# clear the temp folder
	clear_temp_folder(temp_dir, size)

def produce_collection_audio(collection):

	print('episodes\n======')

	episodes = gv.get_episodes()

	for episode in episodes:
		print(collection, episode)
		produce_single_audio(collection, episode)

# deletes all audio clips after audio condensing is complete
def clear_temp_folder(dir, size):

	# change to dynamically get size of folder

	for i in range(0, size):
		file = dir + '' + str(i) + '.mp3'
		os.remove(file)

# converts a video file to an audio file using ffmpeg
def video_to_audio(episode_file, audio_file):
	
	# produce audio file from video
	subprocess.call(['ffmpeg', '-i', episode_file, '-c:a', 'libmp3lame', '-q:a', '4', audio_file])

# builds the ffmpeg command to concatenate all audio clips into a condensed audio file
def sh_build_command(clip_dir, output_dir, name, size):
	catstr = 'concat:'
	print(catstr)
	for i in range(0, size):
		catstr += clip_dir + str(i) + '.mp3|'

	#print(catstr)
	sh_command = [
		'ffmpeg',
		'-i',
		catstr,
		'-acodec',
		'copy',
		output_dir + name
	]
	return sh_command