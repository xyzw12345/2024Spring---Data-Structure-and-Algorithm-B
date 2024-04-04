def getB(n) :
    if n == 0 :
        return [""]
    res = []
    for j in range(n) :
        k = n - 1 - j
        s1 = getB(j)
        s2 = getB(k)
        for u in s1 :
            for v in s2 :
                res.append("(" + u + ")" + v)
    return res

N = int(input())
s = getB(N)
s = sorted(s)
for item in s :
    print(item)