from tkinter import *
from tkinter import ttk
import numpy as np

gridSize = (5, 9, 3)

root = Tk()
# root.geometry('300x300')

content = ttk.Frame(root)

# one = ttk.Frame(content, borderwidth=5, relief="ridge", width=100, height=100)
# oneButton = ttk.Button(one, text="1")

# two = ttk.Frame(content, borderwidth=5, relief="ridge", width=100, height=100)
# twoButton = ttk.Button(two, text="2")

# def ObjectMatrix(text):
#     lines = text.splitlines()

#     matrix = np.zeros([len(lines), len(lines[0])], dtype=np.object)

#     for i, line in enumerate(lines):
#         for j, char in enumerate(line):
#             matrix[i][j] = Node(char, [i, j])
#     return matrix

matrix = np.zeros(gridSize, dtype=np.object)

content.grid()

for col in range(len(matrix)):
    for row in range(len(matrix[col])):
        cell = matrix[col][row]
        cell[0] = ttk.Frame(content, borderwidth=5, relief="ridge", width=100, height=100)
        cell.pos = row * len(matrix) + col + 1
        print(cell.pos)
        cell[1] = ttk.Button(cell[0], text=f"{cell.pos}", command = lambda: print(cell.pos))

        
        for widget in cell:
            widget.grid(column=col, row=row)
        # matrix[col][row] = cell

# content.grid(column=0, row=0)
# one.grid(column=0,row=0)
# oneButton.grid(column=0,row=0)
# two.grid(column=1,row=0)
# twoButton.grid(column=1,row=0)

root.mainloop()
