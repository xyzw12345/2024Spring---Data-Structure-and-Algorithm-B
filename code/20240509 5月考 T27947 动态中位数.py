import heapq as h

T = int(input())
for Case in range(T) :
    us = list(map(int, input().split()))
    q1 = [] # less than median
    q2 = [] # more than median
    h.heapify(q1)
    h.heapify(q2)
    siz1, siz2 = 0, 0
    res = []
    for u in us :
        if siz2 == 0 :
            h.heappush(q2, u)
            siz2 += 1
        else :
            v = h.heappop(q2)
            h.heappush(q2, v)
            if u >= v :
                h.heappush(q2, u)
                siz2 += 1
            else :
                h.heappush(q1, -u)
                siz1 += 1
        if siz1 > siz2 :
            u = -h.heappop(q1)
            siz1 -= 1
            h.heappush(q2, u)
            siz2 += 1
        if siz2 > siz1 + 1 :
            u = h.heappop(q2)
            siz2 -= 1
            h.heappush(q1, -u)
            siz1 += 1
        if siz2 == siz1 + 1 :
            u = h.heappop(q2)
            res.append(u)
            h.heappush(q2, u)
    print(len(res))
    print(" ".join(str(u) for u in res))    
