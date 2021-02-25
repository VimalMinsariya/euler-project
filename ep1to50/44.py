#ㄷㅏㅂ은 나왔으나, 제대로 된 해법이 아님.

import time
start = time.time()

def P(n):
    return n*(3*n-1)//2

def isPN(n):
    test = (1+(1+24*n)**(1/2))/6
    if test == int(test):
        return True
    else:
        return False

first = 1
k = 2
test = True
while test:
    large = P(k)
    for j in range(1,k):
        small = P(j)
        if small >= 3*k + 1:
            if first == 1:
                if isPN(large - small) and isPN(large + small):
                    min = large - small
                    k_limit = (min + 2) / 3
                    first += 1
                    print(small, large, min)
            else:
                if k >= k_limit:
                    test = False
                else:
                    if isPN(large - small) and isPN(large + small):
                        if large - small < min:
                            min = large - small
                            print(small, large, min)
    k += 1

print(min)

print(time.time()-start)