def isPrime(n):
    result = True
    limit = (n+1)**(1/2)
    if n % 2 == 0:
        result = False
    else:
        k = 3
        while k < limit:
            if n % k == 0:
                result = False
                break
            k += 2
    return result

print(isPrime(25))
def permutation(list,r):
    result = []
    if r == 0:
        return [[]]
    else:
        for i in range(len(list)):
            remLst = list[:i]+list[i+1:]
            for p in permutation(remLst,r-1):
                result.append([list[i]]+p)
        return result

def ndigit_pandigital(n):
    ndigit = [i for i in range(1,n+1)]
    ndigits_permute = permutation(ndigit,n)
    result =[]
    for i in ndigits_permute:
        k = 0
        for j in i:
            k = 10*k + j
        result.append(k)
    return result

n = 2
max = 0
while n<10:
    k = ndigit_pandigital(n)
    for j in k:
        if isPrime(j) and j > max:
            max = j
    n += 1

print(max)