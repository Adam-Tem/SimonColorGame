import tkinter as tk
from GameActions import *
from SequenceActions import *
import time

def createScreen():
    window = tk.Tk()
    window.geometry("500x500")
    sequence = ""
    displayed_text = tk.StringVar()
    displayed_text.set("Please press start to begin!")

    def startGame():
        red_button.config(command = hello, state = "normal")
        blue_button.config(command = hello, state = "normal")
        yellow_button.config(command = hello, state = "normal")
        green_button.config(command = hello, state = "normal")
        sequence = createSequence()
        start_button.config(state = "disabled")
        displaySequence(sequence)

    def displaySequence(sequence):
        for step in sequence:
            print(step)
            displayed_text.set(step)
            window.update()
            time.sleep(1)
        displayed_text.set("Now repeat the sequence below!")


    
    start_button = tk.Button(text = "Start game", command = startGame)
    red_button = tk.Button(bg = "#d10c02", activebackground = "#ff6363", width = 8, bd = 3, state = "disabled", text = "red")
    blue_button = tk.Button(bg = "#0590fa", activebackground = "#63fffc", width = 8, bd = 3, state = "disabled", text = "blue")
    yellow_button = tk.Button(bg = "#b8b206", activebackground = "#faf205", width = 8, bd = 3, state = "disabled", text = "yellow")
    green_button = tk.Button(bg = "green", activebackground = "#63ff63", width = 8, bd = 3, state = "disabled", text = "green")

    patternLabel = tk.Label(textvariable = displayed_text, height = 10)

    start_button.pack(fill = tk.X)
    patternLabel.pack()

    red_button.pack(side = tk.LEFT, fill=tk.X, expand = True)
    blue_button.pack(side = tk.LEFT, fill=tk.X, expand = True)
    yellow_button.pack(side = tk.LEFT, fill=tk.X, expand = True)
    green_button.pack(side = tk.LEFT, fill=tk.X, expand = True)

 
    return window