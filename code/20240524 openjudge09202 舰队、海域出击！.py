T = int(input())
for case in range(T) :
    n, m = map(int, input().split())
    degree = [0]
    edge = [[]]
    for i in range(1, n + 1):
        edge.append([])
        degree.append(0)
    for i in range(m):
        u, v = map(int, input().split())
        edge[u].append(v)
        degree[v] += 1
    cnt = 0
    q = []
    for i in range(1, n + 1):
        if degree[i] == 0:
            q.append(i)
    while q:
        u = q[-1]
        cnt += 1
        q.pop()
        for v in edge[u]:
            degree[v] -= 1
            if degree[v] == 0:
                q.append(v)
    print("No" if cnt == n else "Yes")