from tkinter import *
from timeit import default_timer as timer 
from setupFunctions import randomSentence, findWordLengths
import random 

#INITALIZE WINDOW 
window = Tk()
window.title("Typing Test")
window.geometry("500x500")

#DEFINE FUNCTIONS 
def openNewWindow(fn): 
    def wrapper(*args):
        result = fn(*args)
        if result != -1: 
            newWindow = Toplevel()
            lbl_description1 = Label(master=newWindow, text="WPM: {}".format(result[0]))
            lbl_description2 = Label(master=newWindow, text="Accuracy: {}".format(result[1]))
            lbl_description1.grid(row=0, column=0, sticky=W)
            lbl_description2.grid(row=1, column=0, sticky=W)
        return result
    return wrapper

@openNewWindow
def checkAnswer(sentence, answer, start): 
    if len(sentence) == len(answer): 
        #Calculate time elapsed
        end = timer()
        time_elapsed = end - start 
        error = 0

        #Calculate error
        num_letters = len(sentence)
        for letter in range(num_letters): 
            if sentence[letter] != answer[letter]: 
                error += 1 

        #Calculate wpm and accuracy 
        length = len(sentence)
        wpm = length/5
        wpm = wpm - error 
        wpm = int(wpm / (time_elapsed / 60))
        accuracy = ((length - error) / length) * 100
        return (wpm, accuracy)
    else: 
        return -1

def displayNewSentence(): 
    sentence = randomSentence()
    txt_wordBox.config(state=NORMAL)
    txt_wordBox.delete("1.0", END)
    txt_wordBox.insert(INSERT, sentence)
    txt_wordBox.config(state=DISABLED)

def startTime(): 
    global start 
    if start == None: 
        start = timer()
        print("Time has started")

def selectWord(): 
    index, index1, index2 = 0, 0, 0
    word = ent_userInput.get()
    wordLengths = findWordLengths(sentence)
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
    

#DEFINE EVENT HANDLING FUNCTIONS
def entryReturnHandler(event): 
    print("The length of your answer is: ", len(ent_userInput.get()))
    print("The length of the sentence is: ", len(sentence))

    result = checkAnswer(sentence, ent_userInput.get(), start)
    if result != -1: 
        displayNewSentence()
        
def entryKeyHandler(event): 
    startTime()
    #selectWord()

#SETUP
sentence = randomSentence()
start = None 

#WORDBOX WIDGET 
txt_wordBox = Text(width=len(sentence), height=1)
txt_wordBox.insert(INSERT, sentence)
txt_wordBox.config(state=DISABLED)
txt_wordBox.grid(row=0, column=0, sticky=W)

#ENTRY BOX WIDGET 
ent_userInput = Entry(width=len(sentence) + 12)
ent_userInput.bind("<Key>", entryKeyHandler)
ent_userInput.bind("<Return>", entryReturnHandler)
ent_userInput.grid(row=1, column=0, sticky=W)
ent_userInput.focus_set()

window.mainloop()