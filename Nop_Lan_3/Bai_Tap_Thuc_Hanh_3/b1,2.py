pi = 1
a = 1
for i in range(1,1000000):
    a = a+2
    if i % 2 ==1:
        pi = pi - 1/a
    else:
        pi = pi + 1/a
print(4*pi)