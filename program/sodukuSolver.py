"""
이 프로그램은 프로젝트오일러(Eulerproject) 96번 문제 풀이를 응용한 것이다.
수도쿠 문제를 정해진 양식으로 입력하면, 해답을 출력하는 프로그램이다.
문제와 해답을 읽기 좋게 하기 위해, 바탕화면에 latex 형식으로 출력한다.
"""
import time
import sys

grid = []
for i in range(9):
    inputString = input(f'{i+1}번째 줄:')
    rlist = [int(s) for s in inputString]
    grid.append(rlist)

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

sudoku = grid
path = '/Users/yslee/Desktop/'
prefix = str(int(time.time())%10000)
fname = 'sudoku'+prefix+'.tex'
with open(path+fname,'w') as f:
    old = sys.stdout
    sys.stdout = f
    print('\\documentclass[11pt,a4paper]{article}')
    print('\\usepackage{sudoku}')
    print('\\begin{document}')
    print('\\begin{sudoku}')
    print_sudoku_latex(sudoku)
    print('\\end{sudoku}')
    print('\\begin{sudoku}')
    solveSudoku(sudoku)
    print_sudoku_latex(sudoku)
    print('\\end{sudoku}')
    print('\\end{document}')
    sys.stdout = old
