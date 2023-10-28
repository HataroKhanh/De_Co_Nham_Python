from snt import songuyento

n = int(input())
if n%2==0:
    l = []
    for i in range(2,n+1):
        if songuyento(i):
            l.append(i)
    for j in range(len(l)):
        for i in range((len(l)//2)+1):
            if l[j]+l[i]==n:
                print(l[j],l[i])