import math
import time

start = time.time()

def isSquare(n):
    test = math.sqrt(n)
    if test == int(test):
        return True
    else:
        return False

assert(isSquare(3**3-2) == True)

sum_perimeter = 0
limit = 10**9

s,p = 1, 16
while p < limit:
    if isSquare(3*s**2+1):
        a = 4*s**2+1
        print(a,a,a+1,'=>', p)
        sum_perimeter += p
    s += 1
    p = 12*s**2 + 4

s,p = 3, 50
while p < limit:
    if isSquare(3*s**2-2):
        a = 2*s**2 - 1
        print(a,a,a-1,'=>', p)
        sum_perimeter += p
    s += 2
    p = 6*s**2 - 4

print(sum_perimeter)

print(time.time()-start)