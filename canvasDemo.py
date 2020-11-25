
from tkinter import *

window =Tk()
window.geometry("800x500")
window.title("Canvas Demo")

c = Canvas(window,bg="Pink",height=200)

arc = c.create_arc((15,10,150,200),start=10,extent=90,fill="White")

c.place(x=100,y=100)
window.mainloop()