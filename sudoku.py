from tkinter import *
from copy import deepcopy

#function to check if it is possible to insert a number in square
def isPossible(sudoku, row, col, number):
    
    #checking if in row there is already no number that we want to insert
    for j in range(len(sudoku)):
        if sudoku[row][j] == number:
            return False

    #checking if in column there is already no number that we want to insert
    for i in range(len(sudoku)):
        if sudoku[i][col] == number:
            return False
    
    #checking if in square 3x3 there is already no number that we want to insert
    for i in range(3*(row//3), 3*(row//3) + 3):
        for j in range(3*(col//3), 3*(col//3) + 3):
            if sudoku[i][j] == number:
                return False

    return True            


def solve(sudoku, row=0, col=0):
    if row == 9: #checking if sudoku is solved
        global tab
        tab = deepcopy(sudoku)
        return

    if col > 8: #checking if col is not out of range
        return

    #checking if there is any number inserted in square 1x1 
    if sudoku[row][col] == 0:
        for number in range(1, 10):
            if isPossible(sudoku, row, col, number):#checking if it is possible to insert
                sudoku[row][col] = number #filling sudoku array with values
                if col < 8:
                    solve(sudoku, row, col + 1)
                else:
                    solve(sudoku, row + 1, 0)

        else:
            sudoku[row][col] = 0

    #if there is number inserted in square 1x1 keep going
    else:
        if col < 8:
            solve(sudoku, row, col + 1)
        else:
            solve(sudoku, row + 1, 0)


sudoku = [
[8,0,4,0,0,5,1,0,6],
[5,0,6,7,0,8,0,0,0],
[0,9,0,0,0,6,8,7,5],
[0,6,1,0,8,0,9,0,2],
[0,0,0,2,9,0,0,0,7],
[0,0,2,0,4,0,0,0,1],
[0,3,0,1,0,0,0,6,0],
[0,2,0,0,0,0,7,3,0],
[0,8,0,3,0,2,0,0,4]
]
tab = []
solve(sudoku)
for x in tab:
    print(x)

#setting up window
window = Tk()
#setting up window title
window.title('Sudoku Solver')
#setting up resolution of window
window.geometry('550x550')

#array containing our Entries
tab = [[" " for _ in range(9)] for _ in range(9)]
#array of numbers inputed by user
input_container = [[StringVar() for _ in range(9)] for _ in range(9)]


for i in range(9):
    for j in range(9):
        #configuring entry and saving it to the array, so we can easily access it
        tab[i][j] = Entry(window, bd='4', fg='black', justify='center', font=("Canvas", 25, 'bold'), textvariable=input_container[i][j])
        #displaying entries on the window
        tab[i][j].place(x=45 + 50*i, y = 25 + 50*j, width=50, height=50)      


window.mainloop()