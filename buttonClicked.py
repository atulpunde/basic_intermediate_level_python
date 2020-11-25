from tkinter import * 
from tkinter import messagebox
  
window = Tk()  
  
window.geometry("300x300")  
  
def Red():  
    messagebox.showinfo("Hello", "Red Button clicked")

def Blue():  
    messagebox.showinfo("Hello", "Blue Button clicked")

def Green():  
    messagebox.showinfo("Hello", "Green Button clicked")

def Yellow():  
    messagebox.showinfo("Hello", "Yellow Button clicked")  
  
  
b1 = Button(window,text = "Red",command = Red,activeforeground = "red",activebackground = "pink",pady=10).pack(side = LEFT)
  
b2 = Button(window, text = "Blue",command = Blue,activeforeground = "blue",activebackground = "pink",pady=10).pack(side = RIGHT)
  
b3 = Button(window, text = "Green",command = Green,activeforeground = "green",activebackground = "pink",pady = 10).pack(side = BOTTOM)
  
b4 = Button(window, text = "Yellow",command = Yellow,activeforeground = "yellow",activebackground = "pink",pady = 10).pack(side = TOP) 
  
window.mainloop()  