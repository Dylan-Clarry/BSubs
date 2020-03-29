import sys
sys.path.insert(0, './decorators')

from Singleton import Singleton

@Singleton
class Settings:

   __name = 'bob'
   __lastname = 'george'

   def __init__(self):
      print('Settings created')

   def sayhello(self):
      print('hi ' + self.__name + ' ' + self.__lastname + '.')

# create settings singleton object
settings = Settings.instance()
