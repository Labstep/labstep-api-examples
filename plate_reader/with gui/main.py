from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from queue import Queue
import labstep
from gui import GUI
from users import users
from analysis import analyzeData
from api import attachData

class CustomHandler(FileSystemEventHandler):
    def __init__(self, app, lsUser):
        FileSystemEventHandler.__init__(self)
        self.app = app
        self.user = lsUser
    def on_created(self, event):
        app.notify(event, self.user)

class App(object):
    def __init__(self):
        self.observers = []

        for user in users:
          path = user['folder']
          lsUser = labstep.authenticate(user['username'], user['apikey'])
          handler = CustomHandler(self,lsUser)
          observer = Observer()
          observer.schedule(handler, path, recursive=True)
          observer.start()
          self.observers.append(observer)

        self.queue = Queue()
        self.gui = GUI()
        self.gui.window.bind("<Destroy>", self.shutdown)
        self.gui.window.bind("<<WatchdogEvent>>", self.handle_watchdog_event)

    def handle_watchdog_event(self, event):
        """Called when watchdog posts an event"""
        watchdog_event = self.queue.get()
        print("event type:", type(watchdog_event))
        filepath = watchdog_event.src_path
        print(f'file detected at{filepath}')
        ## Get Experiments and Display List
        experiments = self.activeUser.getExperiments(count=5)
        ## Do Analysis
        analyzeData(filepath)
        ## Do Labstep Stuff
        self.gui.experimentSelect(experiments,attachData)

    def shutdown(self, event):
        """Perform safe shutdown when GUI has been destroyed"""
        for observer in self.observers:
          observer.stop()
          observer.join()

    def start(self):
        """Start the GUI loop"""
        self.gui.window.mainloop()

    def notify(self, event, user):
        """Forward events from watchdog to GUI"""
        self.queue.put(event)
        self.activeUser = user
        self.gui.window.event_generate("<<WatchdogEvent>>", when="tail")

app = App()
app.start()