from tkinter import * 
from tkinter import font 
from tkinter import messagebox
from functions import randomSentence, findWordLengths, checkAnswer
from timeit import default_timer as timer 

#DECORATORS 
def startTime(fn): 
    def wrapper(*args): 
        result = fn(*args)
        fn.inital = True 
        if fn.inital == True: 
            fn.start = timer()
            fn.inital = False 
        return result 
    return wrapper 

@startTime
def selectedWord(event, wordLengths): 
    global index1
    global index2 
    global index

    word = ent_userInput.get()
    numWords = len(wordLengths)
    userInput = ""
    
    if len(word) + 1 > wordLengths[index] and index < numWords - 1: 
        index += 1 
        index1 = index1 + wordLengths[index] + 1
        index2 = index2 + wordLengths[index] + 1
        userInput += ent_userInput.get()
        ent_userInput.delete(0, END)
        print("")
        
    if len(word) + 1 > wordLengths[index] and index == numWords - 1: 
        userInput += ent_userInput.get()
        ent_userInput.delete(0, END)
        #checkAnswer(sentence, userInput, selectedWord.start)


#GLOBAL VARIABLES
# inital = True
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