k={}
def c(i,j):
    if (i,j) in k:
        return k[(i,j)]
    if i == 0 or j == 0:
        v=1
        return v
    else:
        v = c(i-1,j) + c(i, j-1)
    k[(i,j)] = v
    return v
import time
start = time.time()
print(c(20,20))
print(time.time()-start)