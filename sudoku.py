import numpy as np

sudoku = np.array([[0,6,0,4,2,0,0,0,1],
                   [1,9,0,0,8,3,0,2,0],
                   [0,0,2,0,1,0,7,0,0],
                   [0,0,0,8,7,0,5,0,0],
                   [0,5,1,3,4,9,0,0,2],
                   [4,0,3,0,5,0,0,8,0],
                   [6,0,5,1,3,2,0,0,0],
                   [7,0,4,0,0,8,0,1,0],
                   [0,1,0,0,6,0,8,5,0]]).reshape(9,9)

def valid(y,x,n):
    global sudoku
    for i in range(0,9):
        if sudoku[y][i] == n:
            return False
    for i in range(0,9):
        if sudoku[i][x] == n:
            return False
    x0 = (x//3) * 3
    y0 = (y//3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if sudoku[y0+i][x0+j] == n:
                return False
    return True

def backTrack():
    global sudoku
    for y in range(9):
        for x in range(9):
            if sudoku[y][x]== 0:
                for n in range(1,10):
                    if valid(y,x,n):
                        sudoku[y][x] = n
                        backTrack()
                        sudoku[y][x] = 0
                return
    print(sudoku)


backTrack()

