# 주어진 수 n의 각 자리수 분석 13352222888 -> {'0':0, '1':1, '2':4, ... , '9':0}
def resolve(n):
    sol = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    while n > 0:
        remainder = n % 10
        sol[remainder] += 1
        n = n // 10
    return sol


# n, 2*n, ... 6*n have the same digits?
def is_samedigits(n):
    sol1=resolve(n)
    if sol1 != resolve(2*n):
        return False
    elif sol1 != resolve(3*n):
        return False
    elif sol1 != resolve(4*n):
        return False
    elif sol1 != resolve(5*n):
        return False
    elif sol1 != resolve(6*n):
        return False
    else:
        return True


if __name__=='__main__':
    k = 2
    n= 10**k

    while is_samedigits(n) == False:
        if 6*n > 10**(k+1):
            k += 1
            n = 10 ** k
        n += 1

    print(n)