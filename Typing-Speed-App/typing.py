from tkinter import * 
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
    sentenceLength = random.randint(5, 13)
    sentence = ""
    word_list = [word for word in file]

    for word in range(sentenceLength): 
        randomWord = random.choice(word_list)
        randomWord = randomWord.split()
        sentence = sentence + randomWord[0] + " "

    return sentence


def test(): 
    print(ent_userInput.get())
    if ent_userInput.get() == "": 
        print("nothing here")

def checkAnswer(): 
    end = timer()
    time_elapsed = end - start 
    answer = ent_userInput.get()
    error = 0

    #difference in length
    if len(sentence) != len(answer): 
        error += abs(len(sentence) - len(answer))

    wpm = len(sentence)/5
    wpm = wpm - error 
    wpm = (wpm / (time_elapsed / 60))
    return wpm


window = Tk()
window.title("Typing Test")
window.geometry("500x500")

sentence = randomSentence()
lbl_displaySentence = Label(text=sentence)
lbl_displaySentence.grid(row=0, column = 0)

ent_userInput = Entry()
ent_userInput.grid(row = 1, column=0)

btn_submit = Button(text="Submit", command=checkAnswer)
btn_submit.bind("<Return>", checkAnswer)
btn_submit.grid(row = 2, column = 0)

start = timer()


window.mainloop()