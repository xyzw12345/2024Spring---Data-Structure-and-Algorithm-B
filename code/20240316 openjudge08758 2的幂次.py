def getstr(n) :
    if n == 0 :
        return "0"
    i = 0
    while (1 << (i + 1)) <= n :
        i += 1
    s1 = getstr(i)
    s2 = getstr(n - (1 << i))
    s3 = "2(" + s1 + ")"
    if i == 1 :
        s3 = "2"
    if n == 1 << i :
        return s3
    else :
        return s3 + "+" + s2
n = int(input())
print(getstr(n))