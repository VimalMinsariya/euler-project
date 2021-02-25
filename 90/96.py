import time

grids = open("p096_sudoku.txt").readlines()

def open_sudoku(k):
    grid = [[], [], [], [], [], [], [], [], []]
    for i in range(9):
        for j in range(9):
            grid[i].append(int(grids[10*k+1 + i][j]))
    return grid

def print_sudoku(grid):
    print("\n|-----------------------|")
    for i in range(9):
        print("|", end=" ")
        for j in range(9):
            if j % 3 == 2:
                print(grid[i][j],end=' | ')
            else:
                print(grid[i][j], end=' ')
        if i%3 == 2:
            print("\n|-----------------------|")
        else:
            print("\r")

def print_sudoku_latex(grid):
    for i in range(9):
        print('|', end='')
        for j in range(9):
            num = grid[i][j]
            if num == 0:
                print(' |',end='')
            else:
                print(f"{num}|",end='')
        print(".")

def findUnassignedLocation(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return [i,j]
    return False

def noConflicts(sudoku, row, col, num):
    return not usedInRow(sudoku, row, num) and not usedInCol(sudoku, col, num) and not usedInBox(sudoku, row-row%3, col-col%3, num)

def usedInRow(sudoku, row, num):
    for i in range(9):
        if sudoku[row][i] == num:
            return True
    return False

def usedInCol(sudoku, col, num):
    for i in range(9):
        if sudoku[i][col] == num:
            return True
    return False

def usedInBox(sudoku, row, col, num):
    for i in range(3):
        for j in range(3):
            if sudoku[row+i][col+j] == num:
                return True
    return False

def solveSudoku(sudoku):
    if not findUnassignedLocation(sudoku):
        return True
    else:
        row, col = findUnassignedLocation(sudoku)
        for i in range(1,10):
            if noConflicts(sudoku, row, col, i):
                sudoku[row][col] = i
                if solveSudoku(sudoku):
                    return True
                sudoku[row][col] = 0
    return False

def main():
    result = 0
    start = time.time()
    for k in range(50):
        sudoku = open_sudoku(k)
        print_sudoku(sudoku)
        solveSudoku(sudoku)
        sum = sudoku[0][0]*100 + sudoku[0][1]*10 + sudoku[0][2]
        result += sum
        print_sudoku(sudoku)
        print(k,' | 3-digit numbers:', sum)
        print(time.time() - start)
        start = time.time()
        print("============================")
    print(result)

def main_latex():
    select = int(input("select number:"))
    sudoku = open_sudoku(select)
    print_sudoku_latex(sudoku)
    print("\n")
    solveSudoku(sudoku)
    print_sudoku_latex(sudoku)

#main()
main_latex()