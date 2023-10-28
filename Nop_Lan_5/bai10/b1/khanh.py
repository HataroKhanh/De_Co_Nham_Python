fi = open('khanh.int','r')
fo = open('khanh.out','w')
s = fi.readline()
a = [int(i) for i in s.split()]
if a[1]/a[0]==a[2]/a[1]:
	fo.write('Yes')
else:
	fo.write('No')
fo.close()