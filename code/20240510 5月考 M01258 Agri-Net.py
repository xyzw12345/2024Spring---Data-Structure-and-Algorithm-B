import heapq

class Graph :
    def __init__(self) :
        self.edges = {}
    def addv(self, name) :
        self.edges[name] = []
    def addedge(self, u, v, w) :
        self.edges[u].append((v, w))
    def Prim(self, start) :
        res = 0
        q = [(0, start)]
        heapq.heapify(q)
        vis = set()
        while q :
            d, u = heapq.heappop(q)
            if u in vis :
                continue
            res += d
            for e in self.edges[u] :
                v, w = e
                heapq.heappush(q, (w, v))
            vis.add(u)
            #print(q, d, u)
        return res

n = int(input())
G = Graph()
for i in range(n) :
    G.addv(i)
for i in range(n) :
    tmp = 0
    while tmp < n :
        u = list(map(int, input().split()))
        for j in range(len(u)) :
            G.addedge(i, j + tmp, u[j])
        tmp += len(u)
print(G.Prim(0))