def snt(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def ucln(a,b):
    while b!=0:
        t = b
        b=a%b
        a=t
    return a
l = [int(i) for i in input().split()]
d=0
for i in range(len(l)):
    if snt(l[i]):
        d+=1
    for j in range(1,i):
        uclnn = ucln(l[i],l[j])
print(d)
print(uclnn)    

    