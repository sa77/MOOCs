# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    temp = list("".join(set(secretWord)))
    wordlen = len(temp)
    count = 0 
    for letter in lettersGuessed:
        if letter in temp:
            count += 1
    if count == wordlen:
        return True
    return False            



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    current_word = ''
    for c in secretWord:
        if c in lettersGuessed:
            current_word += c 
        else:
            current_word += '_ '            
    return current_word


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters = 'abcdefghijklmnopqrstuvwxyz'
    if len(lettersGuessed) == 0:
        return letters
    else:
        available_letters = ''
        for c in letters:
            if c not in lettersGuessed:
                available_letters += c
    return available_letters                


def verifyGuessedLetter(guess_letter, lettersGuessed, secretWord):    
    '''
    guess_letter - string, letter guessed by player
    lettersGuessed - list, list of letters guessed by player till now
    secretWord - string, secret word the player has to guess

    returns: boolean (True is guess is correct | False if guess is incorrect)
    '''
    if guess_letter in lettersGuessed:
        current_word = getGuessedWord(secretWord, lettersGuessed)
        print "Oops! You've already guessed that letter: {cur_word}".format(cur_word = current_word) 
        return True
    else:
        lettersGuessed.append(guess_letter)
        current_word = getGuessedWord(secretWord, lettersGuessed)
        if guess_letter in secretWord: 
            print "Good Guess: {cur_word}".format(cur_word = current_word)
            return True
        else:
            print "Oops! That letter is not in my word: {cur_word}".format(cur_word = current_word)
            return False

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
    global lettersGuessed
    lettersGuessed = []
    count = 8
    while count > 0:
        print 'You have {guess_count} guesses left.'.format(guess_count = count)
        print 'Available letters: {letters}'.format(letters = getAvailableLetters(lettersGuessed)) 
        guess_letter = raw_input('Please guess a letter: ')
        if verifyGuessedLetter(guess_letter, lettersGuessed, secretWord):
            if isWordGuessed(secretWord, lettersGuessed):
                print '------------'        
                print 'Congratulations, you won!'
                break
        elif count == 1:
            print '------------'        
            print 'Sorry, you ran out of guesses. The word was {secretWord}.'.format(secretWord = secretWord)
            break
        else:
            count -= 1
        print '------------'        


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
print 'Welcome to the game, Hangman!'
secretWord = chooseWord(wordlist).lower()
print 'I am thinking of a word that is {wordlen} letters long.'.format(wordlen = len(secretWord))
print '------------ ' + str(secretWord)
hangman(secretWord)




