from tkinter import *
from tkinter import messagebox

window =Tk()
window.geometry("800x500")
# window.title("")

messagebox.showerror("Error","This is Error..")

messagebox.showinfo("My Info","This is Info..")

messagebox.showwarning("Warning","This is Warning..")

messagebox.askquestion("Confirm","Are you sure.?")

messagebox.askokcancel("Redirect","Redirecting to new page.?")

messagebox.askyesno("Application","Got ")

messagebox.askretrycancel("Application","try again?")  



window.mainloop()