# Donald Knuth's Five-Guess Algorithm
from codemaker import *

Color = ['red', 'green', 'blue', 'yellow', 'purple', 'white']

def createSet(Color):
    codes = []
    for i in Color:
        for j in Color:
            for k in Color:
                for l in Color:
                    codes.append([i, j, k, l])
    return codes


def updateSet(result, guess, possibleCodes, Color):
    i, end = 0, len(possibleCodes) - 1
    while i <= end:
        if checkCode(possibleCodes[i], guess, Color) != result: 
            possibleCodes.pop(i)
            end = len(possibleCodes) - 1
        else: i += 1


def checkCode(code, guess, Color):
    black = sum(s == g for s, g in zip(code, guess))
    white = sum(min(guess.count(c), code.count(c)) for c in Color) - black
    return [black, white]


def minimax(master, possibleCodes, Color):
    scoreAll = {}  
    scoreSingle = {}
    nextGuesses = [] 
    
    for i in range(len(master)):
        for j in range(len(possibleCodes)):
            
            pegs = tuple(checkCode(possibleCodes[j], master[i], Color))
            if pegs in scoreSingle: scoreSingle[pegs] += 1
            else: scoreSingle[pegs] = 1
        
        index = tuple(master[i])
        scoreAll[index] = max(scoreSingle.values())
        scoreSingle.clear()
        
    least = min(scoreAll.values())
    return [code for code in scoreAll if scoreAll[code] == least]


def findNextGuess(nextGuesses, master, possibleCodes):
    for i in nextGuesses:
        if list(i) in possibleCodes:
            return i
    
    for i in nextGuesses:
        if list(i) in master:
            return i


def codebreaker(CodeMaker):
    master = createSet(Color)
    possibleCodes = master.copy()
    
    guess = [Color[0], Color[0], Color[1], Color[1]]
    result = CodeMaker.guessCode(guess)
    if result == "win" or result == "lose": return
    
    for _ in range(11):
        if guess in possibleCodes: possibleCodes.remove(guess)
        if guess in master: master.remove(guess)
        updateSet(result, guess, possibleCodes, Color)        
        nextGuesses = minimax(master, possibleCodes, Color)
        guess = findNextGuess(nextGuesses, master, possibleCodes)
        result = CodeMaker.guessCode(guess)
        if result == "win" or result == "lose": return