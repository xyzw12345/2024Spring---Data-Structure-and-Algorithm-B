h = []
def getTopAndPop() :
    global h
    res = h[len(h) - 1]
    del(h[len(h) - 1])
    return res

n = int(input())
for i in range(n) :
    s = input().split()
    for item in s :
        if item == '+' :
            x = getTopAndPop()
            y = getTopAndPop()
            h.append(x + y)
        elif item == '-' :
            x = getTopAndPop()
            y = getTopAndPop()
            h.append(y - x)
        elif item == '*' :
            x = getTopAndPop()
            y = getTopAndPop()
            h.append(x * y)
        elif item == '/' :
            x = getTopAndPop()
            y = getTopAndPop()
            h.append(y / x)
        else :
            h.append(float(item))
        #print(h)
    print(f"{getTopAndPop() :.2f}")
        