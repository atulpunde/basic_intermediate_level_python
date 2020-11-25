#img = Image.open(path)	 
# On successful execution of this statement, 
# an object of Image type is returned and stored in img variable) 

from tkinter import *
from PIL import Image

top = Tk()
top.geometry("500x500")
top.title("Hiiiiiiii")

Label(top, text="How is Pic..?", font="Arial").place(x=20,y=20)

try: 
	img = Image.open('D://Sem 4//Python//Program Files//pic.jpg')
	img.show()
	print("Image Displayed.")
except IOError as e: 
	print(e)
print("Executed")
top.mainloop()
# Use the above statement within try block, as it can 
# raise an IOError if file cannot be found, 
# or image cannot be opened.
