from codemaker import *
from codebreaker import *

print(
    "Select 0 for Auto Play\n" +
    "Select 1 for Manual Play"
)
mode = input()
print()
CodeMaker = CodeMaker()
CodeMaker.newGame()

if mode == '0':
    CodeBreaker = CodeBreaker().run(CodeMaker)
    result = (None, None)
    while result[0] != (4, 0):
        result = next(CodeBreaker)
        if result == "lose": break
        response = "B"*result[0][0] + "W"*result[0][1] if (result[0][0] + result[0][1] > 0) else "None"
        print("guess: " + ', '.join(result[1]))
        print("response: " + response + '\n')
    
    if result == "lose": print("Game Over! The code was: " + ', '.join(CodeMaker.getCode()))
    else: print("You Win")

else:
    Color = ['red', 'green', 'blue', 'yellow', 'purple', 'white']
    print("The colors are: " + ', '.join(Color))
    print("Separate the guess with a ',' (i.e. red, red, green, green)\n")
    result = None
    while result != (4, 0):
        guess = input("guess: ")
        guess = guess.split(sep=', ')
        result = CodeMaker.guessCode(guess)
        if result == "lose": break
        response = "B"*result[0] + "W"*result[1] if (result[0] + result[1] > 0) else "None"
        print("response: " + response)
        print("You have " + str(CodeMaker.getAttemptsLeft()) + " remaining" + '\n')

    if result == "lose": print("\nGame Over! The code was: " + ', '.join(CodeMaker.getCode()))
    else: print("\nYou Win")