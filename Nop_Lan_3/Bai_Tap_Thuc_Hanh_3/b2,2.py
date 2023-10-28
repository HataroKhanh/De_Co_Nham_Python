n = int(input())
e = 0
t = 1
for i in range(1,n+1):
    t = t * i
    e+=1/t
print(e)