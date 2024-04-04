s = []
res = 0

def mergesort(l, r) :
    global s
    global res
    if l == r :
        return 
    m = (l + r) // 2
    mergesort(l, m)
    mergesort(m + 1, r)
    s1 = s[l : m + 1]
    s2 = s[m + 1 : r + 1]
    n1 = len(s1)
    n2 = len(s2)
    pos1 = 0
    pos2 = 0
    for i in range(l, r + 1) :
        if pos1 == n1 :
            s[i] = s2[pos2]
            pos2 += 1
            continue
        if pos2 == n2 or s1[pos1] <= s2[pos2]:
            s[i] = s1[pos1]
            pos1 += 1
            res += pos2
        else :
            s[i] = s2[pos2]
            pos2 += 1

n = int(input())
for i in range(n) :
    s.append(int(input()))
res = 0
s.reverse()
mergesort(0, n - 1)
print(res)