def songuyento(n):
    check = True
    kq =[]
    for i in range(2,n):
        if n%i==0:
            check =False
    a = 2
    while a<=(n+1) and check:
        for j in range(2,a):
            if (not a%j==0):
                kq.append(j)
        a+=1
    kq = [str(i) for i in kq]
    return (' '.join(kq))
n = int(input())
print(songuyento(n))