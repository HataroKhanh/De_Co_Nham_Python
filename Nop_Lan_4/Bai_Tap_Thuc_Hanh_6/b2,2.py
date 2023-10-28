s = input()
rs =''
for i in range(len(s)):
    rs+=s[-i-1]
print(rs)