n = int(input())
d = dict()
dstr = dict()
def getstr(u) :
    global d
    global dstr
    if u in dstr :
        return dstr[u]
    dstr[u] = "\n".join((getstr(v) if v != u else str(u)) for v in d[u])
    return dstr[u]
for i in range(n) :
    s = list(map(int, input().split()))
    d[s[0]] = sorted(s)
dfather = dict(zip(list(item for item in d), list(item for item in d)))
for u in d :
    for v in d[u] :
        if v != u :
            dfather[v] = u
root = 0
for u in d :
    if dfather[u] == u :
        root = u
print(getstr(root))