colors = ["red", "green", "yellow", "blue"]

def adjustCase(entered_color):
    return entered_color.lower()

def removeSpaces(entered_color):
    return entered_color.strip()

def validColor(entered_color):
    entered_color = oneCharInput(adjustCase(removeSpaces(entered_color)))
    if(entered_color in colors):
        return True, entered_color
    else:
        return False

def oneCharInput(entered_color):
    if(len(entered_color) == 1):
        for color in colors:
            if (color[0] == entered_color):
                return color
        return entered_color
    else:
        return entered_color
