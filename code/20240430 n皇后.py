def getres(now, m) :
    n = len(now)
    if n == m :
        return [now]
    else :
        res = []
        for j in range(m) :
            flag = True
            for k in range(n) :
                if j == now[k] or j - now[k] == n - k or j - now[k] == k - n :
                    flag = False
            if flag :
                res.extend(getres(now + [j], m))
        return res

m = int(input())
print(len(getres([], m)))