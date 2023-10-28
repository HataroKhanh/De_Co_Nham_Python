def ghepcap(n,a):
    d = 0
    for i in range(n):
        for j in range(i+1):
            if 9/10*a[j] <= a[i] <= a[j]:
                d+=1
    return d
print(ghepcap(6,[100,89,90,101,91,99]))
with open('ghepcap.int','r') as fi:
    n = int(fi.readline())
    a = [int(i) for i in fi.readline().split()]
d = ghepcap(n,a)
with open('ghepcap.out','w') as fo:
    fo.write(str(d))