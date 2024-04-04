from collections import deque
people2grp = dict()
t = int(input())
for i in range(t) :
    s = list(map(int, input().split()))
    for u in s :
        people2grp[u] = i
q = []
for i in range(t) :
    q.append(deque([]))
qgrp = deque([])
isin = dict(zip(list(i for i in range(t)), [0] * t))
while True :
    s = input().split()
    if s[0] == "STOP" :
        break
    if s[0] == "DEQUEUE" :
        u = qgrp.popleft()
        isin[u] = 0
        print(q[u].popleft())
        if len(q[u]) > 0 :
            qgrp.appendleft(u)
            isin[u] = 1
    if s[0] == "ENQUEUE" :
        u = people2grp[int(s[1])]
        q[u].append(int(s[1]))
        if isin[u] == 0 :
            qgrp.append(u)
            isin[u] = 1

