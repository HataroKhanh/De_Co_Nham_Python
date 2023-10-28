
def hang(a,n,m):
    temp = 0

    for i in range(n):
        tong = 0
        for j in range(m):
            tong+=a[i][j]
    if tong>temp:
        temp = tong
    return temp
def cot(a,n,m):
    temp = 0
    for i in range(m):
        tong = 0
        for j in range(n):
            tong += a[j][i]
        if tong>temp:
            temp = tong
    return temp

n,m = map(int,input().split())
a = []
for i in range(n):
    a.append(list(map(int,input().split()))[:m])
print(hang(a,n,m))
print(cot(a,n,m))