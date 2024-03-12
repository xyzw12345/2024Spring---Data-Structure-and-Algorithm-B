class node :
    def __init__ (self, left, right) :
        self.left = left
        self.right = right
nodePool = [None]
depth = []

def getdepth(u) :
    global nodePool
    if u == -1 :
        return 0
    if depth[u] != 0 :
        return depth[u]
    depth[u] = max(getdepth(nodePool[u].left), getdepth(nodePool[u].right)) + 1
    return depth[u]

n = int(input())
depth = [0] * (n + 1)
for i in range(n) :
    u, v = map(int, input().split())
    nodePool.append(node(u, v))
print(getdepth(1))
