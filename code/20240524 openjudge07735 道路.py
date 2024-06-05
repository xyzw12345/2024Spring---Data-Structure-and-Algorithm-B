import heapq

K = int(input())
N = int(input())
M = int(input())
edge = [[]]
for i in range(N):
    edge.append([])
for i in range(M) :
    u, v, w, c = map(int, input().split())
    edge[u].append((v, w, c))
dist = {}
q = [(0, 1, 0)]
vis = set()
heapq.heapify(q)
while q:
    d, u, c = heapq.heappop(q)
    if (u, c) in vis:
        continue
    dist[(u, c)] = d
    vis.add((u, c))
    if u == N :
        break
    for e in edge[u]:
        v, w, c1 = e
        w2, c2 = d + w, c1 + c
        if c2 > K:
            continue
        if (v, c2) not in dist or dist[(v, c2)] > w2:
            heapq.heappush(q, (w2, v, c2))
res = -1
for i in dist:
    u = i[0]
    if u == N:
        res = dist[i] if res == -1 else min(res, dist[i])
print(res)





