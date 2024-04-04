while True :
    try :
        N = int(input())
        dp = []
        for i in range(N + 1) :
            dp.append([0] * (N + 1))
        dp[0][0] = 1    # the number of ways with maximum <= i, sum = j
        for i in range(1, N + 1) :
            for j in range(N + 1) :
                dp[i][j] = dp[i - 1][j]
                if j >= i :
                    dp[i][j] += dp[i][j - i]    
        res = 0
        print(dp[N][N])
    except:
        break




'''
u = [1,1,2,3,5,7,11,15,22,30,42,56,77,101,135,176,231,
 297,385,490,627,792,1002,1255,1575,1958,2436,3010,
 3718,4565,5604,6842,8349,10143,12310,14883,17977,
 21637,26015,31185,37338,44583,53174,63261,75175,
 89134,105558,124754,147273,173525,204226]
'''