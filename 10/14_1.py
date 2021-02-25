import time
start = time.time()

mySaved = {}
def IterativeFunction(n) :
    n = int(n)
    mySaved[1] = 1
    count = 0
    if n in mySaved :
        return mySaved[n]
    else :
        count += 1
        if n % 2 == 0 :
            count += IterativeFunction(n/2)
        else :
            count += IterativeFunction(3*n+1)
        mySaved[n] = count
        return count

def LongestChainOfIterativeFunction(N) :
    bestNumber = -1
    bestScore = -1
    for n in range(1,N) :
        tempScore = IterativeFunction(n)
        if tempScore > bestScore :
            bestNumber = n
            bestScore = tempScore
    return bestNumber

#print(LongestChainOfIterativeFunction(100))
IterativeFunction(7)
print(mySaved)
print(7 in mySaved)

print("time :", time.time()-start)