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
        if start not in self.edges or end not in self.edges :
            return -1
        dist = {}
        for i in self.edges :
            dist[i] = -1
        vis = set()
        q = [(0, start)]
        heapq.heapify(q)
        while q :
            d, u = heapq.heappop(q)
            #print(d, u)
            if u == end :
                return d
            if u in vis :
                continue
            dist[u] = d
            vis.add(u)
            for e in self.edges[u] :
                v, w = e
                if dist[u] + w < dist[v] or dist[v] == -1 :
                    dist[v] = dist[u] + w
                heapq.heappush(q, (dist[v], v))
        return -1

abs = lambda x : x if x >= 0 else -x
n, m, T = map(int, input().split())
q = []
for i in range(n) :
    q.append(input().split())
G = Graph()
for i in range(n) :
    for j in range(m) :
        if q[i][j] != "#" :
            G.addv((i, j))
for i in range(n) :
    for j in range(m) :
        dxs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dx in dxs :
            u, v = i + dx[0], j + dx[1]
            if (i, j) in G.edges and (u, v) in G.edges :
                G.addedge((i, j), (u, v), abs(int(q[i][j]) - int(q[u][v])))
for i in range(T) :
    u1, v1, u2, v2 = map(int, input().split())
    res = G.dijkstra((u1, v1), (u2, v2))
    print(res if res != -1 else "NO")