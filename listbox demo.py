from tkinter import *
top = Tk()
top.geometry("500x500")
top.title("ListBox Demo")

label1 = Label(top,text="Student List:",font="Arial")
label1.place(x=250,y=15)

lb = Listbox(top,font="Arial",height=10,width=10,highlightcolor="Yellow",highlightthickness=10,fg="blue")
lb.place(x=250,y=50)
lb.insert(1,"Ajit")
lb.insert(2,"Amit")
lb.insert(3,"Arjit")
lb.insert(4,"Abhi")

# lb.pack()
top.mainloop()