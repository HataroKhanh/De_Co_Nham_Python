fi = open('b2.int','r')
fo = open('b2.out','w')

n = int(fi.readline())
a = fi.readline().split()
a = [int(i) for i in a]
x = int(fi.readline())
d=0
for i in range(n):
    for j in range(i+1,n):
        if a[i]+a[j]==x:
            d+=1
fo.write(str(d))

fo.close()
fi.close()
