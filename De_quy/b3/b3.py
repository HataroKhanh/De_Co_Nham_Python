def dequy3(x,n):
	if n == 1:
		return x
	else:
		return x*dequy3(x,n-1)
with open('dequy3.int','r') as fi:
	x,n=[int(i) for i in fi.readline().split()]
with open('dequy3.out','w') as fo:
	fo.write(str(dequy3(x,n)))