def gcd(a,b):
	while b!=0:
		a,b=b,a%b
	return a
fi = open('gcdseq.int','r')
fo = open('gcdseq.out','w')
s = fi.readline()
a = list(map(int,s.split()))
ucln = gcd(a[0],a[1])
if all(i%ucln==0 for i in a):
	fo.write(str(ucln))
fo.close()

