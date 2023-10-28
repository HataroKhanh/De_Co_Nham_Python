fi = open('b1.int', 'r')
fo = open('b1.out', 'w')
n = int(fi.readline())
l = []
for i in range(n):
    a = fi.readline().split()
    l.append(a)
maxx = 0
for i in range(n):
    for j in range(i + 1, n):
        xA = int(l[i][0])
        xB = int(l[j][0])
        yA = int(l[i][1])
        yB = int(l[j][1])
        t = abs(xA - xB) + abs(yA - yB)
        if t >= maxx:
            maxx = t
fo.write(str(maxx))
fi.close()
fo.close()
