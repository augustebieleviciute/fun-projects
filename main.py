from tkinter import *
from matrix import *

root = Tk()

def printname(event):
    print("Hello im tavotevas")

button1 = Button(root, text="Whats my name")
button1.bind("<Button-1>", printname)
button1.pack()

root.mainloop()