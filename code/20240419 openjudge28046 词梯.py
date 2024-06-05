from itertools import product
from collections import deque

class Graph:
    def __init__(self) :
        self.vertices = dict()
    def addVertices(self, names) :
        for name in names :
            if name not in self.vertices :
                self.vertices[name] = []
    def addedge(self, u, v) : # directed edge
        self.vertices[u].append(v)
    def shortest_path(self, u, v, return_list = False) :
        vis = set()
        search_list = deque()
        search_list.append((u, 0))
        prev = dict()
        vis.add(u)
        while len(search_list) > 0 :
            w, x = search_list.popleft()
            for p in self.vertices[w] :
                if p == v :
                    res = x + 1
                    if return_list :
                        l = [v, w]
                        while l[-1] in prev :
                            l.append(prev[l[-1]])
                            #print(l)
                        l.reverse()
                        return res, l
                    else :
                        return res
                else :
                    if p not in vis :
                        prev[p] = w
                        vis.add(p)
                        search_list.append((p, x + 1))
        return -1

n = int(input())
d = dict()
G = Graph()
for i in range(n) :
    s = input()
    for i in range(len(s)) :
        s1 = s[0: i] + "*" + s[(i + 1):]
        if s1 not in d :
            d[s1] = [s]
        else :
            d[s1].append(s)
    G.addVertices([s])
for item in d :
    for i in d[item] :
        for j in d[item] :
            if i != j :
                G.addedge(i, j)
s1, s2 = input().split()
res = G.shortest_path(s1, s2, return_list=True)
if res == -1 :
    print("NO")
else :
    len, l = res
    print(" ".join(s for s in l))



                    
        
    