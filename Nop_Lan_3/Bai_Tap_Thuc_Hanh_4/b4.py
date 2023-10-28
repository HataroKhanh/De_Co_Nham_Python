n = int(input())
check = True
for i in range(2,n):
    if n%i==0:
        check=False
if check == True:
    print('Yes')
else:
    print('No')
