import time
start=time.time()

nameList = sorted([x.replace('"','') for x in open('p022_names.txt').readline().split(',')])
print(sum([((ord(j)-ord('A')+1)*(nameList.index(i)+1)) for i in nameList for j in i]))

print("Elapsed Time: ",time.time()-start)