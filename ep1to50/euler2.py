f0=1
f1=1
fibo=f1+f0
while(fibo < 50):
	fibo=f1+f0
	f0=f1
	f1=fibo
	if(fibo%2==0):
		fibo_even=fibo
		fibo1_even=f0
print((2*fibo_even+fibo1_even)/2)
