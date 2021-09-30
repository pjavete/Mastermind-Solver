from tkinter import *
import random

def main():
    root = Tk()
    myCanvas = Canvas(root)
    myCanvas.pack()

    create_circle(100, 100, 20, myCanvas)
    create_circle(50, 25, 10, myCanvas)

    root.mainloop()

def create_circle(x, y, r, color, canvasName): #center coordinates, radius, color
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1, outline="#000", fill=color)

# Generates a random code of size 'size' from set 'colors' with a duplicate switch
def generate_code(duplicates, size, colors):
    if duplicates:
        return random.choice(colors, k=size)
    else:
        return random.sample(colors, size)

if __name__ == "__main__":
    main()