import time
start = time.time()

matrix=[\
    [131,673,234,103,18],\
   [201,96,342,965,150],\
   [630,803,746,422,111],\
   [537,699,497,121,956],\
   [805,732,524,37,331]\
    ]

matrix = [[int(num) for num in line.split(',')] for line in open('p081_matrix.txt')]
length = len(matrix)
matrix_min=[[matrix[i][j] for i in range(length)] for j in range(length)]

def min(m,n):
    if m < n :
        return m
    else:
        return n


for dia in range(2*length - 1):
    for row in range(length):
        col = dia - row
        if col >=0 and col < length:
            if row == 0 and col == 0:
                matrix_min[row][col] = matrix[row][col]
            elif row == 0 and col > 0:
                matrix_min[row][col] = matrix[row][col] + matrix_min[row][col-1]
            elif row > 0 and col == 0:
                matrix_min[row][col] = matrix[row][col] + matrix_min[row-1][col]
            else:
                matrix_min[row][col] = matrix[row][col] + min(matrix_min[row - 1][col], matrix_min[row][col-1])


min_path = [[0 for i in range(length)] for j in range(length)]
min_path[length-1][length-1] = 1
row, col = length-1, length-1
for i in range(2*length-1):
    if row>1:
        pre_row = row - 1
    else:
        pre_row = 0
    if col>1:
        pre_col = col - 1
    else:
        pre_col = 0
    a = matrix_min[pre_row][col]
    b = matrix_min[row][pre_col]
    if a < b:
        min_path[pre_row][col] = 1
        row = pre_row
    else:
        min_path[row][pre_col] = 1
        col = pre_col

for i in min_path:
    print(i)

print(time.time()-start)
