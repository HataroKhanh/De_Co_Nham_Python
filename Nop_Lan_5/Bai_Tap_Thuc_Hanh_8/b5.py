i = int(input())
l = [int(i) for i in input().split()]
new_l = []
for a in range(len(l)):
    if l[a]==l[i]:
        continue
    new_l.append(l[a])
print(' '.join(str(i) for i in new_l))
    
    