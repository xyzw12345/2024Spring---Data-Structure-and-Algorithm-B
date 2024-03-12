n = int(input())
res = 0
for a1 in range(n - 29, n + 1) :
    for a2 in range(n - 29, n + 1) :
        for a3 in range(n - 29, n + 1) :
            if (a1 + a2) % 2 != 0 :
                continue
            if (a2 + a3) % 3 != 0 :
                continue
            if (a1 + a2 + a3) % 5 != 0 :
                continue
            res = max(res, a1 + a2 + a3)
print(res)