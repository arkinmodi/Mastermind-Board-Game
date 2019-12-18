# Donald Knuth's Five-Guess Algorithm
Color = ['red', 'green', 'blue', 'yellow', 'purple', 'white']

class CodeBreaker:
    def __createSet(self):
        codes = []
        for i in Color:
            for j in Color:
                for k in Color:
                    for l in Color:
                        codes.append([i, j, k, l])
        return codes


    def __updateSet(self, result, guess, possibleCodes):
        i, end = 0, len(possibleCodes) - 1
        while i <= end:
            if self.__checkCode(possibleCodes[i], guess) != result: 
                possibleCodes.pop(i)
                end = len(possibleCodes) - 1
            else: i += 1


    def __checkCode(self, code, guess):
        black = sum(s == g for s, g in zip(code, guess))
        white = sum(min(guess.count(c), code.count(c)) for c in Color) - black
        return (black, white)


    def __minimax(self, master, possibleCodes):
        scoreAll = {}  
        scoreSingle = {}
        nextGuesses = [] 
        
        for i in master:
            for j in possibleCodes:
                
                pegs = self.__checkCode(i, j)
                if pegs in scoreSingle: scoreSingle[pegs] += 1
                else: scoreSingle[pegs] = 1

            index = tuple(i)
            scoreAll[index] = max(scoreSingle.values())
            scoreSingle.clear()
            
        least = min(scoreAll.values())
        return [list(code) for code in scoreAll if scoreAll[code] == least]


    def __findNextGuess(self, nextGuesses, master, possibleCodes):
        for i in nextGuesses:
            if list(i) in possibleCodes:
                return i
        
        for i in nextGuesses:
            if list(i) in master:
                return i


    def run(self, CodeMaker):
        master = self.__createSet()
        possibleCodes = master.copy()
        
        guess = [Color[0], Color[0], Color[1], Color[1]]
        result = CodeMaker.guessCode(guess)
        yield (result, guess)
        
        for _ in range(11):
            if guess in possibleCodes: possibleCodes.remove(guess)
            if guess in master: master.remove(guess)
            self.__updateSet(result, guess, possibleCodes)
            nextGuesses = self.__minimax(master, possibleCodes)
            guess = self.__findNextGuess(nextGuesses, master, possibleCodes)
            result = CodeMaker.guessCode(guess)
            yield (result, guess)
            if result == (4,0) or result == "lose": return