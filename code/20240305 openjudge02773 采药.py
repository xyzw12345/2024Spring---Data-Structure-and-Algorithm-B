class herb :
    def __init__(self, time, val) :
        self.val = val
        self.time = time

T, M = map(int, input().split())
h = []
dp = []
for i in range(M) :
    x, y = map(int, input().split())
    h.append(herb(x, y))
for i in range(M + 1) :
    dp.append([0] * (T + 1))
for i in range(1, M + 1) :
    for j in range(T + 1) :
        u = h[i - 1].time
        v = h[i - 1].val
        if j >= u:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - u] + v)
        else :
            dp[i][j] = dp[i - 1][j]
res = 0
for i in range(T + 1) :
    res = max(res, dp[M][i])
print(res)