from tkinter import Tk, Frame, Label, Button, Entry, CENTER, LEFT, RIGHT, W, E, X
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser
class Logo:
  def __init__(self,root):
    load = Image.open("labstep_logo.png")
    render = ImageTk.PhotoImage(load)
    logo = Label(root, image=render)
    logo.image = render
    logo.pack()

class WatchingMessage:
  def __init__(self, root):
    self.label = Label(root, text='Watching Folders For Data...')
    self.label.pack()

class Confirmation:
    def __init__(self, root, message, experiment):
      self.experiment = experiment
      self.frame = Frame(root)
      self.frame.pack(fill=X)
      self.label = Label(self.frame, text=message)
      self.label.pack()
      self.button = Button(self.frame, text="Open", command=self.open)
      self.button.pack()
      self.button = Button(self.frame, text="Dismiss", command=self.close)
      self.button.pack()

    def open(self):
      webbrowser.open(f'https://app.labstep.com/experiment-workflow/{self.experiment.id}/results', new=2)
      self.frame.pack_forget()

    def close(self):
      self.frame.pack_forget()
class ExperimentSelect:
  def __init__(self,form,experiment,onSelect):
    root = form.frame
    def onSelection():
      onSelect(self.experiment)
      root.pack_forget()
      Confirmation(form.root,'Data uploaded!', experiment)

    self.experiment = experiment
    self.frame = Frame(root)
    self.frame.pack(fill=X)
    self.label = Label(self.frame, text=experiment.name)
    self.label.pack(anchor=W, side=LEFT, fill=X)
    self.button = Button(self.frame, text="Select", command=onSelection)
    self.button.pack(anchor=E, side=RIGHT)

class ExperimentSelectForm:
    def __init__(self,root,experiments,onSelect):
      self.root = root
      self.frame = Frame(root)
      self.frame.pack()
      self.label = Label(self.frame, pady=10, text='File Detected! Please select an experiment to attach data to...')
      self.label.pack()
      for experiment in experiments:
        ExperimentSelect(self,experiment,onSelect)

class GUI:
  def __init__(self):
    self.window = Tk()
    self.window.title("Labstep Python App")
    self.window.geometry('600x400')
    Logo(self.window)
    WatchingMessage(self.window)

  def experimentSelect(self, experiments, onSelect):
    self.window.attributes('-topmost', True)
    self.window.attributes('-topmost', False)
    ExperimentSelectForm(self.window, experiments, onSelect)
    