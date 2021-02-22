from tkinter import *
from copy import deepcopy


def click():
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
            nonlocal tab_pom
            tab_pom = deepcopy(sudoku)
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
    

    sudoku = [[" " for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            sudoku[j][i] = tab1[i][j].get()
    
    tab_pom = []
    solve(sudoku)
    for i in range(9):
        for j in range(9):
            tab1[j][i].set(tab_pom[i][j])
#end function


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
        tab[i][j] = Entry(window, highlightbackground='black', highlightthickness=1, bd='0', fg='black', justify='center', font=("Canvas", 25, 'bold'),
         textvariable=input_container[i][j])
        #displaying entries on the window
        tab[i][j].place(x=45 + 50*i, y = 25 + 50*j, width=50, height=50)      

#configuring button to get data with click function
Button(window, text="SOLVE", font=('Canvas', 10, 'bold'), width=5, command=click).place(x=40, y=500, width=60, height=40)


window.mainloop()