import csv
import subprocess as sp
import globalvars as gv

def prep_tsv():
	episode = gv.get_curr_ep()
	episode.print_paths()
	sub = episode.get_index(5)
	sub.print_sub()


	deck = episode.get_episode_suffix()
	sound_name = deck + "_" + sub.get_start().replace(':', '-') + "-" + sub.get_end().replace(':', '-') + ".mp3"
	img_name = deck + "_" + sub.get_start().replace(':', '-') + "-" + sub.get_end().replace(':', '-') + ".jpg"

	sound = "[sound:" + sound_name + "]"
	img = "<img src=\"" + img_name + "\">"
	content = sub.get_content()


	# export media
	media_dir = episode.get_deck_dir() + 'media/'

	sp.call(['ffmpeg', '-i', episode.get_audio_file(), '-ss', sub.get_start(), '-t', sub.get_dur(), '-q:a', '0', '-map', 'a', media_dir + '' + sound_name])
	sp.call(['ffmpeg', '-ss', sub.get_end(), '-i', episode.get_episode_file(), '-vframes', '1', '-q:v', '2', media_dir + '' + img_name])

	# create deck tsv file
	deck_dir = episode.get_deck_dir() + '' + deck + '.tsv'
	with open(deck_dir, 'wt') as out_file:
		tsv_writer = csv.writer(out_file, delimiter='\t')
		tsv_writer.writerow([deck, sound, img, content])
	

	print("tsv card")
	print("==============")
	print("deck: ", deck)
	print("sound_name: ", media_dir + '' + sound_name, type(media_dir + '' + sound_name))
	print("img_name: ", media_dir + '' + img_name, type(media_dir + '' + img_name))
	print("content: ", content)


def export_to_deck():

	gv.print_exports()

	exports = gv.get_exports()
	episode = gv.get_curr_ep()
	deck = episode.get_episode_suffix()

	# create deck tsv file
	deck_dir = episode.get_deck_dir() + '' + deck + '.tsv'
	with open(deck_dir, 'wt') as out_file:
		tsv_writer = csv.writer(out_file, delimiter='\t')

		for export in exports:

			sound_name = deck + "_" + export.get_start().replace(':', '-') + "-" + export.get_end().replace(':', '-') + ".mp3"
			img_name = deck + "_" + export.get_start().replace(':', '-') + "-" + export.get_end().replace(':', '-') + ".jpg"

			sound = "[sound:" + sound_name + "]"
			img = "<img src=\"" + img_name + "\">"
			content = export.get_content()

			# export media
			media_dir = episode.get_deck_dir() + 'media/'

			sp.call(['ffmpeg', '-i', episode.get_audio_file(), '-ss', export.get_start(), '-t', export.get_dur(), '-q:a', '0', '-map', 'a', media_dir + '' + sound_name])
			sp.call(['ffmpeg', '-ss', export.get_end(), '-i', episode.get_episode_file(), '-vframes', '1', '-q:v', '2', media_dir + '' + img_name])

			# write row to tsv file
			tsv_writer.writerow([deck, sound, img, content])

	# clear exports
	gv.clear_exports()
	gv.print_exports()








