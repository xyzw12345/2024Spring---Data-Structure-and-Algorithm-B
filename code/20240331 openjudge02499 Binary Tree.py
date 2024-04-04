def getLR(x, y) :
    if y == 1 :
        return x - 1, 0
    if x == 1 :
        return 0, y - 1
    if x > y :
        u, v = getLR(x % y, y)
        return x // y + u, v
    else :
        u, v = getLR(x, y % x)
        return u, y // x + v

T = int(input())
for case in range(1, T + 1) :
    n, m = map(int, input().split())
    print(f"Scenario #{case}:")
    u, v = getLR(n, m)
    print(u, v)
    print("")