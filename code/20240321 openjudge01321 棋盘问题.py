def bitcnt(n) :
    if n == 0 :
        return 0
    return bitcnt(n // 2) + n % 2
n = 0
m = 0
while True :
    n, m = input().split()
    n = int(n)
    m = int(m)
    #print(n, m)
    if n == -1 and m == -1 :
        break
    map = [[]]
    dp = [[1]]
    for i in range((1 << n) - 1) :
        dp[0].append(0)
    #print(dp)
    for i in range(n) :
        dp.append([0] * (1 << n))
    #print(dp)
    for i in range(n) :
        map.append(input())
    for i in range(1, n + 1) :
        for k in range(1 << n) :
            dp[i][k] = dp[i - 1][k]
        for j in range(n) :
            if map[i][j] == "#" :
                for k in range(1 << n) :
                    if (k & (1 << j)) > 0 :
                        dp[i][k] += dp[i - 1][k - (1 << j)]
        #print(dp[i])
    res = 0
    for i in range(1 << n) :
        if bitcnt(i) == m :
            res += dp[n][i]
    print(res)