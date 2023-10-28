from itertools import permutations

def Qd(n, x):
    la = permutations(x, 3)
    d = 0
    for i in range(n):
        for j in range(i + 1):
            a, b, c = la[j], la[j + 1], la[j + 2]
            delta = b ** 2 - 4 * a * c
            if (-b + delta ** 0.5) / (2 * a) == -1 or (-b - delta ** 0.5) / (2 * a) == -1:
                d += 1
    return d

print(Qd(3, [1, 2, 3]))
