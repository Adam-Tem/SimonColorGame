import tkinter as tk

def createScreen():
    window = tk.Tk()
    window.geometry("500x500")

    start_button = tk.Button(text = "Start game")
    red_button = tk.Button(bg = "#d10c02", activebackground = "#ff6363", width = 8, bd = 3)
    blue_button = tk.Button(bg = "#0590fa", activebackground = "#63fffc", width = 8, bd = 3)
    yellow_button = tk.Button(bg = "#b8b206", activebackground = "#faf205", width = 8, bd = 3)
    green_button = tk.Button(bg = "green", activebackground = "#63ff63", width = 8, bd = 3)



    start_button.grid(row = 0, column = 0)
    red_button.grid(row = 1, column = 1)
    blue_button.grid(row = 1, column = 2)
    yellow_button.grid(row = 1, column = 3)
    green_button.grid(row = 1, column = 4)
    window.mainloop()

createScreen()