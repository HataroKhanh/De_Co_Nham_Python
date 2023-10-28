m =int(input())
n =int(input())
k =int(input())
if m>0 and n>0 and k>0:
    if m//10!=0 and n//10!=0 and k//10!=0 and (m*n*k)%10==0:
        print('Yes')
    else:
        print('No')
    