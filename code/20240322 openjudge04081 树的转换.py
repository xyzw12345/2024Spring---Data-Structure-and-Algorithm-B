class Binnode :
    def __init__ (self, left, right) :
        self.left = left
        self.right = right
    def depth (self) :
        d1 = -1
        d2 = -1
        if self.left != None :
            d1 = self.left.depth()
        if self.right != None :
            d2 = self.right.depth()
        return max(d1, d2) + 1

class Multinode :
    def __init__ (self, sons) :
        self.sons = sons 
    def depth (self) :
        res = -1
        for son in self.sons :
            res = max(res, son.depth())
        return res + 1
    
def ToBinTree (u) : # u is a list of MultiNodes, corresponding to the sons of a certain nodes
    if u == [] :
        return None
    if len(u) == 1 :
        return Binnode(ToBinTree(u[0].sons), None)
    return Binnode(ToBinTree(u[0].sons), ToBinTree(u[1 : len(u)]))

def build(dep, nowdp) :
    seplist = []
    for i in range(len(dep)) :
        if dep[i] == nowdp :
            seplist.append(i)
    listnode = []
    for i in range(len(seplist) - 1) :
        listnode.append(build(dep[seplist[i] : seplist[i + 1] + 1], nowdp + 1))
    return Multinode(listnode)


s = input()
dep = [0]
for i in range(len(s)) :
    if s[i] == "d" :
        tmp = 1
    else :
        tmp = -1
    dep.append(dep[len(dep) - 1] + tmp)
u = build(dep, 0)
d1 = u.depth()
v = ToBinTree([u])
d2 = v.depth()
print(f"{d1} => {d2}")
