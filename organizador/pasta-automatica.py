from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# pip install watchdog pra funcionar esses pacotes

import os
import json
import time

class MyHandler(FileSystemEventHandler):

  i = 1

  def on_modified(self, event):
    new_name = "nova_anotaçao_" + str(self.i) + ".txt"
    for filename in os.listdir(folder_to_track):
      file_exists = os.path.isfile(folder_destination + "/" + new_name)
      while file_exists:
        self.i += 1
        new_name = "nova_anotaçao_" + str(self.i) + ".txt"
        file_exists = os.path.isfile(folder_destination + "/" + new_name)

      src = folder_to_track + "/" + filename
      new_destination = folder_destination + "/" + new_name
      os.rename(src, new_destination)

folder_to_track = "C:/Users/ema29/Desktop/Auto"
folder_destination = "C:/Users/ema29/Desktop/pastaNova"

event_handler = MyHandler()
Observer = Observer()
Observer.schedule(event_handler, folder_to_track, recursive=True)
Observer.start()

try:
  while True:
    time.sleep(10)
except KeyboardInterrupt:
  Observer.stop()
Observer.join()
