import random

#DEFINE SETUP FUNCTIONS
def randomSentence(): 
    file = open("randomWords.txt", "r")
    sentenceLength = random.randint(4, 5)
    sentence = ""
    word_list = [word for word in file]

    for word in range(sentenceLength): 
        randomWord = random.choice(word_list)
        randomWord = randomWord.split()
        sentence = sentence + randomWord[0] + " "

    return sentence

def findWordLengths(sentence): 
    wordLengths = []
    for word in sentence.split(): 
        length = len(word)
        wordLengths.append(length)

    return wordLengths

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