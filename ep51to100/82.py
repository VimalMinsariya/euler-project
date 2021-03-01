import time
start = time.time()

matrix = [[int(num) for num in line.split(',')] for line in open('p082_matrix.txt')]
"""
matrix = [[131, 673, 234, 103, 18],\
          [201,96, 342, 965, 150],\
          [630, 803, 746, 422, 111],\
          [537, 699, 497, 121, 956],\
          [805, 732, 524, 37, 331],\
          ]
"""
length = len(matrix)
sum_matrix = [[matrix[i][0]] for i in range(length)]
print(sum_matrix)

def add_matrix(row,col):
    test = []
    for k in range(length):
        if k <= row:
            s = sum_matrix[k][col-1] + sum([matrix[t][col] for t in range(k,row+1)])
            test.append(s)
        else:
            s = sum_matrix[k][col-1] + sum([matrix[t][col] for t in range(row,k+1)])
            test.append(s)
    return min(test)

for col in range(1,length):
    for row in range(length):
        sum_matrix[row].append(add_matrix(row,col))

print(min([sum_matrix[row][length-1] for row in range(length)]))
print(time.time()-start)