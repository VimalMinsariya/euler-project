import math
import time
start = time.time()

def n_sol(P):
    m, n = P
    g = math.gcd(m,n)
    m1, n1 = m//g, n//g
    a, b = (m-x_limit)/n1, m/n1
    a, b = math.ceil(a), math.floor(b)
    c, d = -n/m1, (y_limit-n)/m1
    c, d = math.ceil(c), math.floor(d)
    list_t1 = [i for i in range(a,b+1)]
    list_t2 = [i for i in range(c,d+1)]
    t = set(list_t1).intersection(set(list_t2))
    return len(t)-1

def main():
    result = 0
    global x_limit, y_limit
    x_limit, y_limit = 50, 50

    for m in range(x_limit+1):
        for n in range(y_limit+1):
            if m>0 and n>0:
                P = [m,n]
                result += n_sol(P)
            elif m == 0 and n > 0:
                result += x_limit
            elif n == 0 and m > 0:
                result += y_limit
            elif m == 0 and n == 0:
                result += x_limit * y_limit
    print(result)

main()

print(time.time()-start)