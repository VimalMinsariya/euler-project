import time
start = time.time()

def mul_permutation(list,r):
    result = []
    if r == 0:
        return ['']
    else:
        for i in range(len(list)):
            for p in mul_permutation(list,r-1):
                result.append(list[i]+p)
        return result

keys = mul_permutation('abcdefghijklmnopqrstuvwxyz',3)
a = open('cipher1.txt').read().split(',')
l = len(a)

for key in keys:
    b = [ord(i) for i in key]
    text = ''
    sum = 0
    for i in range(l):
        t = i % 3
        sum += int(a[i])^b[t]
        text += chr(int(a[i])^b[t])
    j = 0
    while j < len(text) - 3:
        if text[j:j+3] == ' a ':
            print(sum, text)
            break
        j += 1


print('\n',time.time()-start)