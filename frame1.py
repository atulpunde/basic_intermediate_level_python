from tkinter import * 

window = Tk()

window.geometry("500x500")

def UserPswdValidation():
    user = uname.get("1.0",END)
    password = pswd.get("1.0",END)
    print("User : ",user)
    print("Password : ",password) 

    valid =True
    for i in user:
        if i.isdigit():
            valid=False
            break
    if valid==False:
        print("Invalid input")  
    else:
        print("Valid Input")

    valid1 =True
    valid2 =True
    for i in password:
        if i.isdigit():
            valid1=False
            break
        elif i.isalpha():
            valid2=False
            break
        # else:
        #     valid1=True
        #     valid2=True
    if valid1==True and valid2==True:
        print("Invalid input..") 
    else:
        print("Valid Input..")
'''
    if user.strip()=="" or user.strip()==" " or password.strip()=="" or password.strip()==" ":
        print("Field can not empty.")
    # else:
    #     print("Invalid")

    
    elif digit in user.isdigit()
    :
         print("InValid....")
    else:
        print("8888")
    # elif password.isalpha():
    #     print("Invalid !!")
    # else:
    #     print("valid")
'''

    
frame = Frame(window,bg="Light Blue")
frame.pack()

label1 = Label(frame,text="Username: ",bg="Light Blue",font="Arial")
label1.grid(row=2,column=4)

label1 = Label(frame,text="Password: ",bg="Light Blue",font="Arial")
label1.grid(row=3,column=4)

uname = Text(frame,height=1,width=20)
uname.grid(row=2,column=5)



pswd = Text(frame,height=1,width=20)
pswd.grid(row=3,column=5)

chbox = Checkbutton(frame,text="Keep me logged in",bg="Light Blue",font="Arial")
chbox.grid(row=4,column=4)

submitbtn = Button(frame,text="Submit",font="Arial",command=UserPswdValidation,bg="light green")
submitbtn.grid(row=5,column=4)

submitbtn = Button(frame,text="Cancel",font="Arial",bg="light green")
submitbtn.grid(row=5,column=5)

window.mainloop()