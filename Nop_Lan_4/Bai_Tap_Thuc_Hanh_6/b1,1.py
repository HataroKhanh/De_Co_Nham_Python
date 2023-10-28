s = input()
rs = ''
for i in range(1,len(s)+1):
    rs+=s[-i]
if s==rs:
    print('YES')
else:print('No')