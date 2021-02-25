import time
start = time.time()

def combination(list,r):
    result = []
    if len(list) == r and r > 0:
        return [list]
    elif r == 0:
        return [[]]
    else:
        first = list[0]
        remLst = list[1:]
        for p in combination(remLst,r-1):
                result.append([first]+p)
        for p in combination(remLst,r):
                result.append(p)
        return result

def asterisk(n,m):
    ast = []
    a = dict()
    q = str(n)
    digit = 0
    for num in q:
        if num in a:
            a[num].append(digit)
        else:
            a[num] = [digit]
        digit += 1
    for digit in a:
        if len(a[digit]) >= m:
            b = combination(a[digit],m)
            for com in b:
                k = ''
                for digit in range(len(q)):
                    if digit in com:
                        k += '*'
                    else:
                        k += q[digit]
                ast.append(k)
    return ast

def main():
    primes = [2]
    table = dict()
    cnt = 1
    n = 3
    c = 1
    while c != '0':
        limit = int(n**(1/2)) + 1
        isPrime = True
        for d in primes:
            if d < limit:
                if n%d == 0:
                    isPrime = False
                    break
            else:
                break
        if isPrime == True:
            primes.append(n)
            if len(str(n)) > len(str(n-1)):
                table = {}
            t = len(str(n))
            l = []
            for i in range((t-1)//3):
                l += asterisk(n,3*(i+1))
            for k in l:
                if k in table:
                    table[k].append(n)
                else:
                    table[k] = [n]
                if len(table[k]) == 9:
                    c = '0'
                    print(k,table[k])
                    break
            cnt += 1
        n += 2

main()
print(time.time()-start)