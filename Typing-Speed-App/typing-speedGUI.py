from tkinter import *
from timeit import default_timer as timer 
from setupFunctions import randomSentence, findWordLengths
import random 

#INITALIZE WINDOW 
window = Tk()
window.title("Typing Test")
window.geometry("500x500")

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

#DEFINE EVENT HANDLING FUNCTIONS
def entryReturnHandler(event): 
    print("The length of your answer is: ", len(ent_userInput.get()))
    print("The length of the sentence is: ", len(sentence))

    result = checkAnswer(sentence, ent_userInput.get(), start)
    if result != -1: 
        displayNewSentence()
        
    # print(result[0])
    # print(result[1])

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
    txt_wordBox.config(text=sentence)
    txt_wordBox.config(state=DISABLED)


    


def entryKeyHandler(event): 
    startTime()
    #erase words after typing

def startTime(): 
    global start 
    if start == None: 
        start = timer()
        print("Time has started")


#SETUP
sentence = randomSentence()
wordLength = findWordLengths(sentence)
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