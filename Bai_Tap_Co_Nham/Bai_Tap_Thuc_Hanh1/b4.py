a = int(input())
tong = 0
if 0 <= a <= 999:
    for i in str(a):
        tong += int(i)
    print(tong)