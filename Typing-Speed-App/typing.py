from tkinter import * 
from tkinter import font 
from tkinter import messagebox
from timeit import default_timer as timer 
import random

# def randomSentence(): 
#     file = open("sentence.txt", "r")
#     sentenceList = []
#     for sentence in file: 
#         sentenceList.append(sentence)
#     randomSentence = random.choice(sentenceList)
#     return randomSentence

def randomSentence(): 
    file = open("randomWords.txt", "r")
    sentenceLength = random.randint(5, 5)
    sentence = ""
    word_list = [word for word in file]

    for word in range(sentenceLength): 
        randomWord = random.choice(word_list)
        randomWord = randomWord.split()
        sentence = sentence + randomWord[0] + " "

    return sentence

def startTime(event): 
    global start 
    global inital
    if inital == True: 
        start = timer()
        inital = False
        
def checkAnswer(event): 
    end = timer()
    time_elapsed = end - start 
    answer = ent_userInput.get()
    error = 0

    #difference in length
    if len(sentence) != len(answer): 
        error += abs(len(sentence) - len(answer))

    #difference in letters
    user_sentence = ent_userInput.get()
    num_letters = len(sentence)
    for letter in range(num_letters): 
        if sentence[letter] != user_sentence[letter]: 
            error += 1 
    print("the number of errors are: ", error)

    wpm = len(sentence)/5
    wpm = wpm - error 
    wpm = int(wpm / (time_elapsed / 60))
    print(wpm)
    return wpm

def findfWordLengths(sentence): 
    wordLengths = []
    for word in sentence: 
        length = len(word)
        wordLengths.append(length)

    return wordLengths

def selectedWord(event, wordLengths): 
    global index1
    global index2 
    global index
    word = ent_userInput.get()
    numWords = len(wordLengths)
    

    if len(word) + 1 > wordLengths[index] and index < numWords - 1: 
        index += 1 
        index1 = index1 + wordLengths[index] + 1
        index2 = index2 + wordLengths[index] + 1
        ent_userInput.delete(0, END)
        
    if len(word) + 1 > wordLengths[index] and index == numWords - 1: 
        ent_userInput.delete(0, END)

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
index, index1, index2 = None, None, None 

#INITALIZE WINDOW 
window = Tk()
window.title("Typing Test")
window.geometry("500x500")

#SETUP 
sentence = randomSentence()
wordLength = findfWordLengths(sentence)
# lbl_displaySentence = Label(text=sentence)
# lbl_displaySentence.grid(row=0, column = 0)
txt_wordBox = Text(width=len(sentence), height=1)
txt_wordBox.insert(INSERT, sentence)
txt_wordBox.grid(row = 0, column=0)

ent_userInput = Entry(width=len(sentence) + 12)
ent_userInput.bind("<Key>", startTime)
ent_userInput.bind("<Return>", checkAnswer)
ent_userInput.grid(row = 1, column=0)
ent_userInput.focus_set()

window.mainloop()