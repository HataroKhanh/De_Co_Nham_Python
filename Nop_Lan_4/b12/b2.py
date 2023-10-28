a = [float(i) for i in input().split()]
t = a[0]
duoi10=[]
for i in a:
    if i<10:
        duoi10.append(i)
        print(i,end=' ')
    if i>t:
        t=i
d = duoi10[0]
for i in duoi10:
    if d>i:
        d=i
print()
print(d)
print(t)