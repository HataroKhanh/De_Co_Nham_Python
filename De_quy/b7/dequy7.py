def dequy7(n):
	if n == 1:
		return 1
	else:
		return n**2+dequy7(n-1)
with open('dequy7.int','r') as fi:
	n = int(fi.readline())
with open('dequy7.out','w') as fo:
	fo.write(str(dequy7(n)))
