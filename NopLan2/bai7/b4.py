def khanh(x,y):
	if x>y:
		return x**2
	if x==y:
		return x+y
	if x<y:
		return y**2
x = int(input())
y = int(input())
print(khanh(x,y))