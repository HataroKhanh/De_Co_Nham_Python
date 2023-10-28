s = input()
new_s = ""
boqua = False
for i in s:
    if i == ' ':
        if not boqua:
            new_s+=' '
        boqua = True
    else:
        new_s+=i
        boqua = False
print(new_s)