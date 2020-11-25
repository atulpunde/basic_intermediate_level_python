# importing only those functions 
# which are needed 
from tkinter import *
from tkinter.ttk import *

# creating tkinter window 
root = Tk() 

# Creating button. In this destroy method is passed 
# as command, so as soon as button 1 is pressed root 
# window will be destroyed 
btn1 = Button(root, text ="Button 1") 
btn1.pack(pady = 10) 
btn1.after(3000, btn1.destroy) 
root = Tk() 
# Creating button. In this destroy method is passed 
# as command, so as soon as button 2 is pressed 
# button 1 will be destroyed 
btn2 = Button(root, text ="Button 2") 
btn2.pack(pady = 10) 
btn2.after(6000, btn2.destroy) 
root = Tk() 
btn3 = Button(root, text ="Button 33") 
btn3.pack(pady = 10) 
btn3.after(9000, btn3.destroy) 
root = Tk() 
btn4 = Button(root, text ="Button 44") 
btn4.pack(pady = 10) 

btn4.after(12000, btn4.destroy) 
root = Tk() 
btn5 = Button(root, text ="Button 55") 
btn5.pack(pady = 10) 

# after method destroying button-1 
# and button-2 after certain time 



btn5.after(16000, btn5.destroy) 

# infinite loop 
mainloop() 
