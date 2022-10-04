#Wordle :)
#Joey Koumjian

#This is a program to play the game Wordle in text format

import random

#initialize a global wordList that we will write data to
#initialize allwordlist so that we dont reuse any words

# Open's the data file
# Makes sure the file exists and if so return the file
def openFile():
    goodFile = False;
    while goodFile == False:
        fname = input("Please enter a file name: ")
        try:
            inFile = open(fname, 'r')
            goodFile = True
        except IOError:
            print("Invalid file name try again ... ")
    return inFile

# Function to append all the words in the wordlist file into the actual global wordList
def getData():
    wordList = []
    inFile = openFile()
    for line in inFile:
        word = line.strip()
        wordList.append(word)
    inFile.close()
    return wordList

# Function to choose a random word out of the list
# Returns this (the user is trying to guess this word)
def getWordle(wordList):
    n = random.randint(0,len(wordList)-1)
    worldWord = wordList[n]
    return worldWord

# Function to ask the user for their guess
# The guess must be exactly five characters or it will not work
# The function returns the guess as an all uppercase string
# While true is just a while loop until it returns
# instead of looping thru the entire list we can ask if the guess is not in the list
def computeGuess(wordList):
    while True:
        guessWord = input("Make a guess: ")
        guessWord = str(guessWord).upper()
        if guessWord not in wordList:
            print("Word not in dictionary - try again ... ")
        else:
            return guessWord

#this functions returns a dictionary of how many elements of each character
#are in a word
def characterCounter(word):
    counts = {}
    for i in range(len(word)):
        if word[i] not in counts:
            counts[word[i]] = 1
        else:
            counts[word[i]] += 1
    return counts

# Function to compare the guess of the user to the actual chosen word they are
# trying to guess.
# The guess was returned as an uppercase string in the previous function because all the
# words from the file are all uppercase so its easier to identify matches.
# I made the output a list becuase I was having difficulty using strings
# If there is a direct match between character and location - a 'G' is inserted
# If the guess is a correct letter but is in the wrong place a 'Y' is inserted
# The output is returned
def computeClue(guessWord, worldWord):
    print(guessWord)
    clue = ['X','X','X','X','X']
    characterCounts = characterCounter(guessWord)
    for i in range(len(guessWord)):
        if guessWord[i] == worldWord[i]:
            clue[i] = 'G'
            characterCounts[guessWord[i]] -= 1
    for i in range(len(guessWord)):
        for j in range(len(worldWord)):
            if guessWord[i] == worldWord[j] and guessWord[i] != worldWord[i] and clue[j] != 'G':
                if characterCounts[guessWord[j]] > 0:
                    clue[i] = "Y"
                    characterCounts[guessWord[j]] -=1
    return clue

# This prints the output as a string
# print(clue.join(""))
# note this command does the same thing as my function^^
def printOutput(clue):
    outprint = ""
    for i in range(len(clue)):
        outprint = outprint + clue[i]
    print(outprint)
    return outprint

# This function checks if the outprint from the previous function is a win or not
# It checks if the string is five "G's"
# It also prints your score
def checkWin(outprint):
    won = False
    if outprint == "GGGGG":
        won = True
    return won

# This was my previous main function
# It plays the actual game and generates a new wordle
# Each time the game increases the score it checks if you won and
# it checks if you have guessed too many times so you lose
def play(wordList,totalScore):
    usedWords = []
    while True:
        worldWord = getWordle(wordList)
        if worldWord not in usedWords:
            usedWords.append(worldWord)
            break
            #checks to see if the word has been used or not
            # if so it generates a new wordle, otherwise it breaks
            
    scoring = False
    score = 0
    while scoring == False:
        guessWord = computeGuess(wordList)
        clue = computeClue(guessWord, worldWord)
        outprint = printOutput(clue)
        score = score + 1
        won = checkWin(outprint)
        if won == True:
            totalScore = totalScore + score
            print("")
            print("Congratulations, your wordle score for this game is  ",str(score))
            print("Your overall score is  ",str(totalScore))
            print("")
            scoring = True

        elif score == 6:
            totalScore = totalScore + 10
            print("Sorry, you did not guess the word:   ",worldWord)
            print("Your overall score is  ",str(totalScore))
            print("")
            scoring = True
    

    #if you lose it returns
    #otherwise if you won it will ask if you want to play again or not
        #if yes it runs the play function again
        #if no it returns
    
    checkAsk = False
    while checkAsk == False:
        ask = input("Would you like to play again (Y or N)? ")
        if ask == "N" or ask == "n":
            print("")
            print("Thanks for playing! ")
            return
        elif ask == "Y" or ask == "y":
            play(wordList,totalScore)
            checkAsk = True

#this is the main function that takes a seed to generate the random number
#that selects the wordle.
#it creates the wordlist and plays the game
def main(seedValue):
    random.seed(seedValue)
    wordList = getData()
    totalScore = 0
    play(wordList, totalScore)
    
