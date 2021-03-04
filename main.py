
# -*- coding: utf-8 -*-
"""
johnwoates
CPSC 223P-01
Thu Mar 8, 2021
joates@fullerton.edu
"""

import random

# Hangman class.
class Hangman:
    
    def __init__(self, word, triesAllowed):
        pass

    def Guess(self, letter):
        """Pass in a letter (length = 1) and check to see if it is in the word.
            If it is, replace blanks in display word with letter and return True
            If not, decrement the number of tries left and return False
        """
        pass

    def GetNumTriesLeft(self):
        """Return the number of tries left"""
        pass
    
    def GetDisplayWord(self):
        """Return the display word (with blanks where letters have not been guessed)"""
        pass
    
    def GetLettersUsed(self):
        """Return a string with the list of letters that have been used"""
        pass

    def DidIWin(self):
        """Return True if all letters have been guessed. False otherwise"""
        pass

    def DrawGallows(self):
        """Optional: Return string representing state of gallows"""
        pass

# implement the logic of your game below
if __name__=="__main__":
    # Read all the words from the hangman_words.txt file
    wordFile = open("hangman_words.txt", "r")
    
    # Seed the random number generator with current system time
    random.seed()
    
    # Convert the string of words in wordFile to a list,
    # then get a random word using
    # randomIndex = random.randint(min, max)
    
    # Instantiate a game using the Hangman class
    
    
    # Use a while loop to play the game
