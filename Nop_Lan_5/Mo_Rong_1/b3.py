n = int(input())
a =[]
for i in range(n):
    a.append(list(map(int,input().split())))
t1 = 0
t2 = 0
d1 = 0
for i in range(n):
    t1+=a[i][d1]
    t2+=a[i][n-1]
    d1+=1
print(t1)
print(t2)