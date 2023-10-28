s = input()
a = []
d = 0
for i in range(len(s)):
    if s[i]=='a':
        d+=1
        a.append(i)
a = [str(i) for i in a]
print(' '.join(a))
print(d)