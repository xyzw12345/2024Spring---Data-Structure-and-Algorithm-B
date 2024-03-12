def splt(s) :
    list1 = []
    list2 = []
    for c in s :
        if c == '+':
            list1.append(list2)
            list2 = []
        else:
            list2.append(c)
    list1.append(list2)
    return list1
def splt1(s) :
    list1 = []
    list2 = []
    for c in s :
        if ord(c) < ord('0') or ord(c) > ord('9'):
            if list2 != [] :
                list1.append(list2)
                list2 = []
        else:
            list2.append(c)
    list1.append(list2)
    return list1

def getNum(s) :
    s1 = splt1(s)
    res = []
    tmp = 0
    for ss in s1 :
        tmp = 0
        for c in ss :
            tmp = tmp * 10 + ord(c) - ord('0')
        res.append(tmp)
    return res

s = input()
s1 = splt(s)
s2 = []
x = 0
y = 0
k = 0
for ss in s1 :
    s2 = getNum(ss)
    #print(s2)
    if len(s2) == 1 :
        x = 1
        y = s2[0]
    else :
        x = s2[0]
        y = s2[1]
    if y > k and x > 0 :
        k = y
print(f"n^{k}")