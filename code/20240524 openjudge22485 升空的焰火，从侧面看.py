from collections import deque

n = int(input())
left = [0]
right = [0]
fa = [0] * (n + 1)
h = {}
for i in range(n):
    u, v = map(int, input().split())
    left.append(u)
    right.append(v)
    if u != -1:
        fa[u] = i + 1
    if v != -1:
        fa[v] = i + 1
root = 0
for i in range(n):
    if fa[i + 1] == 0:
        root = i + 1
q = deque()
q.append(root)
h[root] = 0
res = []
# print(left, right)
while q:
    u = q.popleft()
    # print(u, q, h)
    if left[u] != -1:
        q.append(left[u])
        h[left[u]] = h[u] + 1
    if right[u] != -1:
        q.append(right[u])
        h[right[u]] = h[u] + 1
    if not q:
        res.append(u)
        continue
    v = q.popleft()
    if h[v] > h[u]:
        res.append(u)
    q.appendleft(v)
print(" ".join(str(i) for i in res))
    