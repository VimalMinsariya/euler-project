import time
start=time.time()

words1=['','one','two','three','four','five','six','seven','eight','nine', \
'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
words2=['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

cnt_words1 = [len(s) for s in words1]
cnt_words2 = [len(s) for s in words2]


def cnt(n):
    r = n%100
    p = n//100
    cnt = 0
    if p > 0 and p < 10:
        cnt += cnt_words1[p] + len('hundred')
        if r > 0:
            cnt += len('and')

    if r<20:
        cnt += cnt_words1[r]
    else:
        r1 = r // 10
        r2 = r % 10
        cnt += cnt_words2[r1-2]+cnt_words1[r2]
    return cnt

result = 0
for i in range(1,1000):
    result += cnt(i)
print(result+11)

print("elapsed time= ",time.time()-start)