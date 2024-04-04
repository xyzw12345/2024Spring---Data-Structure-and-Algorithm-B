from collections import deque
n, k = map(int, input().split())
dp = [-1] * (2 * max(n, k) + 1)
q = deque([n])
dp[n] = 0
while dp[k] == -1 :
    u = q.popleft()
    if u >= 1 and dp[u - 1] == -1 :
        dp[u - 1] = dp[u] + 1
        q.append(u - 1)
    if 2 * u < len(dp) and dp[2 * u] == -1 :
        dp[2 * u] = dp[u] + 1
        q.append(2 * u)
    if u + 1 < len(dp) and dp[u + 1] == -1 :
        dp[u + 1] = dp[u] + 1
        q.append(u + 1)
print(dp[k])