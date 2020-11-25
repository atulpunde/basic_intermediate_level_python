from tkinter import * 

window = Tk()

window.geometry("500x500")

frame = Frame(window)
frame.pack()

#### FRAME
lframe = Frame(window)
lframe.pack(side=LEFT)

lframe = Frame(window)
lframe.pack(side=RIGHT)

lframe = Frame(window)
lframe.pack(side=TOP)

b1 = Button(frame,text="Submit")
b1.pack(side=LEFT)

b1 = Button(frame,text="login")
b1.pack(side=TOP)

b1 = Button(window,text="ok")
b1.pack(side=RIGHT)

window.mainloop()