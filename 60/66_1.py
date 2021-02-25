import time
import math
start = time.time()

def cf(a,k,D):
    r = (a + math.sqrt(D))/k
    z = int(r)
    a = k*z - a
    k = (D - a**2)//k
    return [z,(a,k,D)]

def cftof(list):
    p, q = list[-1],1 # q/p
    if len(list) > 1:
        for t in range(len(list)-1):
            p_temp, q_temp = p, q
            p = list[-t-2]*p_temp + q_temp
            q = p_temp
    return [p,q]

def min_sol(D):
    c_fraction = []
    z,r = cf(0,1,D)
    a,k,D = r
    c_fraction.append(z)
    x, y = cftof(c_fraction)
    while x**2 - D*y**2 != 1:
        z, r = cf(a,k,D)
        c_fraction.append(z)
        x, y = cftof(c_fraction)
        a,k,D = r
    print(c_fraction)
    return [x,D,y]

def main():
    max = 0
    result = 0
    for D in range(2,1001):
        test = math.sqrt(D)
        if test != int(test):
            x,D,y = min_sol(D)
            print(x,D,y)
            if x > max:
                max = x
                result = D
    print('result:',result)

main()
