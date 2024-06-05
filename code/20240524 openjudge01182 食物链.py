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
    def check(self, u, v):
        return self.getrep(u) == self.getrep(v)
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

N, K = map(int, input().split())
cnt = 0
D = DisjointSet(list(i for i in range(1, 3 * N + 1)))
for i in range(K) :
    op, u, v = map(int, input().split())
    if u > N or v > N:
        cnt += 1
        continue
    if op == 1:
        if D.check(u, v + N) or D.check(u, v + 2 * N) :
            cnt += 1
            continue
        D.merge(u, v)
        D.merge(u + N, v + N)
        D.merge(u + 2 * N, v + 2 * N)
    if op == 2:
        if D.check(u, v) or D.check(u, v + 2 * N) :
            cnt += 1
            continue
        D.merge(u, v + N)
        D.merge(u + N, v + 2 * N)
        D.merge(u + 2 * N, v)
print(cnt)