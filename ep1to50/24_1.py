import time
from itertools import count

start = time.time()

a=count(10,2)

for i in enumerate(10):
    print(next(a))

print(time.time()-start)