def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def uclna(a):
    uc = a[0]
    for i in range(1, len(a)):
        uc = ucln(uc, a[i])
    return uc
a = [int(i) for i in input().split()]
print(uclna(a))