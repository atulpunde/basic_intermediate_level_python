#indices listbox (end :denote end of listbox)
#if you give number :it specifies 
#active it indicate element that have cursor location 
# this ele is displyaed with underline when listbox has keyword focus
#lstbox (active)
#ACTIVE it return selected element
#lambda listbox = listbox:lstbox.delete(ANCHOR)
#lambda listbox = listbox:lstbox.delete(0,END)
#radio button you can show multiple button you can select one ata a time 

import tkinter
from tkinter import ANCHOR
from tkinter import ACTIVE
from tkinter import END
from tkinter import messagebox
import re

window =tkinter.Tk()
window.geometry("800x500")
window.title("Login page")

def getUserPswd():
    lb.insert(tkinter.END,(user.get()).strip().capitalize())
    user.delete(0,tkinter.END)
    pswd.delete(0,tkinter.END)


    # if (user.get()).strip()=="" or (user.get()).strip()==" ":
    #     messagebox.showerror("Error","User Name Can Not Be Empty..")
    # elif (pswd.get()).strip()=="" or (pswd.get()).strip()==" ":
    #     messagebox.showerror("Error","Password Can Not Be Empty..")
    # elif re.search("[0-9]",user.get()):
    #     messagebox.showerror("Error","Invalid Username.")
    # elif len(pswd.get())<6:
    #     messagebox.showerror("Error","Password is too short.")
    # elif not(re.search("[a-z]",pswd.get()) and re.search("[A-Z]",pswd.get()) and re.search("[0-9]",pswd.get())):
    #     messagebox.showinfo("Error","Password Must Contain \n\t1) Integer,\n\t2)Upper Case And \n\t3)Lower Case Letters.")
    # else:
    #     lb.insert(tkinter.END,(user.get()).strip().capitalize())
    #     user.delete(0,tkinter.END)
    #     pswd.delete(0,tkinter.END)

# def DeleteOne():
    

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
print(lb.get(ACTIVE))
b1 = tkinter.Button(window,text = "Login",font=("Times New Roman",20),command=getUserPswd,fg="White",bg="Blue",padx=80).place(x=110,y=200)

d1 = tkinter.Button(window,text = "Delete",font=("Times New Roman",20),command=lambda lb=lb:lb.delete(ANCHOR),fg="White",bg="Blue",padx=80).place(x=110,y=300)

d1 = tkinter.Button(window,text = "Delete ALL",font=("Times New Roman",20),command=lambda lb=lb:lb.delete(0,END),fg="White",bg="Blue",padx=80).place(x=110,y=400)

window.mainloop()