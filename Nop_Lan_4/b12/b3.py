n = int(input())
a = [i for i in input().split()][:n]
for i in range(len(a)):
    for j in range(i + 1):
        if a[j] > a[i]:
            a[i], a[j] = a[j], a[i]
print(a)
