x=153
y=int(x)
s=0
while y!=0:
    r=int(y%10)
    r=r*r*r
    s=s+r
    y=int(y/10)
if x==s:
    print("yes")
else:
    print("No")
    
