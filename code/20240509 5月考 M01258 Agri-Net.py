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

while True :
    try :
        N = int(input())
        E = []
        for i in range(N) :
            tmp = 0
            while tmp < N :
                u = list(map(int, input().split()))
                for j in range(len(u)) :
                    E.append((u[j], i, j + tmp))
                tmp += len(u)   
        E = sorted(E)
        D = DisjointSet(list(i for i in range(N)))
        ans = 0
        for e in E :
            flag = D.merge(e[1], e[2])
            if not flag :
                ans += e[0]
        print(ans)
    except :
        break