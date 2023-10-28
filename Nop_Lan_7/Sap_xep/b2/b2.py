def check(n, a):
    d = 0
    for i in range(n - 1):
        if a[i][0] == a[i + 1][0] and abs(a[i][1] - a[i + 1][1]) <= 60:
            d += 1
        else:
        	d=1
    return d
with open('coffe.int', 'r') as fi:
    n = int(fi.readline())
    a = []
    for i in range(n):
        l = [int(i) for i in fi.readline().split()]
        a.append(l)
d = check(n, a)
with open("coffe.out", 'w') as fo:
    fo.write(str(d))
