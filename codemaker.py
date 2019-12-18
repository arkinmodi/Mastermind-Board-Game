from random import choice

Colors = ['red', 'green', 'blue', 'yellow', 'purple', 'white']
totalAttempts = 12

class CodeMaker:
    def newGame(self):
        self.__attempts = 0
        self.__code = [choice(Colors) for i in range(4)]

    def guessCode(self, guess):
        if type(guess) != list or len(guess) != 4 or not (set(guess) <= set(Colors)):
            return "invalid guess"
        black = sum(s == g for s, g in zip(self.__code, guess))
        white = sum(min(guess.count(c), self.__code.count(c)) for c in Colors) - black
        self.__attempts += 1
        if self.__attempts == totalAttempts: return "lose"
        return (black, white)

    def getCode(self):
        return self.__code
    
    def getAttemptsLeft(self):
        return totalAttempts - self.__attempts