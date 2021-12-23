import random

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

def findfWordLengths(sentence): 
    wordLengths = []
    for word in sentence.split(): 
        length = len(word)
        wordLengths.append(length)

    return wordLengths

# def randomSentence(): 
#     file = open("sentence.txt", "r")
#     sentenceList = []
#     for sentence in file: 
#         sentenceList.append(sentence)
#     randomSentence = random.choice(sentenceList)
#     return randomSentence