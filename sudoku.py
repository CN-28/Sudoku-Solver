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

import time
def solve(sudoku,row=0, col=0):
    if col > 8 or row > 8:
        return

    if row == 8 and col == 8:
        temp_alt = True
        for x in sudoku:
            if x.count(0) != 0:
                temp_alt = False
                break
        if temp_alt:
            for x in sudoku:
                print(x)
            exit(0)

    if sudoku[row][col] == 0:
        for number in range(1, 10):
            temp = False
            if isPossible(sudoku, row, col, number):
                temp = True
                sudoku[row][col] = number
                
                
                if col < 8:
                    solve(sudoku, row, col + 1)
                elif col == 8 and row < 8:
                    solve(sudoku, row + 1, 0)

        else:
            sudoku[row][col] = 0
            return
            
    else:
        if col < 8:
            solve(sudoku, row, col + 1)
        elif col == 8 and row < 8:
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

solve(sudoku)
