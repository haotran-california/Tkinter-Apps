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