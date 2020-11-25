##from tkinter import * 
##top = Tk()
##text = Text(Top)
##text.insert(INSERT,"Mytext")
##text.pack()
##top.mainloop()

##from tkinter import *
## 
##window = Tk()
## 
##window.title("Welcome to LikeGeeks app")
## 
##window.mainloop()

##from tkinter import *
## 
##window = Tk()
## 
##window.title("Welcome to LikeGeeks app")
## 
##window.geometry('350x200')
## 
##lbl = Label(window, text="Hello")
## 
##lbl.grid(column=0, row=0)
## 
##btn = Button(window, text="Click Me")
## 
##btn.grid(column=1, row=0)
## 
##window.mainloop()

##from tkinter import messagebox
##
##messagebox.showinfo("Title", "a Tk MessageBox")

##from tkinter import tkMessageBox
##import tkMessageBox
##
##tkMessageBox.showinfo("Title", "a Tk MessageBox")
#_____________________________________________________________
import tkinter
from tkinter import messagebox

# hide main window
root = tkinter.Tk()
root.withdraw()

j=1
# message box display
i = int(input("Enter Input = "))
if i==j:
    messagebox.showerror("Error", "Error message Positive values")
messagebox.showwarning("Warning","Warning message")
messagebox.showinfo("Information","Informative message")
root.mainloop() 






