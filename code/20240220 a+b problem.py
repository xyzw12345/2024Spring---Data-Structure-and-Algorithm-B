def splt(s) :
    list1 = []
    list2 = []
    for c in s :
        if c == ' ':
            list1.append(list2)
            list2 = []
        else:
            list2.append(c)
    list1.append(list2)
    return list1
def getInt(s) :
    a = 0
    sgna = 1
    for c in s :
        if c == '-' :
            sgna = - sgna
            continue
        if ord('0') <= ord(c) and ord(c) <= ord('9') :
            a = a * 10 + ord(c) - ord('0')
        if ord(c) < ord('0') or ord(c) > ord('9') :
            break
    return a * sgna
def readIntList() :
    s = input()
    sList = splt(s)
    IntList = []
    for ss in sList :
        IntList.append(getInt(ss))
    return IntList
def initWithZero(s) :
    if len(s) == 0 :
        return 0
    else :
        s1 = []
        for i in range(len(s)) :
            if i == 0 :
                continue
            else :
                s1.append(s[i])
        res = []
        for i in range(s[0]) :
            res.append(initWithZero(s1))
        return res

#s = readIntList()
#print(s[0] + s[1])

s1 = initWithZero([2,2,3])
print(s1)
