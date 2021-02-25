import time
start = time.time()

def square_sum(n):
    result = 0
    son = str(n)
    for i in son:
        result += (int(i))**2
    return result

cnt = 0
n = 1
Limit = 10**7
memo_1 = {1}
memo_89 = {89}
while n < Limit:
    if n < (9**2)*7 + 1:
        k = n
        memo_temp = set()
        while k not in memo_1 | memo_89:
            if k < (9**2)*7 + 1:
                memo_temp.add(k)
            k = square_sum(k)
        if k in memo_1:
            memo_1 |= memo_temp
        else:
            memo_89 |= memo_temp
            cnt += 1
    else:
        if square_sum(n) in memo_89:
            cnt += 1
    n += 1

print(cnt)

print(time.time()-start)