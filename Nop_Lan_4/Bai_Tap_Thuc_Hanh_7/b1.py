l = [int(i) for i in input().split()]
t = 0
tnhotb = []
for i in range(len(l)):
    t+=l[i]
for i in range(len(l)):
    if l[i]>(t/12):
        tnhotb.append(str(i+1))
print(t)
print(t/12)
print(' '.join(tnhotb))