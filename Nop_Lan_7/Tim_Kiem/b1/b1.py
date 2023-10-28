def tim_tien(x, a, n):
    max_tien = 0
    a.sort()
    if n < 2:
        return max_tien
    for i in range(n-1):
        temp = a[i] + a[i+1]
        if temp > x:
            break
        max_tien = max(max_tien, temp)
    return max_tien

with open('gift.int', 'r') as fi:
    n, x = map(int,fi.readline().split())
    a = list(map(int,fi.readline().split()))[:n]

d = tim_tien(x,a,n)

with open('gift.out', 'w') as fo:
    fo.write(str(d))
