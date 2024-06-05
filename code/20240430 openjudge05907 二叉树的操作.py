t = int(input())
for Case in range(t) :
    n, m = map(int, input().split())
    son = []
    for i in range(n) :
        son.append([0, 0])
    parent = []
    for i in range(n) :
        parent.append([0, 0])
    for j in range(n) :
        i, u, v = map(int, input().split())
        son[i] = [u, v]
        parent[u] = [i, 0]
        parent[v] = [i, 1]
    for i in range(m) :
        s = input().split()
        if s[0] == "1" :
            u = int(s[1])
            v = int(s[2])
            fu, diru = parent[u]
            fv, dirv = parent[v]
            son[fu][diru] = v
            son[fv][dirv] = u
            parent[v] = [fu, diru]
            parent[u] = [fv, dirv]
        if s[0] == "2" :
            u = int(s[1])
            while son[u][0] != -1 :
                u = son[u][0]
            print(u)
    