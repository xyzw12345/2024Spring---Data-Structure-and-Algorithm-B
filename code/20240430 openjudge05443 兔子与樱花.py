import heapq

class Graph :
    def __init__(self) :
        self.edges = {}
    def addv(self, name) :
        self.edges[name] = []
    def addedge(self, u, v, w) :
        if u in self.edges and v in self.edges:
            self.edges[u].append((v, w))
    def dijkstra(self, start, end) :
        dist = {}
        prev = {}
        for i in self.edges :
            dist[i] = -1
        for i in self.edges :
            prev[i] = None
        dist[start] = 0
        vis = set()
        q = [(0, start)]
        heapq.heapify(q)
        while q :
            d, u = heapq.heappop(q)
            #print(d, u)
            if u == end :
                break
            if u in vis :
                continue
            dist[u] = d
            vis.add(u)
            for e in self.edges[u] :
                v, w = e
                if (dist[u] + w < dist[v] or dist[v] == -1) and v not in vis :
                    dist[v] = dist[u] + w
                    prev[v] = (u, v, w)
                heapq.heappush(q, (dist[v], v))
        return dist, prev
n = int(input())
G = Graph()
for i in range(n) :
    G.addv(input().strip())
m = int(input())
for i in range(m) :
    s = input().split()
    G.addedge(s[0], s[1], int(s[2]))
    G.addedge(s[1], s[0], int(s[2]))
T = int(input())
for i in range(T) :
    s = input().split()
    dist, prev = G.dijkstra(s[0], s[1])
    u = s[1]
    path = []
    while u != s[0] :
        path.append(prev[u])
        u = prev[u][0]
    path.reverse()
    print(s[0], end="")
    for p in path :
        print("->(", p[2], ")->", p[1], sep="", end="")
    print()
