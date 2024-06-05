class Vertex :
    def __init__ (self) :
        self.adj = set()
    def addedge(self, other) :
        self.adj.add(other)
class Graph :
    def __init__ (self, vertices, edges = []) :
        self.vertices = {}
        for item in vertices :
            self.vertices[item] = Vertex()
        for edge in edges :
            self.addedge(edge[0], edge[1])
    def addedge (self, u, v) :
        self.vertices[u].addedge(v)
        self.vertices[v].addedge(u)
    def getdeg (self, v) :
        return len(self.vertices[v].adj)
    def checkedge (self, u, v) :
        if v in self.vertices[u].adj :
            return 1
        return 0
n, m = map(int, input().split())
G = Graph(list(i for i in range(n)))
for i in range(m) :
    u, v = map(int, input().split())
    G.addedge(u, v)
print("\n".join(" ".join(str(-G.checkedge(i, j) if i != j else G.getdeg(i)) for j in range(n)) for i in range(n)))
