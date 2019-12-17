from random import choice

Colors = ['red', 'green', 'blue', 'yellow', 'purple', 'white']

class CodeMaker:
    def __init__(self):
        self.code = None
        self.attempts = None

    def newGame(self):
        self.attempts = 0
        self.code = {choice(Colors) for i in range(4)}

    def guessCode(self, guess):
        if type(guess) != list or len(guess) != 4 or not (set(guess) <= set(Colors)):
            return "invalid guess"
        black = sum(s == g for s, g in zip(self.code, guess))
        white = sum(min(guess.count(c), self.code.count(c)) for c in Colors) - black
        self.attempts += 1
        if black == 4: return "win"
        if self.attempts == 12: return "lose"
        return (black, white)
        