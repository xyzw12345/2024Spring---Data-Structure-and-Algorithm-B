class info :
    def __init__(self, Cname, Sname, val) :
        self.Cname = Cname
        self.Sname = Sname
        self.val = val
    def __lt__(self, other) :
        return self.Sname < other.Sname

h = []
Numdict = {}
Sumdict = {}
n, x, y = map(int, input().split())
for i in range(n) :
    s = input().split()
    h.append(info(s[0], s[1], int(s[2])))
h = sorted(h)
m = int(input())
tmpNum = 0
tmpSum = 0
for i in range(n) :
    if i == 0 :
        tmpNum = 1
        tmpSum = h[i].val
    else :
        if h[i].Sname != h[i - 1].Sname :
            Numdict[h[i - 1].Sname] = tmpNum
            Sumdict[h[i - 1].Sname] = tmpSum
            tmpNum = 1
            tmpSum = h[i].val
        else :
            tmpNum += 1
            tmpSum += h[i].val
Numdict[h[n - 1].Sname] = tmpNum
Sumdict[h[n - 1].Sname] = tmpSum

for i in range(m) :
    s = input()
    if Numdict[s] >= x and Sumdict[s] / Numdict[s] > y :
        print("yes")
    else :
        print("no")



