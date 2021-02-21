###############################################################
## Global AI Hub Introduction to Python Programming Course
## Day 5 Homework Assignment 1
## Hangman
###############################################################
## Author: Oğuzhan GÜVERCİN
## Author Email: ogzhngvrcn00@gmail.com
###############################################################

# Importing required module
import random
from os import system
# All of the special characters to filter user inputs
numsChars = "01234567890!#$€é%&'()*+,-./:;<=>?@[\]^_`{|}~\""


# Creating object
class Hangman:

    # Initializing object variables
    def __init__(self, gameStates, wordList, playMode=None):
        self.lives = 6
        self.stateNum = 0
        self.states = gameStates
        self.wordList = wordList
        self.playMode = playMode

    @staticmethod
    def checkWord(word):
        if any(c in numsChars for c in word):
            print("Don't cheat >:(. Use of special characters and number is not allowed!")
            return False
        else:
            return True

    # A method to choose between Player vs Player and Computer vs Player
    def choosePlayMode(self):
        while True:
            # Asking user for player mode
            self.playMode = input("Enter 1 for Player vs Player mode or enter 2 for Computer vs Player mode :")
            # If 1 is chosen
            if self.playMode == "1":
                # Select Player vs Player mode
                print("You've chosen Player vs Player mode."
                      "In this mode Player 1 is going to select a word and Player 2 will try to guess it.")

                while True:
                    # And ask Player 1 for a word and lowercase it
                    word = input("Player 1 input your word don't let Player 2 see it :) :").lower()
                    # If player 1 tries to choose a word with special characters
                    if not self.checkWord(word):
                        # Ask for another word
                        continue
                    # Else
                    else:
                        # Break
                        break
                # Return the word
                return word
            # If 2 is chosen
            elif self.playMode == "2":
                # Select Computer vs Player mode:
                print(
                    "You've chosen Computer vs Player mode."
                    "In this mode Computer is going to select a word and Player 2 will try to guess it.")
                # Select a word
                word = self.selectWord()
                return word
            # If user typed a wrong input, inform user and ask for an mode selection again
            else:
                print("Wrong input! please only input 1 and 2 don't include any other characters.")
                continue

    # A method to select a word from word pool
    def selectWord(self):
        selectedWord = self.wordList[random.randint(0, len(self.wordList) - 1)]
        return selectedWord

    # A method to update game state
    def drawState(self):
        print(self.states[self.stateNum])

    # A static method to check if guessed letter is in the word
    @staticmethod
    def checkLetter(letter, word, emptyLines):
        # If we can't find any matches assign False to check variable
        check = False
        # Iterating over the word
        for i in range(len(word)):
            # If any letter in the word matches with guessed letter
            if letter == word[i]:
                # Fill that empty line with guessed letter
                emptyLines = emptyLines[:i] + letter + emptyLines[i + 1:]
                # Update the check to True since we found a matching letter
                check = True

        # Return check and emptyLines
        return check, emptyLines

    # A function to apply game logic
    def gameLogic(self):
        # Initializing required variables
        check = False
        rightLetters = []
        wrongLetters = []

        # Getting a random word from word pool or from Player 1
        word = self.choosePlayMode()
        system('cls')
        # Drawing game state and printing game info
        self.drawState()
        emptyLines = "_" * len(word)
        print(emptyLines)

        # Looping until word is found or live count goes down to zero
        while not check and self.lives != 0:
            # Getting a guess from user
            guessedLetter = input("Make your guess : ")
            # Asking for an input again if input isn't a string
            if not isinstance(guessedLetter, str):
                print("You are allowed to enter only letters!")
                continue
            # Asking for an input again if input string isn't one letter
            elif len(guessedLetter) > 1:
                print("You are only allowed to enter one letter!")
                continue
            # Asking for an input again if input isn't a string but a special character
            elif numsChars.find(guessedLetter) != -1:
                print("You are allowed to enter only letters!")
                continue
            # Asking for an input again if user inputs a letter that already guessed before
            elif guessedLetter in wrongLetters or guessedLetter in rightLetters:
                print("You already guessed that letter!")
                continue
            # Checking if guessed letter matches with any character from the word and updating the blank lines
            isRightGuess, emptyLines = self.checkLetter(guessedLetter, word, emptyLines)
            # If guessed letter matches with any character from the word informing user and adding letter to correct guessed letters list
            if isRightGuess:
                rightLetters.append(guessedLetter)
                print("Good guess!")
            # If guessed letter doesn't match with any character from the word informing user and adding letter to wrong guessed letters list
            else:
                self.lives -= 1
                self.stateNum += 1
                wrongLetters.append(guessedLetter)
            # Clear console
            system('cls')
            # Updating game state and game info
            self.drawState()
            print("{} lives left".format(self.lives))
            print(emptyLines)
            print(wrongLetters)

            # Checking if user has won the games
            if emptyLines.find("_") == -1:
                print("Congratulations you found the word!!!")
                exit()
            # If not continuing
            else:
                continue

        # If user ran out of lives finishing the game
        print("The word was {}".format(word))
        print("You have lost the game :(")


# An ASCII art to display game states
states = ['''
               +---+
               |   |
                   |
                   |
                   |
                   |
             =========''', '''
               +---+
               |   |
               O   |
                   |
                   |
                   |
             =========''', '''
               +---+
               |   |
               O   |
               |   |
                   |
                   |
             =========''', '''
               +---+
               |   |
               O   |
              /|   |
                   |
                   |
             =========''', '''
               +---+
               |   |
               O   |
              /|\  |
                   |
                   |
             =========''', '''
               +---+
               |   |
               O   |
              /|\  |
              /    |
                   |
             =========''', '''
               +---+
               |   |
               O   |
              /|\  |
              / \  |
                   |
             =========''']

# A word pool to choose from
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

print("WELCOME TO HANGMAN")
# Initiating hangman class
game = Hangman(gameStates=states, wordList=words)

# Staring the game
game.gameLogic()
