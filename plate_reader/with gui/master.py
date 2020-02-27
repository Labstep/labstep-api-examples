from folderWatcher import FolderWatcher
from users import users
from analysis import analyzeData
from api import attachDataToExistingExperiment, getExperiments
from gui import App

app = App()

def onNewFile(filepath):
  analyzeData(filepath)
  experiments = getExperiments()
  app.experimentSelect(experiments,attachDataToExistingExperiment)

FolderWatcher(users[0]['folder'],onNewFile).run()

app.start()
