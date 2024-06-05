n = int(input())
s = list(map(int, input().split()))
q = []
res = []
for i in range(n - 1, -1, -1):
    while q and s[i] >= s[q[-1]]:
        q.pop()
    res.append(-1 if not q else q[-1])
    q.append(i)
res.reverse()
for i in res:
    print(i + 1, end=" ")