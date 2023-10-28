from snt import songuyento
def sosinhdoi(n):
    kq =[]
    for i in range(2,n+1):
        if songuyento(i) and songuyento(i+2):
            kq.append((i,i+2))
    return kq
print(sosinhdoi(1000))
