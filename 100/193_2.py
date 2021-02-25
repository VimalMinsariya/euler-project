import time
start = time.time()

seive_list = dict()
Limit = 2**50
limit = int(Limit**(1/2))
result = 2**50
mju = {1:[False,1,1]}

for d in range(1,limit+1):

    result += mju[d]*(Limit//(d**2))