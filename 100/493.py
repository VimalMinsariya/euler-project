def main1():
    import random

    urn = list(range(70))
    random.shuffle(urn)
    try_number = 1
    num_color = 0
    test = 1
    while test != 0:
        for n in range(10000):
            color = set()
            try_choice = random.sample(urn,20)
            for i in try_choice:
                color.add(i//10)
            num_color += len(color)
            try_number += 1
        pbt = num_color / (try_number-1)
        print(pbt)
        test = input()

def main2():
    def permute(n,r):
        result = 1
        for i in range(n-r+1,n+1):
            result *= i
        return result

    def factorial(n):
        return permute(n,n)

    def choose(n,r):
        if r > n/2:
            r = n - r
        result = permute(n,r) / factorial(r)
        return result

    assert choose(7,3) == 35

    def H(n,r):
        return choose(n+r-1,r)

    sum = 0
    for k in range(2,8):
        sign = -1
        q = 0
        for j in range(k):
            sign *= -1
            if k-j > 1:
                q += sign * choose(k,j) * choose(10*(k-j),20)
        t = choose(7,k) * q
        sum += (k*t)

    total = choose(70,20)
    print(sum, total)
    print(sum/total)

def main3():
    n, d = 1, 1
    for i in range(41,51):
        n *= i
        d *= (20+i)
    result = 7 * (1 - n/d)
    print(result)

main3()