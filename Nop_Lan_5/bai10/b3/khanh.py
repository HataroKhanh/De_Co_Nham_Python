def snt(n):
	for i in range(2,n):
		if n%i==0:
			return False
	return True
fi = open('fprime.int','r')
fo = open('fprime.out','w')
s = int(fi.readline())
d=2
l = ''
while s>=d:
	if s%d==0 and snt(d)==True:
		s=s/d
		l+=' ' + str(d)
	else:
		d+=1
if fi=='1':
	fo.write('1')
else:
	fo.write(l[1:])
fo.close()
