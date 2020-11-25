##import tkinter

from tkinter import *

##window = tkinter.Tk()
window = Tk()
window.title("login")
# Tk class is instantiated without args ,this create top level widget of Tk which use as main window of appln
# each instance has its own associated tcl interpreter

window.geometry("600x600")
# #we can set default window size using above fun

# # Label(window,text='Login Form ',font='Arial').grid(row=1,column=5)
# # Label(window,text='Username :',font='Arial').grid(row=2)
# # Label(window,text='Password :',font='Arial').grid(row=3)
# Label(window,text='Login Form ',font='Arial').pack()
# Label(window,text='Username :',font='Arial').pack()
# Label(window,text='Password :',font='Arial').pack()

# # Entry().grid(row=2,column=2)
# # Entry().grid(row=3,column=2)

# window.mainloop()
#____________________________________________________________________________
# window.geometry("600x600")
# var = StringVar()
# label = Label(window,textvariable=var,relief=RAISED)      #gives border to label
# # label = Label(window,textvariable=var)      #no border to label

# var.set("Hey..how are you doing..")
# label.pack()
# window.mainloop()
#_____________________________________________________________________________

# Label(window,text='Login Form ',font='Arial').grid(row=1,column=5)
# Label(window,text='Username :',font='Arial').grid(row=2)
# Label(window,text='Password :',font='Arial').grid(row=3)

# Label(window,text='Login Form ',font='Arial').pack()
# username = Label(window,text='Username :',font='Arial').place(x=30,y=60)
# Label(window,text='Password :',font='Arial').place(x=30,y=100)

# # Entry().grid(row=2,column=2)
# # Entry().grid(row=3,column=2)
# e1 = Entry(window,width=20).place(x=150,y=70)
# e2 = Entry(window,width=20).place(x=150,y=110)

# submitbtn = Button(window,text="Submit",foreground='red',background='yellow').place(x=150,y=150)
# # submitbtn.place(x=150,y=150)

b1 = Button(window,text="button 1",foreground='red',padx=15,background='yellow').place(x=150,y=40)
b2 = Button(window,text="button 2",foreground='red',padx=15,background='yellow').place(x=80,y=80)
b3 = Button(window,text="button 3",foreground='red',padx=15,background='yellow').place(x=220,y=80)
b4 = Button(window,text="button 4",foreground='red',padx=15,background='yellow').place(x=150,y=120)

window.mainloop()

