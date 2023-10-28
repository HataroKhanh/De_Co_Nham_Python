a = float(input())
b = float(input())
c = float(input())
if a+b>c and a+c>b and b+c>a:
	if a**2+b**2==c**2 or b**2+c**2==a**2 or a**2+c**2==b**2:
		print('la tam giac vuong')
	else:
		print("la 3 canh cua tam giac")
else:
	print('khong la ba canh tam giac')