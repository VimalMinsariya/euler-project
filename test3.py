import time

a = 2**25
print(a)
test = '2'
while test != '1':
    N = 10**int(input())
    start = time.time()
    n = 1
    sum = 0
    while n < N:
        sum += n
        n += 1
    print(N, sum)
    print(time.time() - start)
