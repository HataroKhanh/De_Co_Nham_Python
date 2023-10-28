s = input()
if s[-3:]=='.py' and len(s)>3  and s.count('.')==1:
    print('YES')
else:
    print('NO')