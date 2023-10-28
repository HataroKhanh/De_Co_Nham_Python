def dequy8(n):
	if n<10:
		return n
	else:
		donvi = n%10
		xoadv = n//10
		return donvi+dequy8(xoadv)
with open('dequy8.int','r') as fi:
	n = int(fi.readline())
with open('dequy8.out','w') as fo:
	fo.write(str(dequy8(n)))
