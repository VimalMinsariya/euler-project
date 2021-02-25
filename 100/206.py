import time
start = time.time()

def test(n):
     a = str(n)
     result = True
     if len(a) == 19:
         k = 0
         while 2*k < 18:
             if k+1 != int(a[2*k]):
                 result = False
                 break
             k += 1
     else:
         result = False
     return result

min = 10**7
max = (2**(1/2)) * (10**7)

s = min
while s < max:
    a = s*100 + 30
    b = s*100 + 70
    if test(a**2):
        print(a, a**2)
    if test(b**2):
        print(b, b**2)
    s += 1

print(time.time()-start)