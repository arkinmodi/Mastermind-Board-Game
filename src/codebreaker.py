## @file codebreaker.py
#  @author Arkin Modi
#  @brief Donald Knuth's Five-Guess Algorithm
#  @date 12/18/2019

Color = ['red', 'green', 'blue', 'yellow', 'purple', 'white']

## @brief CodeBreaker utilizes Donald Knuth's Five-Guess Algorithm to solve the code
class CodeBreaker:

    ## @brief creates a list of all possible codes
    #  @return a list of all possbile codes
    def __createSet(self):
        codes = []
        for i in Color:
            for j in Color:
                for k in Color:
                    for l in Color:
                        codes.append([i, j, k, l])
        return codes

    ## @brief removes all codes that do not generate the same response as the guess
    #  @param result the response from the CodeMaker
    #  @param guess the guess that the result was generated from
    #  @param possibleCodes the list of all possible solutions
    def __updateSet(self, result, guess, possibleCodes):
        i, end = 0, len(possibleCodes) - 1
        while i <= end:
            if self.__checkCode(possibleCodes[i], guess) != result: 
                possibleCodes.pop(i)
                end = len(possibleCodes) - 1
            else: i += 1

    ## @brief calculates the response of a given guess with a given code
    #  @param code the assumed correct code
    #  @param guess the guessed code
    #  @return the corresponding black and white values
    def __checkCode(self, code, guess):
        black = sum(s == g for s, g in zip(code, guess))
        white = sum(min(guess.count(c), code.count(c)) for c in Color) - black
        return (black, white)

    ## @brief calculates list of next guesses
    #  @param master a master list of all possible combinations
    #  @param possibleCodes a list of all possible solutions
    #  @return a list all possible next guesses
    def __minimax(self, master, possibleCodes):
        scoreAll = {}       # tracks max peg for all combinations
        scoreSingle = {}    # tracks all pegs for a single combination
        nextGuesses = []    # all possible next guesses
        
        for i in master:
            for j in possibleCodes:
                
                # track number of peg occurrences (i.e the hit count)
                pegs = self.__checkCode(i, j)
                if pegs in scoreSingle: scoreSingle[pegs] += 1
                else: scoreSingle[pegs] = 1

            # store the max possible peg occurrences of the combination
            index = tuple(i)
            scoreAll[index] = max(scoreSingle.values())
            scoreSingle.clear()
        
        # return a list of that have the smallest max possible peg occurrences
        least = min(scoreAll.values())
        return [list(code) for code in scoreAll if scoreAll[code] == least]

    ## @brief selects next guess from list of possible next guesses
    #  @param nextGuesses a list of possbile next guesses
    #  @param master a master list of all possible combinations
    #  @param possibleCodes a list of all possible solutions
    #  @return a single code to be guessed
    def __findNextGuess(self, nextGuesses, master, possibleCodes):
        # first check if guess is in possible solutions
        for i in nextGuesses:
            if list(i) in possibleCodes:
                return i
        
        # check if guess is in master list
        for i in nextGuesses:
            if list(i) in master:
                return i

    ## @brief codebreaker controller
    #  @param CodeMaker the current codemaker that is to be solved
    def run(self, CodeMaker):
        # setup
        master = self.__createSet()     # master list of combinations not guessed
        possibleCodes = master.copy()   # possible solutions
        
        guess = [Color[0], Color[0], Color[1], Color[1]]    # first guess
        result = CodeMaker.guessCode(guess)                 # initial check of guess
        yield (result, guess)
        
        for _ in range(11):
            if guess in possibleCodes: possibleCodes.remove(guess)              # remove guess from possible solutions
            if guess in master: master.remove(guess)                            # remove guess from master list
            self.__updateSet(result, guess, possibleCodes)                      # remove codes from possible solutions that do not match pegs
            nextGuesses = self.__minimax(master, possibleCodes)                 # find all next possible guesses 
            guess = self.__findNextGuess(nextGuesses, master, possibleCodes)    # select a guess
            result = CodeMaker.guessCode(guess)                                 # check guess
            yield (result, guess)
            if result == (4,0) or result == "lose": return