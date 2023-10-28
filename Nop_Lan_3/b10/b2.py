def AB(xa,ya,xb,yb):
    return ((xa-xb)**2+(ya-yb)**2)**0.5
a,b,c,d =map(float,input().split())
print(AB(a,b,c,d))