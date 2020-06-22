# imports
import os, helper

# page imports
from pages.NewCollectionPage import NewCollectionPage

# module imports
from gsettings import Settings

# set global settings
settings = Settings.instance()

# sets the collections for the current working directory
def set_collections(coll_widget, ep_widget):
	directory = settings.get_directory()
	print('dir:', directory)

	if(directory != ""):
		collections = settings.get_curr_collections()
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

def init_new_coll():
	directory = settings.get_directory()