import tkinter
from tkinter import messagebox
import re

window =tkinter.Tk()
window.geometry("800x500")
window.title("Login page")

def getUserPswd():
    uname = user.get().strip()
    passwd = pswd.get().strip()

    if uname =="" or uname ==" ":
        messagebox.showerror("Error","User Name Can Not Be Empty..")
    elif passwd =="" or passwd ==" ":
        messagebox.showerror("Error","Password Can Not Be Empty..")
    elif re.search("[0-9]",uname):
        messagebox.showerror("Error","Invalid Username.")
    elif len(passwd)<6:
        messagebox.showerror("Error","Password is too short.")
    elif not(re.search("[a-z]",passwd) and re.search("[A-Z]",passwd) and re.search("[0-9]",passwd)):
        messagebox.showinfo("Error","Password Must Contain \n\t1) Integer,\n\t2)Upper Case And \n\t3)Lower Case Letters.")
    else:
        lb.insert(tkinter.END,uname)
        user.delete(0,tkinter.END)
        pswd.delete(0,tkinter.END)

tkinter.Label(window,text="USER LOGIN",font=("Times New Roman",20),bg="Light Green",padx=50).place(x=110,y=20)

tkinter.Label(window,text="User Id:",font="Arial").place(x=110,y=80)
user = tkinter.Entry(window)
user.place(x=215,y=85)

tkinter.Label(window,text="Password:",font="Arial").place(x=110,y=140)
pswd = tkinter.Entry(window,show="*")
pswd.place(x=215,y=145)

label1 = tkinter.Label(window,text="Student List:",font=("Times New Roman",20))
label1.place(x=450,y=15)

lb = tkinter.Listbox(window,font="Arial",highlightcolor="Black",highlightthickness=10,selectmode="extended",fg="blue",bd=15)
lb.place(x=450,y=50)

b1 = tkinter.Button(window,text = "Login",font=("Times New Roman",20),command=getUserPswd,fg="White",bg="Blue",padx=80).place(x=110,y=200)

window.mainloop()