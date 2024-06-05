class SegtreeNode:
    def __init__ (self, val = 0, left = None, right = None, lazy = 0):
        self.sum = val
        self.lazy = lazy
        self.left = left
        self.right = right
    def pushup(self):
        self.sum = (0 if not self.left else self.left.sum) + (0 if not self.right else self.right.sum)
    def pushdown(self, l, r):
        m = (l + r) // 2
        tmp = self.lazy
        self.lazy = 0
        if self.left:
            self.left.lazy += tmp
            self.left.sum += (m - l + 1) * tmp
        if self.right:
            self.right.lazy += tmp
            self.right.sum += (r - m) * tmp
        
    def update(self, l, r, x, y, k):
        if l > y or r < x:
            return
        if x <= l and r <= y:
            self.lazy += k
            self.sum += (r - l + 1) * k
            return
        m = (l + r) // 2
        self.pushdown(l, r)
        if self.left:
            self.left.update(l, m, x, y, k)
        if self.right:
            self.right.update(m + 1, r, x, y, k)
        self.pushup()
    
    def query(self, l, r, x, y):
        if l > y or r < x:
            return 0
        if x <= l and r <= y:
            return self.sum
        m = (l + r) // 2
        self.pushdown(l, r)
        return (0 if not self.left else self.left.query(l, m, x, y)) + (0 if not self.right else self.right.query(m + 1, r, x, y))

def buildtree(l, r, s):
    if l > r:
        return None
    if l == r :
        return SegtreeNode(s[l])
    m = (l + r) // 2
    p = SegtreeNode(0, buildtree(l, m, s), buildtree(m + 1, r, s))
    p.pushup()
    return p

n, m = map(int, input().split())
s = [0]
s.extend(list(map(int, input().split())))
root = buildtree(1, n, s)
for i in range(m):
    u = list(map(int, input().split()))
    if u[0] == 1:
        root.update(1, n, u[1], u[2], u[3])
    else:
        print(root.query(1, n, u[1], u[2]))
