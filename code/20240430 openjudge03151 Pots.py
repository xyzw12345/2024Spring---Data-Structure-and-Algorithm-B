from collections import deque

class Graph:
    def __init__ (self) :
        self.edges = {}
    def addv(self, u) :
        self.edges[u] = []
    def adde(self, u, v, w) :
        self.edges[u].append((v, w))
    def bfs_for_shortest_path(self, start, end) :
        dist = {}
        dist[start] = 0
        vis = set()
        q = deque()
        q.append(start)
        prev = {}
        while q :
            u = q.popleft()
            if u in vis :
                continue
            vis.add(u)
            for e in self.edges[u] :
                v, w = e
                if v not in vis and v not in dist:
                    dist[v] = dist[u] + 1
                    prev[v] = (u, w)
                    q.append(v)
        if end not in dist :
            return -1
        else :
            u = end
            path = []
            while u in prev and u != start :
                e = prev[u]
                path.append(e[1])
                u = e[0]
            path.reverse()
            return path

A, B, C = map(int, input().split())
G = Graph()
for i in range(A + 1) :
    for j in range(B + 1) :
        G.addv((i, j))
G.addv("end")
for i in range(A + 1) :
    if (i, C) in G.edges :
        G.adde((i, C), "end", "")
for i in range(B + 1) :
    if (C, i) in G.edges :
        G.adde((C, i), "end", "")
for i in range(A + 1) :
    for j in range(B + 1) :
        G.adde((i, j), (0, j), "DROP(1)")
        G.adde((i, j), (i, 0), "DROP(2)")
        G.adde((i, j), (A, j), "FILL(1)")
        G.adde((i, j), (i, B), "FILL(2)")
        G.adde((i, j), (max(i + j - B, 0), min(i + j, B)), "POUR(1,2)")
        G.adde((i, j), (min(i + j, A), max(i + j - A, 0)), "POUR(2,1)")
res = G.bfs_for_shortest_path((0, 0), "end")
if res == -1 :
    print("impossible")
else :
    print(len(res) - 1)
    for i in range(len(res) - 1) :
        print(res[i])
            