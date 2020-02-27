from tkinter import Tk, Frame, Label, Button, Entry, CENTER
from tkinter import messagebox
from PIL import Image, ImageTk
from users import users
import labstep
# user = labstep.login('test@labstep.com','testpass')

class Logo:
  def __init__(self,root):
    load = Image.open("labstep_logo.png")
    render = ImageTk.PhotoImage(load)
    logo = Label(root, image=render)
    logo.image = render
    logo.pack()

class Waiting:
  def __init__(self, root):
    self.label = Label(root, text='Watching Folders For Data...')
    self.label.pack()

class ExperimentSelect:
  def __init__(self,root,experiment,onSelect):
    self.experiment = experiment
    self.label = Label(root, text=experiment.name)
    self.label.pack()
    self.button = Button(root,text="Select",command=lambda :onSelect(self.experiment))
    self.button.pack()

class App:
  def __init__(self):
    self.window = Tk()
    self.window.title("Labstep Python App")
    self.window.geometry('200x400')
    self.waiting = Waiting(self.window)

  def experimentSelect(self, experiments, onSelect):
    self.waiting.label.pack_forget()
    for experiment in experiments:
      ExperimentSelect(self.window,experiment,onSelect)

  def start(self):
    self.window.mainloop()
