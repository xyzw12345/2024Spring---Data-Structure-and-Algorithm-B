class node :
    def __init__(self, left, right) :
        self.left = left
        self.right = right

h = []
depth = []
size = []
resd = 0
ress = 0
def getdepth(s) :
    global h
    global depth
    if s == -1 :
        return -1
    if depth[s] != 0 :
        return depth[s]
    depth[s] = max(getdepth(h[s].left), getdepth(h[s].right)) + 1
    return depth[s]

def getsize(s) :
    global h
    global size
    if s == -1 :
        return 0
    if h[s].left == -1 and h[s].right == -1 :
        size[s] = 1
        return 1
    if size[s] != 0 :
        return size[s]
    size[s] = getsize(h[s].left) + getsize(h[s].right)
    return size[s]

n = int(input())
depth = [0] * n 
size = [0] * n
for i in range(n) :
    u, v = map(int, input().split())
    h.append(node(u, v))
for i in range(n) :
    resd = max(resd, getdepth(i))
for i in range(n) :
    ress = max(ress, getsize(i))
print(resd, end = " ")
print(ress)