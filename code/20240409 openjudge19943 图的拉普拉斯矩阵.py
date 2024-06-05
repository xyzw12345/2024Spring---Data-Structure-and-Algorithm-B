n, m = map(int, input().split())
A = []
for i in range(n) :
    A.append([0] * n)
for i in range(m) :
    u, v = map(int, input().split())
    A[u][u] += 1
    A[u][v] -= 1
    A[v][u] -= 1
    A[v][v] += 1
for i in range(n) :
    print(" ".join(str(item) for item in A[i]))