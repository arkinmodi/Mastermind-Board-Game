from codemaker import *
from codebreaker import *

CodeMaker = CodeMaker()
CodeBreaker = CodeBreaker().run(CodeMaker)
result = (None, None)
while result[0] != (4, 0) and result != "lose":
    result = next(CodeBreaker)
    if result == "lose": break
    response = "B"*result[0][0] + "W"*result[0][1] if (result[0][0] + result[0][1] > 0) else "None"
    print("guess: " + ', '.join(result[1]))
    print("response: " + response + '\n')

if result == "lose": print("Game Over! The code was: " + ', '.join(CodeMaker.getCode()))
else: print("You Win")
