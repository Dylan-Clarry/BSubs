from pages.Homepage import Homepage
from pages.SettingsPage import SettingsPage

class Navigator:

	# reveals the homepage
	def show_homepage(self):
		self.homepage = Homepage()
		self.homepage.sig_settings.connect(self.show_settingspage)
		self.homepage.show()
	
	# reveals the settings page
	def show_settingspage(self):
		self.settingspage = SettingsPage()
		self.settingspage.show()