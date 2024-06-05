class DisjointSet :
    def __init__(self, items) :
        self.rep = dict(zip(items, items))
        self.siz = dict(zip(items, [1] * len(items)))
    def getrep(self, item) :
        if self.rep[item] == item :
            return item
        else :
            self.rep[item] = self.getrep(self.rep[item])
            return self.rep[item]
    def merge(self, u, v) :
        fu = self.getrep(u)
        fv = self.getrep(v)
        su = self.siz[fu]
        sv = self.siz[fv]
        if fu == fv :
            return True
        else :
            if su > sv :
                self.rep[fv], self.siz[fu] = fu, su + sv
            else :
                self.rep[fu], self.siz[fv] = fv, su + sv
            return False
    
N, M = map(int, input().split())
D = DisjointSet(list(i for i in range(N)))
tmp = N
flag1 = False
for i in range(M) :
    u, v = map(int, input().split())
    flag = D.merge(u, v)
    if flag :
        flag1 = True
    else :
        tmp = tmp - 1
print("connected:yes" if tmp == 1 else "connected:no")
print("loop:yes" if flag1 else "loop:no")