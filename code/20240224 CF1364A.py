nCases = int(input())
for case in range(nCases) :
    n, x = map(int, input().split())
    listNum = list(map(int, input().split()))
    Sum = [0] * (n + 1)
    for i in range(n) :
        Sum[i + 1] = Sum[i] + listNum[i]
    l = 0
    for i in range(1, n + 1) :
        if (Sum[i]) % x != 0 :
            l = i
            break
    if l == 0 :
        print("-1")
        continue
    r = 0
    for i in range(1, n + 1) :
        if (Sum[n + 1 - i] - Sum[n]) % x != 0 :
            r = n + 1 - i
            break
    if (Sum[n]) % x != 0 :
        print(f"{n}")
        continue
    else :
        print(f"{max(r, n - l)}")
