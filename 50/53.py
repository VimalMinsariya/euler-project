def permutation(n,r):
    result = 1
    for i in range(n,n-r,-1):
        result *= i
    return result

def factorial(n):
    return permutation(n,n)

def C(n,r):
    return int(permutation(n,r)/factorial(r))

total = 4
k=9
for i in range(24,101):
    while C(i,k) > 10**6:
        k -= 1
    total += (i+1) - 2*(k+1)
    k = k + 1
    print(i,k)

print(total)

