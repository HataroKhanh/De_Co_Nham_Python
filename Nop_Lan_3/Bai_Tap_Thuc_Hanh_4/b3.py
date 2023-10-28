n = int(input())
d = 2
while d<=n:
    if n%d==0:
        print(d,end=' ')
        n=n/d
    else:
        d+=1
