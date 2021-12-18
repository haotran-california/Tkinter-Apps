from tkinter import * 
from functions import SignIn, CreateAccount, Input, intializeDataTable, Input
from app import openApp

window = Tk()
window.title("Mason's Application")

def openAppWindow(): 
    state = SignIn(ent_username.get(), ent_password.get())
    if state: 
        window.quit
        openApp()
    else: 
        return 0

#USER LOGIN TAB
frmLogin = Frame(width = 500, height = 500)
frmLogin.pack(fill="both", expand=True)

lbl_username = Label(frmLogin, text = "Username")
lbl_password = Label(frmLogin, text = "Password")

ent_username = Entry(frmLogin)
ent_password = Entry(frmLogin, show="*")

btn_SignIn = Button(frmLogin, text="Sign In", command=openAppWindow)
btn_CreateAccount = Button(frmLogin, text="Create Account", command= lambda: CreateAccount(ent_username.get(), ent_password.get()))
btn_Exit = Button(frmLogin, text = "Exit", command = window.quit)

lbl_username.grid(row = 0, column = 0)
lbl_password.grid(row = 1, column = 0)

ent_username.grid(row = 0, column = 1)
ent_password.grid(row = 1, column = 1)

btn_SignIn.grid(row = 3, column= 0)
btn_CreateAccount.grid(row = 3, column= 1)
btn_Exit.grid(row = 3, column= 2)

window.mainloop()