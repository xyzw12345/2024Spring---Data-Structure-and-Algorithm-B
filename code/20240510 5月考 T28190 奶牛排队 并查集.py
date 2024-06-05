class DisjointSet :
    def __init__(self, items) :
        self.rep = dict(zip(items, items))
        self.siz = dict(zip(items, [1] * len(items)))
        self.maximum = dict(zip(items, items))
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
            self.maximum[self.rep[fu]] = max(self.maximum[fu], self.maximum[fv])
            return False

N = int(input())
h = []
for i in range(N) :
    h.append(int(input()))
qmax = []
qmin = []
D = DisjointSet(list(i for i in range(N)))
res = 0
for i in range(N) :
    while qmax and h[qmax[-1]] < h[i]:
        qmax.pop()
    qmax.append(i)
    while qmin and h[qmin[-1]] >= h[i] :
        D.merge(qmin[-1], qmin[-1] + 1)
        qmin.pop()
    qmin.append(i)  # qmin increase 
    #print(qmax, qmin)
    u = 0 if len(qmax) == 1 else qmax[-2]
    l = D.maximum[D.getrep(u)]
    res = max(res, i - l + 1 if l != i else 0)   
print(res) 
    


