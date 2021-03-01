from time import thread_time

def isPalindrome(n):
    s1 = str(n)
    s2 = ''
    for num in s1:
        s2 = num + s2
    if s1 == s2: return True
    return False

def palindrom(n: int) -> int:
    pal = 0
    while n>0:
        n, r = divmod(n, 10)
        pal = pal * 10 + r
    return pal

max = 0
a = 999
while a > 99:
    b = 999
    while b >= a:
        p = a*b
        if p <= max: break
        if p == palindrom(p): max = p
        b -= 1
    a -= 1
print('max=',max)

print(thread_time())