from tkinter import *
import random

def main():
    colors = {
        "green": '#42c744',
        "red": '#ed2e0c',
        "blue": '#0f3cf2',
        "yellow": '#f4ff29',
        "brown": '#804200',
        "orange": '#f78c20',
        "black": '#000',
        "white": '#fff'
    }

    root = Tk()

    frame = Frame(root)
    frame.pack(expand=True, fill="both")

    size_var = IntVar()
    dup_var = IntVar()

    def submit():
        frame.grid_forget()
        frame.destroy()

        size = size_var.get()
        duplicates = dup_var.get()

        #figure out multiple canvases in grid format
        myCanvas = Canvas(root, width=(size*45+5), height=50, background='white')
        myCanvas.grid(row=10, column=0)

        guess(colors, myCanvas)

    size_label = Label(frame, text='Code Length', font=('calibre', 10, 'bold'))
    size_entry = Entry(frame, textvariable=size_var, font=('calibre', 10, 'normal'))

    dup_box = Checkbutton(frame, variable=dup_var, text='Duplicates?', font=('calibre', 10, 'normal'))

    sub_btn = Button(frame, text='Submit', command=submit)

    size_label.grid(row=0, column=0)
    size_entry.grid(row=0, column=1)
    dup_box.grid(row=1, column=0)
    sub_btn.grid(row=2, column=1)

    root.mainloop()

def guess(colors, myCanvas):
    create_circle(25, 25, 20, colors['black'], myCanvas)
    create_circle(70, 25, 20, colors['orange'], myCanvas)

#center coordinates, radius, color
def create_circle(x, y, r, color, canvasName):
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