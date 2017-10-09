# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 13:46:59 2017

@author: quel
"""

# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"




def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    
    ans = ""
    for i in secretWord:
        if i not in lettersGuessed:
            ans += "_ "            
        else:
            ans += (i + " ")
                
    return ans


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    a = string.ascii_lowercase    
    ans = ""
    for i in a:
        if i not in lettersGuessed:
            ans += i
    return ans




def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    lettersGuessed = []
    lettersGuessed2 = []
    lenofword = len(secretWord)
    print("Welcome to the game, Hangman!")
    print("I am thinking of a world that is " +str(lenofword)+ " letters long")
    import string
    a = string.ascii_lowercase 
    guesses = 8
    s = getGuessedWord(secretWord, lettersGuessed)
    while  guesses != 0:
        print("-----------")
        print("You have "+str(guesses)+ " guesses left")
        print("Available letters: "+str(a))
        EnteredValue = input("Please guess a letter: ")
        lettersGuessed += EnteredValue.lower()
        
        newtry = "".join(lettersGuessed[-1:])
        
        if EnteredValue in lettersGuessed2:
            print("Oops! You've already guessed that letter: "+getGuessedWord(secretWord, lettersGuessed))
            guesses += 1
            
        
        elif "".join(lettersGuessed[-1:]) in secretWord:
            print("Good guess: " +getGuessedWord(secretWord, lettersGuessed))
        
            a = a.replace(newtry,'')
            guesses += 1
        
        else:
            lettersGuessed = lettersGuessed[0:-1]
            print("Oops! That letter is not in my word: " +getGuessedWord(secretWord, lettersGuessed))
            a = a.replace(newtry,'')
        
        s = getGuessedWord(secretWord, lettersGuessed)        
        guesses -= 1
        if "_" not in s:
            guesses = 0            
        lettersGuessed2 += EnteredValue
        global Flag
        Flag = getGuessedWord(secretWord, lettersGuessed) 
        
    print("-----------")
    if '_' not in Flag:
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was "+str(secretWord))
    
            
        
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
