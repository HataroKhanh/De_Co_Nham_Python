t,n = map(int,input().split())
if t in [1,3,5,7,8,10,12]:
    print(31)
if t in [4,6,9,11]:
    print(30)
if t == 2:
    if n%400==0 or (n%4==0 and n%100!=0):
        print(29)
    else:
        print(28)