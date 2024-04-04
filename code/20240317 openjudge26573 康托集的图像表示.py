def getC(n) :
    if n == 0 :
        return "*"
    s1 = getC(n - 1)
    return s1 + "-" * (3 ** (n - 1)) + s1

n = int(input())
print(getC(n))