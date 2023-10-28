a,b,c = map(float,input().split())
if a**2+b**2==c**2 or b**2+c**2==a**2 or a**2+b**2==c**2:
    print('vuong')
elif a==b or a==c or c==b:
    if a==b==c:
        print('deu')
    else:
        print('can')
else:
    print('thuong')