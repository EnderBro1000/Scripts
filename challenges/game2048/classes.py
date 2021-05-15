import tkinter
from tkinter import *
from typing import Optional, Union
import numpy as np

class Matrix(Frame):


    def __init__(self, master, rows, cols):
        super().__init__(master)
        self.grid()
        self.matrix = np.zeros((rows, cols), dtype=Cell)
        for row in range(rows):
            for col in range(cols):
                self.setCell((row * cols + col + 1), row, col) # rows might be wrong, use cols instead
                


    def getCell(self, row, col):
        return self.matrix[row][col]

    def setCell(self, name, row, col):
        self.matrix[row][col] = Cell(master=self, name=name, row=row, col=col)



# class Cell(Frame):
    
#     def __init__(self, master: Optional[Misc], *, row=None, col=None, border: Union[str, float], borderwidth: Union[str, float], class_: str, cursor: tkinter._Cursor, height: tkinter._ScreenUnits, name: str, padding: tkinter._Padding, relief: tkinter._Relief, style: str, takefocus: tkinter._TakeFocusValue, width: tkinter._ScreenUnits) -> None: 
#         super().__init__(master=master, border=border, borderwidth=borderwidth, class_=class_, cursor=cursor, height=height, name=name, padding=padding, relief=relief, style=style, takefocus=takefocus, width=width)
#         self.grid(column=col, row=row)
#         self.name = name
#         self.row = row
#         self.col = col

        

#         self.button = Button(self, text=f"{self.name}", command = lambda: print(self.name))
#         print(f"cell constructed: {name}")

class Cell(Frame):
    
    def __init__(self, master=None, name=None, row=None, col=None, cnf={}, **kw):
        Frame.__init__(self, cnf=cnf, **kw)
        self.grid(column=col, row=row)
        self.name = name
        self.row = row
        self.col = col

        self.button = Button(self, text=f"{self.name}", command = lambda: print(self.name), font=("Arial", 25), width=3)
        self.button.grid(column=col, row=row)
        #print(f"cell constructed: {name}")
        

root = Tk()
content = Frame(root, borderwidth=5)
matrix = Matrix(content, 2, 5)

# matFrame = Frame(content)
# framecellption = Frame(matFrame)

root.mainloop()



#class Temp(Frame):
#    def __init__(self, master: Optional[tkinter.Misc], *, border: tkinter._ScreenUnits, borderwidth: tkinter._ScreenUnits, class_: str, cursor: tkinter._Cursor, height: tkinter._ScreenUnits, name: str, padding: tkinter._Padding, relief: tkinter._Relief, style: str, takefocus: tkinter._TakeFocusValue, width: tkinter._ScreenUnits) -> None:
#        super().__init__(master=master, border=border, borderwidth=borderwidth, class_=class_, cursor=cursor, height=height, name=name, padding=padding, relief=relief, style=style, takefocus=takefocus, width=width)