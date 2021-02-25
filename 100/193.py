import time
import copy
start = time.time()

"""primes = [2]
n = 3
while n < 100000:
    limit = int(n*(1/2)) + 1
    isPrime = True
    rank = 0
    while primes[rank] < limit:
        if n % primes[rank] == 0:
            isPrime = False
            break
        rank += 1
    if isPrime:
        primes.append(n)
    n += 2"""

seive_list = dict()
limit = 2**25
for i in range(2,limit+1):
    seive_list[i] = True
for p in seive_list:
    if p > int(limit**(1/2)):
        break
    else:
        if seive_list[p] == True:
            plus = 2*p
            while plus < limit+1:
                seive_list[plus] = False
                plus += p
        p += 1

squares = dict()
Limit = limit**2
cnt = 0
for i in seive_list:
    if seive_list[i] == True:
        p2 = i ** 2
        tmp = copy.deepcopy(squares)
        for square in tmp:
            k = square * p2
            if k < Limit:
                squares[k] = squares[square] + 1
                if squares[k] % 2 == 0:
                    cnt -= (Limit//k)
                else:
                    cnt += (Limit//k)
        squares[p2] = 1
        cnt += (Limit//p2)
        print(p2,cnt)
        input()

print(2**50-cnt)
print(time.time()-start)