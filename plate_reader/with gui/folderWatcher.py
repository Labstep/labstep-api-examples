import sys
import time

from watchdog.observers import Observer
from watchdog.events import RegexMatchingEventHandler

class EventHandler(RegexMatchingEventHandler):

    def __init__(self, onNewFile):
        super().__init__([r".*\.csv$"])
        self.onNewFile = onNewFile

    def on_created(self, event):
        print(f'file detected at{event.src_path}')
        self.onNewFile(event.src_path)

      
class FolderWatcher:
    def __init__(self, folder_path, onCreate):
        self.__folder_path = folder_path
        self.__event_handler = EventHandler(onCreate)
        self.__event_observer = Observer()

    def run(self):
        self.start()
        print(f'Watching folder {self.__folder_path}')
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

    def start(self):
        self.__schedule()
        self.__event_observer.start()

    def stop(self):
        self.__event_observer.stop()
        self.__event_observer.join()

    def __schedule(self):
        self.__event_observer.schedule(
            self.__event_handler,
            self.__folder_path,
            recursive=True
        )