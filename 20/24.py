import time
start = time.time()

a=[]
for i in range(10):
    a.append([i])

def lex(a):
    lex = []
    n=len(a)
    for i in range(10):
        for j in range(n):
            if i not in a[j]:
                b=[i]+a[j]
                lex.append(b)
    return lex

result=a
for i in range(9):
    result=lex(result)


print(result[10**6-1])

print(time.time()-start)