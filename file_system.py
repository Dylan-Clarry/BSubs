# imports
import sys, json, os

# module imports
from gsettings import Settings

# set global settings
settings = Settings.instance()

# read from the settings file and apply to settings
def read_settings_file():

	# read settings.json and set to settings
	file = "./settings.json"

	if os.path.isfile(file):
		with open(file, 'r') as read_file:
			data = json.load(read_file)
			print(data)

			print(data['directory'])
			settings.set_directory(data['directory'])
			settings.set_output_dir(data['outputDirectory'])
			settings.set_language(data['language'])
			settings.print_all()
	read_file.close()

# write current settings to settings file
def write_settings_file():
	directory = settings.get_directory()
	output_dir = settings.get_output_dir()
	language = settings.get_language()
	settings_data = {
		'directory': directory,
		'outputDirectory': output_dir,
		'language': language
	}
	print(json.dumps(settings_data, indent=4))

	# write settings to json file
	file = "./settings.json"

	with open(file, 'w') as write_file:
		json.dump(settings_data, write_file, indent=4)
	write_file.close()
