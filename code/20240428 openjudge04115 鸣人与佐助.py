from collections import deque

class Graph :
    def __init__ (self) :
        self.edges = {}
    def addv(self, name) :
        self.edges[name] = []
    def addedge(self, u, v) :
        self.edges[u].append(v)
    def shortestpath(self, start, end) :
        q = deque()
        dist = {}
        dist[start] = 0
        q.append(start)
        while len(q) :
            u = q.popleft()
            for v in self.edges[u] :
                if v not in dist :
                    dist[v] = dist[u] + 1
                    q.append(v)         
        if end in dist :
            return dist[end]
        else :
            return -1
        
M, N, T = map(int, input().split())
q = []
for i in range(M) :
    q.append(input())
G = Graph()
for i in range(M) :
    for j in range(N) :
        for k in range(T + 1) :
            G.addv((i, j, k))
G.addv("end")
for i in range(M) :
    for j in range(N) :
        for k in range(T + 1) :
            if q[i][j] == "#" :
                dxs = [(0, 1, -1), (0, -1, -1), (1, 0, -1), (-1, 0, -1)]
            else :
                dxs = [(0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
            for dx in dxs :
                u, v, w = i + dx[0], j + dx[1], k + dx[2]
                if (u, v, w) in G.edges :
                    G.addedge((u, v, w), (i, j, k))
for i in range(M) :
    for j in range(N) :
        if q[i][j] == "@" :
            start = (i, j, 0)
        if q[i][j] == "+" :
            end = (i, j)
for k in range(T + 1) :
    G.addedge((end[0], end[1], k), "end")
res = G.shortestpath(start, "end")
print(res - 1 if res != -1 else -1)