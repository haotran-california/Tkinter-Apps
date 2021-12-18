from tkinter import * 
from tkinter import ttk 
from functions import Input 

def openApp(): 
    #CREATE TOP LEVEL 
    app = Toplevel()

    #CREATE TABS 
    notebook = ttk.Notebook(app)
    notebook.pack(pady=15)

    frm2 = Frame(notebook, width = 500, height = 500)
    frm3 = Frame(notebook, width = 500, height = 500)
    frm4 = Frame(notebook, width = 500, height = 500)

    frm2.pack(fill="both", expand=True)
    frm3.pack(fill="both", expand=True)
    frm4.pack(fill="both", expand=True)

    notebook.add(frm2, text="Upload File")
    notebook.add(frm3, text="Tab 3")
    notebook.add(frm4, text="Tab 4")
    
    #FILE PARSING TAB
    canvas = Canvas(frm2, width = 100, height = 100, bg="white")
    btn_Input = Button(frm2, text="Input", command=Input)
    btn_Exit = Button(frm2, text="Exit", command=app.withdraw)

    canvas.grid(row = 0, column = 0)
    btn_Input.grid(row = 1, column = 0)
    btn_Exit.grid(row = 1, column= 1)

    #TAB 3 
    lbl = Label(frm3, text="This is an empty tab for now")
    lbl.grid(row = 0, column=0)

    #TAB 4
    lbl1 = Label(frm4, text="This is an empty tab for now")
    lbl1.grid(row = 0, column=0)

