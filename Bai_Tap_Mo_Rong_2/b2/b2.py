fi = open('b2.int', 'r')
fo = open('b2.out', 'w')

n = int(fi.readline())
di = []
for i in range(n):
    temp = fi.readline().split()
    ten = temp[0]
    namsinh = temp[1]
    diem = float(temp[2])
    hoc_sinh = (ten, namsinh, diem)
    di.append(hoc_sinh)
print(di)

sorted_di = sorted(di, key=lambda x: x[2])  

for hs in sorted_di:
    ten = hs[0]
    diem = hs[2]
    fo.write(f"{ten}: {diem}\n")  

fo.close()
