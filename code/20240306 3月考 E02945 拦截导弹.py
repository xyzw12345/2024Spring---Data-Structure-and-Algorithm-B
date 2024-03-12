n = int(input())
s = list(map(int, input().split()))
dp = [0] * (n + 1)
res = 0
for i in range(n) :
    dp[i] = 1
    for j in range(i) :
        if s[j] >= s[i] :
            dp[i] = max(dp[i], dp[j] + 1)
    res = max(res, dp[i])
print(res)