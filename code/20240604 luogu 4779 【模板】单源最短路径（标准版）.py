import heapq

class Graph :
    def __init__(self) :
        self.edges = {}
    def addv(self, name) :
        self.edges[name] = []
    def addedge(self, u, v, w) :
        if u in self.edges and v in self.edges:
            self.edges[u].append((v, w))
    def dijkstra(self, start) :
        dist = {}
        for i in self.edges :
            dist[i] = -1
        vis = set()
        q = [(0, start)]
        heapq.heapify(q)
        while q :
            d, u = heapq.heappop(q)
            if u in vis :
                continue
            dist[u] = d
            vis.add(u)
            for e in self.edges[u] :
                v, w = e
                if dist[u] + w < dist[v] or dist[v] == -1 :
                    dist[v] = dist[u] + w
                heapq.heappush(q, (dist[v], v))
        return dist

n, m, s = map(int, input().split())
G = Graph()
for i in range(1, n + 1):
    G.addv(i)
for i in range(m):
    u, v, w = map(int, input().split())
    G.addedge(u, v, w)
d = G.dijkstra(s)
print(" ".join(str(d[i]) for i in range(1, n + 1)))
