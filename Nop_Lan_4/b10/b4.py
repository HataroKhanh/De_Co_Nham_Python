from numpy import sqrt
def khanh(ax,ay,bx,by,cx,cy,dx,dy):
    AC = sqrt((ax + cx)**2+(ay + cy)**2)
    AB = sqrt((ax + bx)**2+(ay + by)**2)
    BC = sqrt((bx + cx)**2+(by + cy)**2)
    AD = sqrt((ax + dx)**2+(ay + dy)**2)
    DC = sqrt((dx + cx)**2+(dy + cy)**2)
    p1 = (AB + BC + AC)/2
    p2 = (AD + DC + AC)/2
    d1 = sqrt(p1 *(p1 - AB)*(p1 - BC)*(p1 - AC))
    d2 = sqrt(p1 *(p1 - AD)*(p1 - DC)*(p1 - AC))
    return (d1+d2)
a,b,c,d,e,g,h,i=map(float,input().split())
print(khanh(a,b,c,d,e,g,h,i))