from tkinter import Tk, Frame, Label, Button, Entry, CENTER, LEFT, RIGHT, W, E, X
from tkinter import messagebox
from PIL import Image, ImageTk

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

class ExperimentSelect:
  def __init__(self,root,experiment,onSelect):

    def onSelection():
      onSelect(self.experiment)
      root.pack_forget()
      #messagebox.showinfo('Data Uploaded!',f'Data uploaded to https://app.labstep.com/experiment-workflow/{self.experiment.id}')

    self.experiment = experiment
    self.frame = Frame(root)
    self.frame.pack(fill=X)
    self.label = Label(self.frame, text=experiment.name)
    self.label.pack(anchor=W, side=LEFT, fill=X)
    self.button = Button(self.frame, text="Select", command=onSelection)
    self.button.pack(anchor=E, side=RIGHT)

class ExperimentSelectForm:
    def __init__(self,root,experiments,onSelect):
      self.frame = Frame(root)
      self.frame.pack()
      self.label = Label(self.frame, pady=10, text='File Detected! Please select an experiment to attach data to...')
      self.label.pack()
      for experiment in experiments:
        ExperimentSelect(self.frame,experiment,onSelect)

class GUI:
  def __init__(self):
    self.window = Tk()
    self.window.title("Labstep Python App")
    self.window.geometry('600x400')
    Logo(self.window)
    WatchingMessage(self.window)

  def experimentSelect(self, experiments, onSelect):
    ExperimentSelectForm(self.window, experiments, onSelect)
    