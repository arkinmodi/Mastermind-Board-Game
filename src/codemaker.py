## @file codemaker.py
#  @author Arkin Modi
#  @brief CodeMaker
#  @date 12/18/2019

from random import choice

Colors = ['red', 'green', 'blue', 'yellow', 'purple', 'white']
totalAttempts = 12

## @brief CodeMaker generated a random code and repsondes to each guess
class CodeMaker:

    ## @brief starts a new game
    def newGame(self):
        self.__attempts = 0
        self.__code = [choice(Colors) for i in range(4)]

    ## @brief calculates the black and white values for a guess
    #  @param guess the inputted guess
    #  @return the corresponding black and white values
    def guessCode(self, guess):
        if type(guess) != list or len(guess) != 4 or not (set(guess) <= set(Colors)):
            return "invalid guess"
        black = sum(s == g for s, g in zip(self.__code, guess))
        white = sum(min(guess.count(c), self.__code.count(c)) for c in Colors) - black
        self.__attempts += 1
        if self.__attempts == totalAttempts: return "lose"
        return (black, white)

    ## @brief gets the secret code
    #  @return the secret code
    def getCode(self):
        return self.__code
    
    ## @brief gets the number of attempts remaining
    #  @return the number of attempts remaining
    def getAttemptsLeft(self):
        return totalAttempts - self.__attempts