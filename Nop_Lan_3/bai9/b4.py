def nhom_nguoi(n):
    a=1
    for i in range(1,n+1):
        a*=i
    return a
print(nhom_nguoi(10))
print(nhom_nguoi(20))