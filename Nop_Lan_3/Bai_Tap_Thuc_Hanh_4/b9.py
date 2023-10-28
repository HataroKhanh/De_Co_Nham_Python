n = input()
if n.isdigit():
    check = n[::-1]
    if check==n:
        print('Yes')
    else:
        print('No')
    
