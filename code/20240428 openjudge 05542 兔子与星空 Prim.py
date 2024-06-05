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
    G.addv(chr(ord('A') + i))
for i in range(n - 1) :
    s = input().split()
    for j in range(1, int(s[1]) + 1) :
        G.addedge(s[0], s[2 * j], int(s[2 * j + 1]))
        G.addedge(s[2 * j], s[0], int(s[2 * j + 1]))
print(G.Prim('A'))