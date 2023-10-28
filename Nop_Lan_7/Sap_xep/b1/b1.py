def sort(n, a):
    for i in range(n):
        for j in range(i+1):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a
def book(a):
    r = [a[i:i+3] for i in range(0, len(a), 3)]
    print(a)
    print(r)
    for sublist in r:
        if len(sublist) == 3:
            del sublist[2]
    kq = 0
    for sublist in r:
        for num in sublist:
            kq += num
    return kq
with open('book.int', 'r') as fi:
    n = int(fi.readline())
    a = [int(i) for i in fi.readline().split()]
    a = sort(n, a)
    r = book(a)
with open('book.out', 'w') as fo:
    fo.write(str(r))