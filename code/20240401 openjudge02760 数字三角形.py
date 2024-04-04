N = int(input())
s = []
for i in range(N) :
    s.append(list(map(int, input().split())))
dp = [s[0][0]]
res = []
for i in range(1, N) :
    res = []
    for j in range(i) :
        res.append(dp[j] + s[i][j])
    res.append(dp[-1] + s[i][-1])
    for j in range(i) :
        res[j + 1] = max(res[j + 1], dp[j] + s[i][j + 1])
    dp = []
    for item in res :
        dp.append(item)
    #print(dp)
print(max(dp))