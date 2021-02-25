def factorial(n):
    k = 1
    if n == 1:
        return n
    else:
        k = n * factorial(n-1)
    return k

def sumOfDigit(n):
    k=0
    while(n>9):
        k += n%10
        n = n//10
    return k+n

print(sumOfDigit(factorial(100)))

#for digit in str(factorial(100)):
#    print(digit,end=',') \

print((factorial(40))/(factorial(20)**2))
