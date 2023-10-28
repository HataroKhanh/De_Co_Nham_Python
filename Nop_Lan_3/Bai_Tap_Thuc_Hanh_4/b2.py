n = int(input())
f1 = 1
f2 = 1
fi = 0
for i in range(3, n + 1):
    fi = f1 + f2
    f1 = f2
    f2 = fi
print(fi)
