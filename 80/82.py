import time
start = time.time()

matrix = [[int(num) for num in line.split(',')] for line in open('p082_matrix.txt')]
length = len(matrix)

print(length)
print(time.time()-start)