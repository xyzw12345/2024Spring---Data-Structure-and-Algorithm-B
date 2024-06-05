from collections import deque

class Graph :
    def __init__ (self) :
        self.edges = {}
        self.type = {}
    def addv(self, name, type) :
        self.edges[name] = []
        self.type[name] = type
    def addedge(self, u, v) :
        self.edges[u].append(v)
    def shortestpath(self, start, end, T) :
        q = deque()
        dist = {}
        dist[(start, 0)] = 0
        q.append((start, 0))
        while len(q) :
            u = q.popleft()
            for v in self.edges[u[0]] :
                if self.type[v] == 1 :
                    if (v, u[1] + 1) in dist :
                        continue
                    if u[1] == T :
                        continue
                    dist[(v, u[1] + 1)] = dist[u] + 1
                    q.append((v, u[1] + 1))
                else :
                    if (v, u[1]) in dist :
                        continue
                    if v == end :
                        return dist[u] + 1
                    dist[(v, u[1])] = dist[u] + 1
                    q.append((v, u[1]))
        return -1
M, N, T = map(int, input().split())
q = []
for i in range(M) :
    q.append(input())
G = Graph()
for i in range(M) :
    for j in range(N) :
        for k in range(T + 1) :
            G.addv((i, j), 1 if q[i][j] == "#" else 0)
for i in range(M) :
    for j in range(N) :
            dxs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx in dxs :
                u, v = i + dx[0], j + dx[1]
                if (u, v) in G.edges :
                    G.addedge((u, v), (i, j))
for i in range(M) :
    for j in range(N) :
        if q[i][j] == "@" :
            start = (i, j)
        if q[i][j] == "+" :
            end = (i, j)
res = G.shortestpath(start, end, T)
print(res)