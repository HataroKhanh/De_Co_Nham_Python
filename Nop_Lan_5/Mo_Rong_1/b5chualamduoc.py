def trai(a):
    new_a = []
    for i in a:
        new = i[:len(i)-1] 
        new_a.append(new_row)
    return new_a
def phai(a):
    new_a = []
    for i in a:
        new = i[len(i)-1:] 
        new_a.append(new)
    return new_a
def trai(a):
    new_a = []
    for i in a:
        new = i[:len(i)-1] 
        new_a.append(new)
    return new_a
def trai(a):
    new_a = []
    for i in a:
        new = i[:len(i)-1] 
        new_a.append(new)
    return new_a


    
n = int(input())
a =[]
for i in range(n):
    a.append(list(map(int,input().split())))
new_a = phai(a)
for i in new_a:
    print(" ".join(str(num) for num in i))