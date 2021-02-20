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

sudoku = [
[2,0,0,3,6,0,0,0,0],
[0,0,0,0,0,0,0,3,0],
[0,0,3,2,4,0,0,9,0],
[0,2,7,0,0,0,0,1,0],
[0,3,1,6,0,0,9,0,0],
[6,0,9,8,1,0,2,0,7],
[9,6,2,4,0,0,3,0,0],
[1,0,5,0,3,0,4,2,0],
[3,7,4,0,8,2,5,6,0]

]
for x in sudoku:
    print(x)