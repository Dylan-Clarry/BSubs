from Homepage import Homepage
from SettingsPage import SettingsPage

class Navigator:

	# reveals the homepage
	def show_homepage(self):
		self.homepage = Homepage()
		self.homepage.switch_window.connect(self.show_settingspage)
		self.homepage.show()
	
	# reveals the settings page
	def show_settingspage(self):
		self.settingspage = SettingsPage()
		self.settingspage.show()