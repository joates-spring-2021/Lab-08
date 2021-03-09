# Lab-08 - Classes
By now you should be pretty familiar with programming in Python. Let's have some fun with this lab and create a game. This lab focuses on using classes, and as usual it will include many other elements.  A skeleton will be there to get you started, but you will be responsible for the majority of the logic.

# Overview
Everyone has heard of the game "hangman."  Right?  The player tries to guess a preselected word one letter at a time.  If a letter is guessed that is not in the word, a body part is added to the gallows (pretty dark now that I think about it). If enough letters are missed, then the whole body is drawn on the gallows and the player loses.  If the player guesses all the letters in the word before the body is fully drawn, he/she wins.

# Background
I'll provide a few elements to help with this task:
- a file containing a list of English words with at least 6 - 12 letters
- a string variable containing the contents of this file
- a class "skeleton" with several empty member functions for you to implement

# Requirements
Using the contents of the English words file and the skeleton class, your code **shall** pick a random index into the list of words to use for the hangman game.  It **shall** then get input from the user in the form of a single letter.  It **shall** check to see if this letter is in the random word. If it is, the letter **shall** be applied to the word so the user can see where it goes, and a turn attempt **shall NOT** be counted.  If the letter is not in the word, an attempt **shall** be counted.  The number of attempts allowed by the user will be equal to the number of letters in the word.  The code **shall** continue prompting the user for a letter until all of the attempts have been made, or the word has been guessed.  You can choose whatever logic you would like, but all member functions of the skeleton Hangman class (except DrawGallows which is optional) **shall** be implemented.

# Assignment Notes: 
Now that we are doing more complicated assignments, it is really important to plan out your logic before you start programming.  Write comments describing what needs to be done in the correct order (like pseudo code).  Then read over your comments and see if the logic makes sense.  Only when you are satisfied with your plan should you start actually coding.  Believe me, it will be quicker in the end this way.

Some things to think about
1. Are you in danger of having an infinite loop?
2. How do you want to display the partial word to the user?
3. Are you keeping track of letters already used?  Don't penalize the player if they forget what they've already guessed.
4. Feel free to add functions to the class, but make sure to implement each one that is there.
