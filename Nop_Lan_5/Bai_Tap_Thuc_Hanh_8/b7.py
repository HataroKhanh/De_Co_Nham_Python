a = [int(i) for i in input().split()]
for i in range(len(a)):
    for j in range(i+1):
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
print(' '.join(str(i) for i in a))
    