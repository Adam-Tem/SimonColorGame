import numpy as np

colors = ["red", "green", "yellow", "blue"]

def createSequence():
    sequence = []
    for i in range(3):
        addToSequence(sequence)
    
    return sequence

def newColor():    
    return colors[np.random.randint(4)]

def addToSequence(sequence):
    next_color = newColor()
    length = len(sequence)
    if(length > 0):
        while(next_color == sequence[length - 1]):
            next_color = newColor()
    sequence.append(next_color)
    return sequence

        


