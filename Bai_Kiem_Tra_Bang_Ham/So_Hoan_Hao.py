def So_Hoan_Hao(n):
    t = 0
    for i in range(1, n):
        if n % i == 0:
            t += i
    return t == n
print(So_Hoan_Hao(28))
