fi = open('b1.int','r')
fo = open('b1.out','w')

n = int(fi.readline())
di = []
for i in range(n):
	temp = fi.readline().split()# ["Lan",'18/9/2006','8.8']
	ten = temp[0]
	namsinh = temp[1]
	diem = float(temp[2])
	hoc_sinh = [ten,namsinh,diem]
	di.append(hoc_sinh)
print(di)
dmax = max(temp,key=lambda x:x[2])
for i in di:
	if maxx in i:
		fo.writelines(f"Ho Ten: {i[0]}\n" )
		fo.writelines(f'Ngay Sinh: {i[1]}\n')
		fo.writelines(f'Diem Thi Trung Binh: {i[2]}\n')
fo.close()
