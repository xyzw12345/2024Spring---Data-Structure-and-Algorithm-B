h = []
root = None
N = 0
class SEGtreenode :
    def __init__ (self, left, right, maxpos, minpos) :
        self.left = left
        self.right = right
        self.maxpos = maxpos
        self.minpos = minpos

def build(l, r) :
    global h
    if l == r :
        return SEGtreenode(None, None, l, l)
    m = (l + r) // 2
    lson = build(l, m)
    rson = build(m + 1, r)
    lmax, lmin = lson.maxpos, lson.minpos
    rmax, rmin = rson.maxpos, rson.minpos
    return SEGtreenode(lson, rson, lmax if h[lmax] > h[rmax] else rmax, lmin if h[lmin] < h[rmin] else rmin)
def getmaxpos(u, l, r, x, y) :
    if l >= x and r <= y :
        return u.maxpos
    if r < x or l > y :
        return -1
    m = (l + r) // 2
    resl = getmaxpos(u.left, l, m, x, y)
    resr = getmaxpos(u.right, m + 1, r, x, y)
    return resl + resr + 1 if (resr == -1 or resl == -1) else (resl if h[resl] > h[resr] else resr)
def getminpos(u, l, r, x, y) :
    if l >= x and r <= y :
        return u.minpos
    if r < x or l > y :
        return -1
    m = (l + r) // 2
    resl = getminpos(u.left, l, m, x, y)
    resr = getminpos(u.right, m + 1, r, x, y)
    return resl + resr + 1 if (resr == -1 or resl == -1) else (resl if h[resl] < h[resr] else resr)    

def maxpos(l, r) :
    if l > r :
        return l
    global root, N
    return getmaxpos(root, 0, N - 1, l, r)
def minpos(l, r) :
    if l > r :
        return l
    global root, N
    return getminpos(root, 0, N - 1, l, r)
def calc(l, r) :
    if l >= r :
        return 0
    MAXpos = maxpos(l, r)
    MINpos = minpos(l, MAXpos - 1)
    return max(calc(l, MAXpos - 1), max(calc(MAXpos + 1, r), MAXpos - MINpos + 1 if MINpos != MAXpos else 0))

N = int(input())
for i in range(N) :
    h.append((int(input()), -i))
h = sorted(h)
for i in range(N) :
    h[i] = (-h[i][1], i + 1)
h = sorted(h)
for i in range(N) :
    h[i] = h[i][1]
root = build(0, N - 1)
print(calc(0, N - 1))

