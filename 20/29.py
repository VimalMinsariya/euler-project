import time
start=time.time()

list=[]

for a in range(2,101):
    for b in range(2,101):
        c=a**b
        if not(c in list):
            list.append(c)
print(len(list))
print("Elapsed Time: ",time.time()-start)