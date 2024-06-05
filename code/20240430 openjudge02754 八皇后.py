def getres(now) :
    n = len(now)
    if n == 8 :
        return [now]
    else :
        res = []
        for j in range(8) :
            flag = True
            for k in range(n) :
                if j == now[k] or j - now[k] == n - k or j - now[k] == k - n :
                    flag = False
            if flag :
                res.extend(getres(now + [j]))
        return res

T = int(input())
res = getres([])
for i in range(T) :
    u = int(input())
    print("".join(str(j + 1) for j in res[u - 1]))