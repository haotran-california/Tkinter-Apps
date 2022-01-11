from tkinter import * 
from tkinter import filedialog
from tkinter import font 

window = Tk()
window.title("Text Editor")
window.geometry("1200x660")

#DEFINE COMANDS
def newFile(): 
    mainText.delete("1.0", END)
    window.title("New File")
    statusBar.config(text="New File  ")

def openFile(): 
    mainText.delete("1.0", END)
    textFile = filedialog.askopenfilename(initialdir="C:/", title="Open File", filetypes=(("Text Files", "*.txt"), ("Python Files", "*.py"), ("All Files", ("*."))))

    #Update Status Bars
    name = textFile
    statusBar.config(text=f'{name}')
    name = name.replace("C:/gui/", "")
    window.title(f'{name} - Textpad')

    #Open file 
    textFile = open(textFile, 'r')
    text = textFile.read()
    mainText.insert(END, text)
    textFile.close()

def saveFile(): 
    return 0

def saveFileAs(): 
    textFile = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/", title="Save File", filetypes=(("Text Files", "*.txt"), ("Python Files", "*.py"), ("All Files", ("*."))))
    if textFile: 
        #Update status bars
        name = textFile
        name = name.replace("C:/", "")
        statusBar.config(text=f'Saved: {name}')
        window.title(f'{name} - Textpad')

        #Save file 
        textFile = open(textFile, 'w')
        textFile.write(mainText.get("1.0", END))
        textFile.close()

# def copyEdit(): 
#     return 0

# def cutEdit(): 
#     return 0

# def undoEdit(): 
#     return 0

# def redoEdit(): 
#     return 0

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
mainMenu.add_cascade(label="File", menu=mainMenu)
fileMenu.add_command(label="New", command=newFile)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_command(label="Save As", command=saveFileAs)
fileMenu.add_separator()
fileMenu.add_command(label="Exit")

#Edit Menu
editMenu = Menu(mainMenu, tearoff=False)
mainMenu.add_cascade(label="Edit", menu=mainMenu)
editMenu.add_command(label="Cut")
editMenu.add_command(label="Copy")
editMenu.add_command(label="Undo")
editMenu.add_command(label="Redo")

#Status Bar
statusBar = Label(window, text="Ready        ", anchor=E)
statusBar.pack(fill=X, side=BOTTOM, ipady=5)

window.mainloop()