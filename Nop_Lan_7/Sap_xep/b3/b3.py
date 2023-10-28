def sapxep(n,a):
    for i in range(n):
        for j in range(i+1):
            if a[i]<a[j]:
                a[i],a[j]=a[j],a[i]
    return a
n = int(input())
a = [int(i) for i in input().split()][:n]
print(' '.join(str(i) for i in sapxep(n,a)) )
    