class Graph:
    def __init__(self) :
        self.vertices = dict()
    def addVertices(self, names) :
        for name in names :
            if name not in self.vertices :
                self.vertices[name] = []
    def addedge(self, u, v) : # directed edge
        self.vertices[u].append(v)
    def countHamiltonPath(self, u, target_level, level = 1, vis = None) :
        #print(u, target_level, level)
        if vis is None :
            vis = set([u])
        if level == target_level :
            return 1
        ans = 0
        for v in self.vertices[u] :
            if v not in vis :
                vis.add(v)
                ans += self.countHamiltonPath(v, target_level, level + 1, vis=vis)
                vis.remove(v)
        return ans

T = int(input())
for _ in range(T) :
    n, m, x, y = map(int, input().split())
    V = []
    for i in range(n) :
        for j in range(m) :
            V.append((i, j))
    G = Graph()
    G.addVertices(V)
    dxs = [(1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-2, 1), (-1, -2), (-2, -1)]
    for v in V :
        z, w = v
        for dx in dxs :
            dz, dw = dx
            xx = z + dz
            yy = w + dw
            if 0 <= xx and xx < n and 0 <= yy and yy < m :
                G.addedge((z, w), (xx, yy))
    print(G.countHamiltonPath((x, y), n * m))
        