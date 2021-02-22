from tkinter import *
from copy import deepcopy

#Sudoke Solver funtions

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
    #we run out of range of our array, so we move to the next line
    if col == 9:
        row += 1
        col = 0

    if row == 9: #checking if sudoku is solved
        return True

    if sudoku[row][col] == "": #checking if there is any number in square 1x1
        for number in range(1, 10):
            if isPossible(sudoku, row, col, str(number)):#checking if it is possible to insert
                sudoku[row][col] = str(number) #filling sudoku array with values
            
                if solve(sudoku, row, col + 1):
                    return True

                sudoku[row][col] = ""
    else:
        if solve(sudoku, row, col + 1):
            return True  
#END OF SUDOKU SOLVER FUNCTIONS


#GUI CODE

def click():
    sudoku = [[" " for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            sudoku[j][i] = input_container[i][j].get()
    
    if solve(sudoku):
        for i in range(9):
            for j in range(9):
                input_container[j][i].set(sudoku[i][j])



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
        tab[i][j] = Entry(window, bd='1', fg='black', justify='center', font=("Canvas", 25, 'bold'), textvariable=input_container[i][j])
        #displaying entries on the window 
        
        tab[i][j].place(x = 45 + 50*i + (i//3)*7, y = 25 + 50*j + (j//3)*7, width=50, height=50)
 

#configuring button to get data with click function
Button(window, text="SOLVE", font=('Canvas', 10, 'bold'), width=5, command=click).place(x=40, y=500, width=60, height=40)


window.mainloop()