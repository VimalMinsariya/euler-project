import time
start = time.time()

data = [[int(n) for n in s.split()] for s in open('p067_triangle.txt').readlines()]
n=len(data)
data_new=[]
data_new.append(data[0])
for i in range(1,n):
    k=[]
    for j in range(i+1):
        if j == 0:
            k.append(data[i][j]+data_new[i-1][j])
        elif j == i:
            k.append(data[i][j]+data_new[i-1][j-1])
        else:
            k.append(max(data[i][j]+data_new[i-1][j-1],data[i][j]+data_new[i-1][j]))
    data_new.append(k)

max = 0
for i in range(n):
    if data_new[n-1][i]>max:
        max = data_new[n-1][i]
print(max)
print("Elapsed Time = ", time.time()-start)