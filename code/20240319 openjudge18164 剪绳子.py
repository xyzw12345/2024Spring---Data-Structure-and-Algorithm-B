# Huffman Coding

from collections import deque

INF = 10**10
N = int(input())
l = list(map(int, input().split()))
l = sorted(l)
q1 = deque()
q2 = deque()
for item in l :
    q1.append(item)
res = 0
for i in range(N - 1) :
    min1 = INF
    min2 = INF
    tmp1 = INF
    tmp2 = INF
    if len(q1) > 0 :
        tmp1 = q1.popleft()
    if len(q2) > 0 :
        tmp2 = q2.popleft()
    if tmp1 < tmp2 :
        min1 = tmp1
        if tmp2 != INF :
            q2.appendleft(tmp2)
    else :
        min1 = tmp2
        if tmp1 != INF :
            q1.appendleft(tmp1)
    tmp1 = INF
    tmp2 = INF
    if len(q1) > 0 :
        tmp1 = q1.popleft()
    if len(q2) > 0 :
        tmp2 = q2.popleft()
    if tmp1 < tmp2 :
        min2 = tmp1
        if tmp2 != INF :
            q2.appendleft(tmp2)
    else :
        min2 = tmp2
        if tmp1 != INF :
            q1.appendleft(tmp1)
    q2.append(min1 + min2)
    res += min1 + min2
print(res)    
 