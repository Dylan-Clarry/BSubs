'''
srsminer.py
Dylan Clarry

A tool for mining sentences for anki using video and srt files that reduces the size of media collections
'''

import srt, pprint, os, subprocess
from playsound import playsound
from chinese import ChineseAnalyzer
from Sub import Sub
from datetime import datetime

# parse srt file to sub objects
def parse_srt(subtitle_file):

	# open srt file
	file = open(subtitle_file, 'r')
	lines = file.readlines()
	file.close()

	subs = []
	analyzer = ChineseAnalyzer()
	i = 0
	c = 0
	while i < len(lines):
		index = lines[i].strip('\n')
		i += 1
		if i >= len(lines): break
		start, end, dur = split_times(lines[i])
		i += 1
		if i >= len(lines): break
		content = lines[i].strip('\n')
		i += 1
		while lines[i] != "\n":
			content += lines[i].strip('\n')
			i += 1
		tokens = remove_garbage(analyzer.parse(content).tokens())
		i += 1
		c += 1
		subs.append(Sub(index, start, end, dur, content, tokens))
		print()
	return subs

# remove none Chinese words from word list
def remove_garbage(arr):
	punc = '[@_!#$%^&*()<>?/\|}{~:]'
	chinese_punc = "！？｡。＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏."
	i = 0
	count = len(arr)
	while i < count:
		word = arr[i]

		# if the word is either non-chinese or srt encoding remove from the word list
		if is_english(word) or word == '\u202a' or word == '\u202c' or word in chinese_punc or word in punc:
			del arr[i]
			count -= 1
			i -= 1
		i += 1
	return arr

# determines if the word contains characters belonging to the english alphabet
def is_english(word):
    try:
        word.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

# splits an srt timestamp into start, end, and duration variables
def split_times(times):

	# split and trim start and end times of subtitle
	times = times.split(' --> ')
	start = times[0].replace(',', '.').strip('\n')
	end = times[1].replace(',', '.').strip('\n')

	# get duration of clip
	tformat = '%H:%M:%S.%f'
	sta = datetime.strptime(start, tformat)
	en = datetime.strptime(end, tformat)
	dur = str(en - sta)
	if (':' in dur[len(dur) - 3:]) is False:
		dur = '0' + dur[0:len(dur) - 3]

	return start, end, dur

#main()
# video to audio mp3
#ffmpeg -i test_01.mp4 -c:a libmp3lame -q:a 4 output.mp3

# video to audio mp3 given timestamp
#ffmpeg -i test_01.mp4 -ss 00:01:20.333 -t 00:00:03 -q:a 0 -map a ../output/sample.mp3

# ffmpeg play audio file
#ffplay -nodisp -autoexit ./input/test_01.mp4 -ss 00:01:32.708 -t 00:00:03.542
#subprocess.call(['ffplay', '-nodisp', '-autoexit', './output/sample.mp3' ])

# ffmpeg snapshot
#ffmpeg -ss 01:23:45 -i input -vframes 1 -q:v 2 output.jpg

#playsound('./test_01.mp4', { true/false })

#ffplay -nodisp -autoexit ./input/test_01.mp4 -ss 00:01:32.708 -t 00:00:03.542

#ffmpeg -i ./input/test_01.mp4 -ss 00:01:32.708 -t 00:00:03.542 -q:a 0 -map a ./output/sample.mp3
#ffmpeg -i ./input/test_01.mp4 -c:a libmp3lame -q:a 4 ./input/aded.mp3


