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

def findWordLengths(sentence): 
    wordLengths = []
    for word in sentence.split(): 
        length = len(word)
        wordLengths.append(length)

    return wordLengths

def checkAnswer(sentence, answer): 
    end = timer()
    time_elapsed = end - start 
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

    wpm = len(sentence)/5
    wpm = wpm - error 
    wpm = int(wpm / (time_elapsed / 60))
    accuracy = (len(sentence)-wpm)/100
    return (wpm, accuracy)

# def randomSentence(): 
#     file = open("sentence.txt", "r")
#     sentenceList = []
#     for sentence in file: 
#         sentenceList.append(sentence)
#     randomSentence = random.choice(sentenceList)
#     return randomSentence

