class DisjointSet :
    def __init__(self, item, size) :
        self.rep = dict(zip(item, item))
        self.size = dict(zip(item, size))
    def getrep(self, x) :
        if not x in self.rep :
            return None
        if self.rep[x] == x :
            return self.rep[x]
        self.rep[x] = self.getrep(self.rep[x])
        return self.rep[x]
    def merge(self, x, y) :
        if (not x in self.rep) or (not y in self.rep) :
            return
        u = self.getrep(x)
        v = self.getrep(y)
        if u == v :
            return 
        if self.size[u] >= self.size[v] :
            self.rep[v] = u
            self.size[u] += self.size[v]
            return
        v, u = u, v
        self.rep[v] = u
        self.size[u] += self.size[v]
        return
    def getsize(self, x) :
        if not x in self.rep :
            return 0
        return self.size[self.getrep(x)]

n, m = map(int, input().split())
s = list(map(int, input().split()))
A = DisjointSet(list(i for i in range(n)), s)
for i in range(m) :
    u, v = map(int, input().split())
    A.merge(u, v)
print(max(A.getsize(u) for u in range(n)))