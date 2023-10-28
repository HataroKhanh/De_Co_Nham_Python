a =[]
n = int(input())
for i in range(n):
    a.append(list(map(int,input().split())))
d=0
t = 0
for i in range(n):
    for j in range(n):
        t+=a[i][j]
        if a[i][j]>d:
            d=a[i][j]
print(t)
print(d)