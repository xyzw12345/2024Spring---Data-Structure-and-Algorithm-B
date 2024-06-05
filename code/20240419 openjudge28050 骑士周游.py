import random

class Graph:
    def __init__(self) :
        self.vertices = dict()
    def addVertices(self, names) :
        for name in names :
            if name not in self.vertices :
                self.vertices[name] = []
    def addedge(self, u, v) : # directed edge
        self.vertices[u].append(v)
    def askHamiltonPath(self, u, target_level, level = 1, vis = None, path_until_now = None, shuffle = False, pr = 0) :
        #print(u, target_level, level)
        if vis is None :
            vis = set([u])
            path_until_now = [u]
        if level == target_level :
            return path_until_now
        ss = self.vertices[u]
        if shuffle :
            r = random.random()
            if r < pr :
                random.shuffle(ss)
        s2 = []
        for s in ss :
            tmp = 0
            for p in self.vertices[s] :
                if p not in vis :
                    tmp += 1
            s2.append(tmp)
        t = zip(ss, s2)
        t = sorted(t, key=lambda x : x[1])
        for v, _ in t :
            if v not in vis :
                vis.add(v)
                path_until_now.append(v)
                res = self.askHamiltonPath(v, target_level, level + 1, vis=vis, path_until_now=path_until_now, shuffle=shuffle, pr = pr * 0.99)
                if res :
                    return res
                vis.remove(v)
                path_until_now.pop()
        return []

flag = False
RES = [[], [], [], [], []]
for n in range(22, 30) :
    RES.append([])
    for i in range(n) :
        RES[-1].append([])
        for j in range(n) :
            RES[-1][i].append(False)
    V = []
    for i in range(n) :
        for j in range(n) :
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
            if 0 <= xx and xx < n and 0 <= yy and yy < n :
                G.addedge((z, w), (xx, yy))
    for x in range(n) :
        for y in range(n) :
            if n % 2 == 1 and (x + y) % 2 == 1 :
                continue
            if RES[-1][x][y] :
                continue
            if RES[-1][y][x] :
                RES[-1][x][y] = list((u[1], u[0]) for u in RES[-1][y][x])
                continue
            res = G.askHamiltonPath((x, y), n * n, shuffle = True if (n, x, y) in [(22, 3, 9), (22, 7, 11)] else False, pr = 0.05)
            if res :
                print(n, x, y, "success")
                RES[-1][x][y] = res
                RES[-1][n - 1 - x][y] = list((n - 1 - u[0], u[1]) for u in res)
                RES[-1][x][n - 1 - y] = list((u[0], n - 1 - u[1]) for u in res)
                RES[-1][n - 1 - x][n - 1 - y] = list((n - 1 - u[0], n - 1 - u[1]) for u in res)
            else :
                print(n, x, y, "fail")
                flag = True
        if flag :
            break
    if flag :
        break

while True :
    n, x, y = map(int, input().split())
    print(RES[n][x][y])
    