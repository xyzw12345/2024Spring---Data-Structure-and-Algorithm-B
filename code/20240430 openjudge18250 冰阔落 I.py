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
            return True
        u = self.sizes[x]
        v = self.sizes[y]
        self.rep[y] = x
        self.sizes[x] = u + v
        return False
    def count(self) :
        res = 0
        for item in self.rep :
            if self.getrep(item) == item :
                res += 1
        return res

while True :
    try :
        n, m = map(int, input().split())
        S = DisjointSet(list(i for i in range(1, n + 1)))
        for i in range(m) :
            u, v = map(int, input().split())
            flag = S.merge(u, v)
            if flag :
                print("Yes")
            else :
                print("No")
        print(S.count())
        for i in S.rep :
            if S.rep[i] == i :
                print(i, end = " ")
        print()
    except:
        break