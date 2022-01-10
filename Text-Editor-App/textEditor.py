from tkinter import * 
from tkinter import filedialog
from tkinter import font 

window = Tk()
window.title("Text Editor")
window.geometry("1200x660")

#Frame 
mainFrame = Frame(window)
mainFrame.pack(pady=10)

#Scrollbar 
text_scroll = Scrollbar(mainFrame)
text_scroll.pack(side=RIGHT, fill=Y)

#Text 
mainText = Text(mainFrame, width=100, height=25, font=("Helvetica", 16), selectbackground="blue", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
mainText.pack()

text_scroll.config(command=mainText.yview)

#Menu
mainMenu = Menu(window)
window.config(menu=mainMenu)

#File Menu 
fileMenu = Menu(mainMenu, tearoff=False)
fileMenu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New")
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Save")
fileMenu.add_separator()
fileMenu.add_command(label="Exit")

#Edit Menu
editMenu = Menu(mainMenu, tearoff=False)
editMenu.add_cascade(label="Cut")
editMenu.add_cascade(label="Copy")
editMenu.add_cascade(label="Undo")
editMenu.add_cascade(label="Redo")

#Status Bar
statusBar = Label(window, text="Ready... ", anchor=E)
statusBar.pack(fill=X, side=BOTTOM, ipady=5)



window.mainloop()