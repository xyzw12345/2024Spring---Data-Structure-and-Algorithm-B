class hotel :
    def __init__(self, dist, cost) :
        self.dist = dist
        self.cost = cost
    def __lt__(self, other) :
        return self.dist < other.dist or (self.dist == other.dist and self.cost < other.cost)

while True :
    N = int(input())
    h = []
    sum = [0] * 10001
    if N == 0 :
        break
    for i in range(N) :
        s = list(map(int, input().split()))
        h.append(hotel(s[0], s[1]))
    h = sorted(h)
    tmpMin = 1000000
    res = 0
    for i in range(N) :
        if h[i].cost < tmpMin :
            res += 1
        tmpMin = min(tmpMin, h[i].cost)
    print(res)
