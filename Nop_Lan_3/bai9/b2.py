def api(n):
    pi = 1
    a = 1
    for i in range(1,n):
        a= a+2
        if i%a==1:
            pi = pi - 1/a
        else:
            pi = pi + 1/a
    return(4*pi)
print(api(123456))