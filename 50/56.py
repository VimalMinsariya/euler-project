import time
start = time.time()

def sumOfdigit(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum

max = 0
max_i = max_j = 0
for i in range(1,100):
    for j in range(1,100):
        if max < sumOfdigit(i**j):
            max = sumOfdigit(i**j)
            max_i = i
            max_j = j

print(f'{max_i}**{max_j} -> {max}')
print('Elapsed Time:',time.time()-start)