fi = open('3seq.int','r')
fo = open('3seq.out','w')
a = fi.readlines()
d=0
for i in range(len(a)):
    t = sum(([int(i) for i in a[i].split()]))
    if t>int(d):
        d = t


fo.write(str(d))
fo.close()
fi.close()