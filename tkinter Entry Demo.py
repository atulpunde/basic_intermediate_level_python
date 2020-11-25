from tkinter import *
import re
window = Tk()
window.geometry("500x500")

window.title("Entry Demo")

def clicks():
    if (e1.get()).strip() == "" or (e1.get()).strip() == " ":
        print("Space...")
    else:
        if re.search("[0-9]",e1.get()):
            print("int :",e1.get())
        elif re.search("[a-z]",e1.get()) and re.search("[A-Z]",e1.get()):
            print("small and u")
        # elif re.search("[A-Z]",e1.get()):
        #     print("upper")
        elif re.search("[^0-9a-zA-Z*]",e1.get()):
            print("sp char")
        else:
            print("other")


e1 = Entry(window)
e1.place(x=20,y=30)
# print(e1.get())
Button(window,text="Click me",command=clicks).place(x=20,y=60)
window.mainloop()
