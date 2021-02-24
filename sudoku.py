from tkinter import *

#Sudoke Solver functions

#function to check if it is possible to insert a number in square
def isPossible(sudoku, row, col, number):
  
    #checking if in row there is already no number that we want to insert
    for j in range(len(sudoku)):
        if j != col and sudoku[row][j] == number:
            return False

    #checking if in column there is already no number that we want to insert
    for i in range(len(sudoku)):
        if i != row and sudoku[i][col] == number:
            return False
    
    #checking if in square 3x3 there is already no number that we want to insert
    for i in range(3*(row//3), 3*(row//3) + 3):
        for j in range(3*(col//3), 3*(col//3) + 3):
            if i != row and j != col and sudoku[i][j] == number:
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

    elif solve(sudoku, row, col + 1):
        return True
#END OF SUDOKU SOLVER FUNCTIONS


#GUI CODE

#click() function gets data from user and prints solution to GUI 
def click():
    sudoku = [["" for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            sudoku[j][i] = input_container[i][j].get()
    
    #checking input from user
    temp = True
    valid_numbers = set(str(_) for _ in range(1, 10))
    for i in range(9):
        for j in range(9):
            if (sudoku[i][j] != "" and not isPossible(sudoku, i, j, str(sudoku[i][j]))) or\
                 sudoku[i][j] not in valid_numbers:
                temp = False
                break
    
    #if input is correct, solve sudoku, and fill the board with numbers
    if temp and solve(sudoku):
        for i in range(9):
            for j in range(9):
                input_container[j][i].set(sudoku[i][j])
    
    #if sudoku is not solvable, display the message
    else: 
        display_error = Label(window, text="This sudoku is not solvable, please enter valid numbers!", font=('Canvas', 15, 'bold'))
        display_error.place(x=5, y=200)
        window.after(4000, display_error.destroy)

#reset() function clears the whole board
def reset():
    for i in range(9):
        for j in range(9):
            input_container[j][i].set("")


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
        tab[i][j] = Entry(window, highlightthickness='0.5', highlightbackground='black', bd='0.5', fg='black', justify='center', font=("Canvas", 25, 'bold'), textvariable=input_container[i][j])
        
        #displaying entries on the window 
        tab[i][j].place(x = 45 + 50*i + (i//3)*7, y = 25 + 50*j + (j//3)*7, width=50, height=50)
 

#configuring "SOLVE" button to get data with click function
Button(window, text="SOLVE", font=('Canvas', 10, 'bold'), width=5, command=click).place(x=40, y=500, width=60, height=40)

#configuring "RESET" button to clear the whole board 
Button(window, text="RESET", font=('Canvas', 10, 'bold'), width=5, command=reset).place(x=120, y=500, width=60, height=40)

window.mainloop()