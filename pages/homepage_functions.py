# imports
import os, helper

# module imports
from gsettings import Settings

# set global settings
settings = Settings.instance()

# sets the collections for the current working directory
def set_collections(coll_widget, ep_widget):
	print("called")
	directory = settings.get_directory()
	print(directory)

	if(directory != ""):
		collections = list(os.walk(directory))[0][1]
		print("collections:", collections)

		for coll in collections:
			coll_widget.addItem(coll)

		coll_widget.itemClicked.connect(lambda: set_episodes(coll_widget.currentItem(), ep_widget))

def set_episodes(item, ep_widget):
	print(item.text() + " clicked")
	settings.set_curr_coll(item.text())
	settings.set_curr_ep("")
	settings.print_all()

	print("current collection: " + settings.get_coll_dir())

	directory = settings.get_video_dir() + '/'
	print(directory)

	if(directory != ""):
		episodes = os.listdir(directory)
		print(episodes)

		ep_widget.clear()

		helper.mergesort(episodes)

		for ep in episodes:
			ep_widget.addItem(ep.strip('.mp4'))

		ep_widget.itemClicked.connect(lambda: set_ep_sel(ep_widget.currentItem()))

def set_ep_sel(item):
	settings.set_curr_ep(item.text())
	settings.print_all()