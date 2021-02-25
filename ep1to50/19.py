import time
start = time.time()

def f(y,m):
    if m in [4,6,9,11]:
        return 30
    elif m in [1,3,5,7,8,10,12]:
        return 31
    elif m==2:
        if (y%4 == 0 and y%100 != 0) or (y%400 == 0):
            return 29
        else:
            return 28

count=0
week=1

for year in range(1900,2001):
    for month in range(1,13):
        if year>1900 and week == 0:
            count += 1
        week = (week+f(year,month))%7
# 테스트

"""
한글로 주석을 달아보자 
"""
print(count)
print(time.time()-start)