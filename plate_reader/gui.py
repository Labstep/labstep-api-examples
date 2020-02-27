from tkinter import Tk, Frame, Label, Button, Entry, CENTER
from tkinter import messagebox
from PIL import Image, ImageTk
from users import users
import labstep
# user = labstep.login('test@labstep.com','testpass')


class NewExperimentForm:
  def __init__(self,root, user):
    self.user = user
    self.frame = Frame(root, width=100, height=50, pady=50,padx=50)
    self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    Logo(self.frame)
    self.experiment_id = LabelledInput(self.frame, 'Experiment ID')
    self.submit_button = Button(self.frame, text="Select Experiment", command=self.action)
    self.submit_button.pack()

  def action(self):
    print('Did stuff')


class Logo:
  def __init__(self,root):
    load = Image.open("labstep_logo.png")
    render = ImageTk.PhotoImage(load)
    logo = Label(root, image=render)
    logo.image = render
    logo.pack()

class LabelledInput:
  def __init__(self,root,name):
    self.label = Label(root, text=name)
    self.label.pack()
    self.input = Entry(root,width=20)
    self.input.pack()
  
  def get(self):
    return self.input.get()

class UserSelect:
  def __init__(self,root,user,onSelect):
    self.user = user
    self.label = Label(root, text=user['username'])
    self.label.pack()
    self.button = Button(root,text="Select",command=lambda :onSelect(self.user))
    self.button.pack()

class LoginForm:
  def __init__(self,root,onSuccess):
    self.onSuccess = onSuccess
    # Define and place the frame for the login form
    self.frame = Frame(root, width=100, height=50, pady=10,padx=10)
    self.frame.place(relx=0, rely=0)
    # Place the labstep logo
    Logo(self.frame)
    label = Label(self.frame, text='Select user')
    label.pack()

    for user in users:
      UserSelect(self.frame,user,self.onSelect)
    

  # Function that runs when user hits enter
  def onSelect(self,user):
    self.frame.place_forget() # hide login frame
    lsUser = labstep.authenticate(user['username'],user['api-key'])
    messagebox.showinfo('Login Success', f'You have successfully authenticated as {lsUser.first_name} {lsUser.last_name}')
    self.onSuccess(user)


class App:
  def __init__(self):
    self.window = Tk()
    self.window.title("Labstep Python App")
    self.window.geometry('200x400')
    self.login()

  def main(self,user):
    NewExperimentForm(self.window,user)

  def login(self):
    LoginForm(self.window,self.main)

  def start(self):
    self.window.mainloop()
