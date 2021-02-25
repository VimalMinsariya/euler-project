a=1; b=1; n=2; length=1

while(length<1000):
    fn=b+a; n+=1
    s=str(fn); length=len(s)
    a=b; b=fn

print(n)
