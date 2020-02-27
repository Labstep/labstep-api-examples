from folderWatcher import FolderWatcher
from users import users
from analysis import analyzeData
from api import attachDataToNewExperiment
#from gui import App

def onNewFile(filepath):
  # App().start()
  analyzeData(filepath)
  attachDataToNewExperiment()

FolderWatcher(users[0]['folder'],onNewFile).run()