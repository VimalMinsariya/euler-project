a, b = 2, 1

def L(a,b):
    return a**2 + 4*a*b + 5*(b**2)

result = 0

for i in range(12):
    print(L(a,b))
    result += L(a,b)
    a, b = 2*a+5*b, a+2*b

print(result)