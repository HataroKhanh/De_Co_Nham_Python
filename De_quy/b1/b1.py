def ucln(a,b):
	if b == 0:
		return a
	else:
		return ucln(b,a%b)
with open('dequy.int','r+') as khanh:
	a,b = [int(i) for i in khanh.readline().split()]
with open('dequy.out','w') as khanhout:
	khanhout.write(str(ucln(a,b)))	