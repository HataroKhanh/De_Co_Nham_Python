def dequy5(n):
	if n==1:
		return 1
	else:
		return dequy5(n-1)+n
print(dequy5(3))
with open('dequy5.int','r') as fi:
	n = int(fi.readline())
with open('depuy5.out','w') as fo:
	fo.write(str(dequy5(n)))

