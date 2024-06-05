class DisjointSet :
    def __init__(self, item) :
        self.rep = dict(zip(item, item))
        self.size = dict(zip(item, [1] * len(item)))
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


T = int(input())
for Case in range(T) :
    s = []
    n, m = map(int, input().split())
    for i in range(n) :
        s.append(input())
    U = []
    for i in range(n) :
        U.extend((i, j) for j in range(m))
    u = DisjointSet(U)
    steps = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, -1), (1, 1)]
    for step in steps :
        for i in range(n) :
            for j in range(m) :
                x = i + step[0]
                y = j + step[1]
                if 0 <= x and x < n and 0 <= y and y < m and s[i][j] == s[x][y] :
                    u.merge((i, j), (x, y))
    res = 0
    for i in range(n) :
        for j in range(m) :
            if s[i][j] == "W" :
                res = max(res, u.getsize((i, j)))
    print(res)
