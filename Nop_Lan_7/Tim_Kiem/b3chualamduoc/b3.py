with open('ghepcap.int','w') as fi:
    n = int(fi.readline())
    a = [int(i) for i in fi.readline().split()]
d = ghepcap(n,a)
with open('ghepcap.out','w') as fo:
    fo.write(str(d))