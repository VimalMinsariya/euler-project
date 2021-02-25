import math
import time

def partial(r):
    # r == [N, a, b] -> r = (sqrt(N) + a)/b
    N, a, b = r
    q = int((math.sqrt(N)+a)/b)
    a = b*q - a
    b = (N - a**2)//b
    return [q,[N,a,b]]

def period(r):
    memo = []
    cf = []
    p_final = 0
    N = r[0]
    while True:
        q, v = partial(r)
        cf.append(q)
        if v in memo:
            p_start = memo.index(v)
            break
        memo.append(v)
        r = v
        p_final +=1
    x = p_final - p_start
    print(f'sqrt({N}) = {cf} | period = {x}')
    return x

def convert(N):
    return [N,0,1]

def main():
    start = time.time()
    cnt = 0
    for N in range(1,10000):
        test = math.sqrt(N)
        if test != int(test):
            k = period(convert(N))
            if k % 2 == 1:
                cnt += 1
    print(cnt)
    print(time.time() - start)

def test_ex():
    continued = True
    while continued:
        N = int(input('number = '))
        a = math.sqrt(N)
        if a == int(a):
            print('Oops!')
            continued = False
        else:
            x = period(convert(N))

main()
#test_ex()