class Graph:
    def __init__(self) :
        self.edges = {}
    def addv(self, u) :
        self.edges[u] = []
    def adde(self, u, v) :
        self.edges[u].append(v)
    def get_connected_component(self) :
        res = 0
        vis = {}
        for u in self.edges :
            vis[u] = 0
        for u in self.edges :
            if vis[u] == 1 :
                continue
            res += 1
            q = [u]
            while len(q) != 0 :
                v = q[-1]
                q.pop()
                if vis[v] == 1 :
                    continue
                vis[v] = 1
                for w in self.edges[v] :
                    if vis[w] == 0 :
                        q.append(w)
        return res

q = []
for i in range(10) :
    q.append(input())
G = Graph()
for i in range(10) :
    for j in range(10) :
        if q[i][j] == "." :
            G.addv((i, j))
for i in range(10) :
    for j in range(10) :
        for dx in [(1, 0), (-1, 0), (0, 1), (0, -1)] :
            if (i, j) in G.edges and (i + dx[0], j + dx[1]) in G.edges :
                G.adde((i, j), (i + dx[0], j + dx[1]))
print(G.get_connected_component())