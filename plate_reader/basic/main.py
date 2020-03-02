from folderWatcher import FolderWatcher
from users import users
from analysis import analyzeData
from api import uploadDataToLabstep

for user in users:

  def onNewFile(filepath):
    analyzeData(filepath)
    uploadDataToLabstep(user)

  FolderWatcher(user['folder'],onNewFile).run()

