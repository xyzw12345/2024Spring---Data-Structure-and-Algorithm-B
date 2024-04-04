def check(s1, s2, s3) :
    if len(s3) != len(s1) + len(s2) :
        return False
    if s1 == "" :
        return s2 == s3
    if s2 == "" :
        return s1 == s3
    n = len(s1)
    m = len(s2)
    dp = []
    for i in range(n + 1) : # dp[i][j] means check(s1[i : len(s1)], s2[j : len(s2)], s3[i + j : len(s3)])
        dp.append([False] * (m + 1))
    dp[n][m] = True
    for k in range(0, n + m) :
        u = n + m - k
        for i in range(max(u - m, 0), min(n, u) + 1) :
            j = u - i
            if i >= 1 and s1[i - 1] == s3[i + j - 1]:
                dp[i - 1][j] = dp[i - 1][j] or dp[i][j]
            if j >= 1 and s2[j - 1] == s3[i + j - 1]:
                dp[i][j - 1] = dp[i][j - 1] or dp[i][j]
        #print(dp)
    return dp[0][0]

N = int(input())
for case in range(1, N + 1) :
    u = input().split()
    if check(u[0], u[1], u[2]) :
        print(f"Data set {case}: yes")
    else :
        print(f"Data set {case}: no")