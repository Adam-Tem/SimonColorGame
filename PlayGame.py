from SequenceActions import *
from UserActions import *

sequence = createSequence()
matching = True
score = 0

print(sequence)

while(matching):
    print("Please enter the sequence.\n")
    for i in range(len(sequence)):
        guess = inputColor()
        if(sequence[i] != guess):
            matching = False
            break
    if(matching):
        score += 1
        addToSequence(sequence)
    else:
        print("Unlucky, you entered the wrong sequence!\n")
        print(f"Correct sequence streak: {score} \n")
        print("Thanks for playing.")





