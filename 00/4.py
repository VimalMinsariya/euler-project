max=0
for i in range(100,1000):
    for j in range(i,1000):
        a=i*j
        #print(a)
        b=str(a)
        #print(b)
        c=len(b)
        #print(c)
        d=''
        for k in range(c):
            d += b[-k-1]
            #print(int(srt(d)))
        if b[-1] != '0':
            e = int(d)
            if a == e:
                print(i,j,a)
                if max<a:
                    max=a
print('max=',max)
