N, W = map(int, input().split())
dp = [0] * (W + 1)
for i in range(N) :
    u, v = map(int, input().split())
    for k in range(0, W + 1) :
        j = W - k
        if j >= u :
            dp[j] = max(dp[j], dp[j - u] + v)
print(max(dp))