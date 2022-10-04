#Wordle :)
#Joey Koumjian

#This is a program to play the game Wordle in text format

import random

#initialize a global wordList that we will write data to
wordList = []

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
            print("Invalid file name try again ...")
    return inFile

# Function to append all the words in the wordlist file into the actual global wordList
# Returns the wordList
def getData():
    inFile = openFile()
    for line in inFile:
        line = line.strip()
        word = line.split(',')
        wordList.append(word)
    inFile.close()
    return wordList

# Function to choose a random word out of the list
# Returns this (the user is trying to guess this word)
def getWordle(wordList):
    n = random.randint(1,344)
    wordle = wordList[n]
    wordle = wordle[0]
    return wordle

# Function to ask the user for their guess
# The guess must be exactly five characters or it will not work
# The function returns the guess as an all uppercase string
def computeGuess(wordle):
    score = 0
    guessing = False
    guess = input("Make a guess: ")
    guess = str(guess.upper())
    
    checkingGuess = True
    while checkingGuess == True:
        for i in range(len(wordList)):
            if guess != wordList[i]:
                checkingGuess = False
    if checkingGuess == False:
        print("Word not in dictionary - try again ... ")
                
    if len(guess) != 5:
        guess = computeGuess(wordle)
    else:
        return guess.upper()

# Function to compare the guess of the user to the actual chosen word they are
# trying to guess.
# The guess was returned as an uppercase string in the previous function because all the
# words from the file are all uppercase so its easier to identify matches.
# I made the output a list becuase I was having difficulty using strings
# If there is a direct match between character and location - a 'G' is inserted
# If the guess is a correct letter but is in the wrong place a 'Y' is inserted
# The output is returned
def computeClue(guess, wordle):
    clue = ['X','X','X','X','X']
    guess = str(guess)
    for i in range(len(guess)):
        if guess[i] == wordle[i]:
            clue[i] = 'G'
        for j in range(len(wordle)):
            if guess[i] == wordle[j] and guess[i] != wordle[i]:
                clue[i] = "Y"
    return clue

# This prints the output as a string
def printOutput(clue):
    outprint = ""
    for i in range(len(clue)):
        outprint = outprint + clue[i]
    print(outprint)
    return outprint

# This function checks if the outprint from the previous function is a win or not
# It checks if the string is five "G's"
# It also prints your score
def checkWin(outprint,wordle,score,totalScore):
    won = False
    if outprint == "GGGGG":
        print("Your score is: ",score)
        print("Your overall score is: ",totalScore)
        won = True
    return won

# This was my previous main function
# It plays the actual game and generates a new wordle
# Each time the game increases the score it checks if you won and
# it checks if you have guessed too many times so you lose
def play(wordList, wordle,totalScore):
    wordle = getWordle(wordList)
    scoring = False
    score = 0
    while scoring == False:
        guess = computeGuess(wordle)
        clue = computeClue(guess, wordle)
        outprint = printOutput(clue)
        score = score + 1
        totalScore += 1
        won = checkWin(outprint,wordle,score,totalScore)
        if won == True:
            scoring = True

        elif score == 7:
            print("You lose. ")
            return

    #if you lose it returns
    #otherwise if you won it will ask if you want to play again or not
        #if yes it runs the play function again
        #if no it returns
    
    checkAsk = False
    while checkAsk == False:
        ask = input("Would you like to play again (Y or N)? ")
        if ask == "N" or ask == "n":
            print("Thanks for playing! ")
            return
        elif ask == "Y" or ask == "y":
            play(wordList,wordle,totalScore)
            checkAsk = True

#this is the main function that takes a seed to generate the random number
#that selects the wordle.
#it creates the wordlist and plays the game
def main(seedValue):
    random.seed(seedValue)
    wordList = getData()
    wordle = getWordle(wordList)
    totalScore = 0
    play(wordList, wordle,totalScore)
    

            

    
