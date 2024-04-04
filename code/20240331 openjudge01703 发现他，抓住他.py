class DisjointSet :
    def __init__(self, items) :
        self.sizes = dict(zip(items, [1] * len(items)))
        self.rep = dict(zip(items, items))
        self.length = len(items)
    def getrep(self, i) :
        if self.rep[i] == i :
            return i 
        res = self.getrep(self.rep[i])
        self.rep[i] = res
        return self.rep[i]
    def check_if_same(self, i, j) :
        return (self.getrep(i) == self.getrep(j))
    def merge(self, i, j) :
        x = self.getrep(i)
        y = self.getrep(j)
        if x == y :
            return
        u = self.sizes[x]
        v = self.sizes[y]
        if u < v :
            self.rep[x] = y
            self.sizes[y] = u + v
        else :
            self.rep[y] = x
            self.sizes[x] = u + v
    def count(self) :
        res = 0
        for item in self.rep :
            if self.getrep(item) == item :
                res += 1
        return res

T = int(input())
for Case in range(T) :
    N, M = map(int, input().split())
    s = DisjointSet([i for i in range(2 * N + 1)])
    for i in range(M) :
        u = input().split()
        x = int(u[1])
        y = int(u[2])
        if u[0] == 'A' :
            if s.check_if_same(x, y) :
                print("In the same gang.")
            elif s.check_if_same(x, N + y) :
                print("In different gangs.")
            else :
                print("Not sure yet.")
        if u[0] == 'D' :
            s.merge(x, N + y)
            s.merge(y, N + x)