import time
import itertools
start = time.time()

matrix=[\
    [131,673,234,103,18],\
   [201,96,342,965,150],\
   [630,803,746,422,111],\
   [537,699,497,121,956],\
   [805,732,524,37,331]\
    ]


matrix = [[int(num) for num in line.split(',')] for line in open('p081_matrix.txt')]

def min_path_sum(matrix,path_start,path_finish):
    s_m = path_start[0]
    s_n = path_start[1]
    f_m = path_finish[0]
    f_n = path_finish[1]
    m = f_m - s_m
    n = f_n - s_n
    result = 10**8
    path = list(itertools.combinations(range(m + n), n))
    for p in path:
        y = s_m
        x = s_n
        sum = matrix[s_m][s_n]
        for i in range(m+n):
            if i in p:
                x += 1
            else:
                y += 1
            sum += matrix[y][x]
        if sum < result:
            result = sum

    return result

for i in range(40):
    print(min_path_sum(matrix,[0,0],[i,40-i]))

print(time.time()-start)