from InputChecks import *

def inputColor():
    entered_color = input()
    valid, entered_color = validColor(entered_color)
    strikes = 0


    while(valid == False and strikes < 2):
        entered_color = input("Please enter a valid color...\n")
        strikes += 1
    
    if(strikes == 3):
        print("Too many invalid inputs.")
        return "game over"
    else:
        return entered_color






    