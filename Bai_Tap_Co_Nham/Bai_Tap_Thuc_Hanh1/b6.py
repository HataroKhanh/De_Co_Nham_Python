m = int(input())
n =int(input())
t = 1
for i in range(1,(m * n)+1):
    t *= 2
t-=1
print("tong so hat:", t)
