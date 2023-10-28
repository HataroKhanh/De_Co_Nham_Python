n = int(input())
if n<=2:
    fo=1
else:
    f1=1
    f2=1
    for i in range(3,n+1):
        fo = f1+f2
        f1,f2=f2,fo
print(fo)
    
    