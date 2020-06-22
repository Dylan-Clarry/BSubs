from pages.Homepage import Homepage
from pages.SettingsPage import SettingsPage
from pages.NewCollectionPage import NewCollectionPage

class Navigator:

	# reveals the homepage
	def show_homepage(self):
		self.homepage = Homepage()
		self.homepage.sig_settings.connect(self.show_settings_page)
		self.homepage.sig_new_coll.connect(self.show_new_collection_page)
		self.homepage.show()
	
	# reveals the settings page
	def show_settings_page(self):
		self.settingspage = SettingsPage()
		self.settingspage.show()

	# reveals the create new collection page
	def show_new_collection_page(self):
		self.newcollectionpage = NewCollectionPage()
		self.newcollectionpage.show()