from tkinter import * 
from tkinter import font 
from tkinter import messagebox
from timeit import default_timer as timer 
from functions import randomSentence, findWordLengths, checkAnswer
        
def selectedWord(event, wordLengths): 
    global index1
    global index2 
    global index
    global start 
    global inital

    #initalize start time 
    if inital == True: 
        start = timer()
        inital = False

    word = ent_userInput.get()
    numWords = len(wordLengths)
    userInput = ""
    
    if len(word) + 1 > wordLengths[index] and index < numWords - 1: 
        index += 1 
        index1 = index1 + wordLengths[index] + 1
        index2 = index2 + wordLengths[index] + 1
        userInput += ent_userInput.get()
        ent_userInput.delete(0, END)
        
    if len(word) + 1 > wordLengths[index] and index == numWords - 1: 
        userInput += ent_userInput.get()
        ent_userInput.delete(0, END)
        checkAnswer(sentence, userInput)

    highlightWord(index1, index2)
    bolder()


def highlightWord(index1, index2): 
    #sliding grey background 
    txt_wordBox.config(state=NORMAL)

    # txt_wordBox.tag_delete("sel")
    # txt_wordBox.tag_delete("bold")
    txt_wordBox.tag_add("sel", "1." + str(index1), "1." + str(index2))
    txt_wordBox.config(state=DISABLED)
    


def bolder(): 
    #font definition 
    bold_font = font.Font(txt_wordBox, txt_wordBox.cget("font"))
    bold_font.config(weight = "bold")

    #configure tag 
    txt_wordBox.tag_configure("bold", font=bold_font)
    current_tags = txt_wordBox.tag_names("sel.first")

    #bold and unbold logic 
    if "bold" in current_tags: 
        txt_wordBox.tag_remove("bold", "sel.first", "sel.last")
    else: 
        txt_wordBox.tag_add("bold", "sel.first", "sel.last")

#GLOBAL VARIABLES
inital = True
index, index1, index2 = 0, 0, 0

#INITALIZE WINDOW 
window = Tk()
window.title("Typing Test")
window.geometry("500x500")

#SETUP FUNCTIONS
sentence = randomSentence()
wordLength = findWordLengths(sentence)

#WORDBOX WIDGET 
txt_wordBox = Text(width=len(sentence), height=1)
txt_wordBox.insert(INSERT, sentence)
txt_wordBox.grid(row = 0, column=0)

#ENTRY BOX WIDGET 
ent_userInput = Entry(width=len(sentence) + 12)
ent_userInput.bind("<Key>", lambda event: selectedWord(event, wordLength))
ent_userInput.bind("<Return>", checkAnswer)
ent_userInput.grid(row = 1, column=0)
ent_userInput.focus_set()

window.mainloop()