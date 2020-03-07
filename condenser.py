# python audio condenser
# condenser.py
# Dylan Clarry
# dylanclarry.ca https://github.com/Dylan-Clarry

# imports
import os, subprocess, settings, bsubs
import globalvars as gv

def produce_single_audio():

	#if collection != '' and collection != 0 and episode != '' and episode != 0:

	print('single\n======')

	episode = gv.get_curr_ep()
	collection_dir = episode.get_collection_dir()
	audio_dir = episode.get_audio_dir()
	temp_dir = episode.get_temp_dir()
	condensed_dir = episode.get_condensed_dir()

	subtitle = episode.get_episode_suffix()
	episode_file = episode.get_episode_file()
	subtitle_file = episode.get_subtitle_file()
	audio_file = episode.get_audio_file()

	gv.print_all_global()

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

	build = sh_build_command(temp_dir, condensed_dir, subtitle + '.mp3', size)

	# build condensed audio file
	subprocess.call(build)

	# clear the temp folder
	clear_temp_folder(temp_dir, size)

def produce_collection_audio():

	print('episodes\n======')

	# get currently selected
	temp_episode = gv.get_sel_ep()
	episodes = gv.get_episodes()

	for episode in episodes:
		gv.set_sel_ep(episode)
		gv.build_paths()
		produce_single_audio()

	# set back to previously selected episode radio button
	gv.set_sel_ep(temp_episode)


# deletes all audio clips after audio condensing is complete
def clear_temp_folder(dir, size):

	# *change to dynamically get size of folder*

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