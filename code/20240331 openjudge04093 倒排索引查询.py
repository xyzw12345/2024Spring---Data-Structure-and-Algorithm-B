N = int(input())
q = []
for i in range(N) :
    u = list(map(int, input().split()))
    q.append(set(u[1 : len(u)]))
M = int(input())
for i in range(M) :
    v = list(map(int, input().split()))
    res = set()
    flag = 0
    for j in range(N) :
        if v[j] == 1 :
            res = q[j]
    for j in range(N) :
        if v[j] == 1 :
            res = res.intersection(q[j])
        if v[j] == -1 :
            res = res.difference(q[j])
    w = list(res)
    w = sorted(w)
    if w == [] :
        print("NOT FOUND")
    else :
        print(" ".join(str(item) for item in w))