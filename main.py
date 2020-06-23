from tkinter import *
from matrix import Matrix

root = Tk()

#matrix1Frame = Frame(root)
#matrix1Frame.pack()
#matrix2Frame = Frame(root)
#matrix2Frame.pack(side=RIGHT)
#buttonsFrame = Frame(root)
#buttonsFrame.pack(side=RIGHT)
#displayFrame = Frame(root)
#displayFrame.pack(side=BOTTOM)

mtx1 = Label(root, text="Matrix 1:")
mtx2 = Label(root, text="Matrix 2:")

mtx1.grid(row=0, columnspan=3)
mtx2.grid(row=0, column=4, columnspan=3)

def drawButtons(row=3, col=3):

    for i in range(row):
        for j in range(col):
            entryname = 'entry' + str(i) + str(j)
            entryname = Entry(root, width=4)
            if j == col-1:
                entryname.grid(row=i+1, column=j+1, padx=10)
            entryname.grid(row=i+1, column=j)


def callBack():
    print("button clicked")
    drawButtons(col=6)



drawButtons()

varmatrix2 = BooleanVar()
varmatrix2.set(False)

matrix2 = Checkbutton(root, text="Add second matrix", var=varmatrix2, command=callBack)
matrix2.grid(row=1, column=10)

#print(varmatrix2.get())
root.mainloop()