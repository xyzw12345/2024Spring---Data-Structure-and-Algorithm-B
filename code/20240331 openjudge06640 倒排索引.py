N = int(input())
q = []
q.append(set())
for i in range(N) :
    u = input().split()
    q.append(set(u[1 : len(u)]))
M = int(input())
for i in range(M) :
    u = input()
    res = []
    for j in range(1, N + 1) :
        if u in q[j] :
            res.append(j)
    if res == [] :
        print("NOT FOUND")
    else :
        print(" ".join(str(item) for item in res))