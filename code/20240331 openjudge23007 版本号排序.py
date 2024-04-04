def cmp(s1, s2) :
    if s1 == [] :
        return True
    if s2 == [] :
        return False
    if s1[0] < s2[0] :
        return True
    if s1[0] > s2[0] :
        return False
    return (cmp(s1[1 : len(s1)], s2[1 : len(s2)]))


class version :
    def __init__(self, s) :
        self.s = s
    def __lt__(self, other) :
        return cmp(list(map(int, self.s.split("."))), list(map(int, other.s.split("."))))

N = int(input())
q = []
for i in range(N) :
    q.append(version(input()))
q = sorted(q) 
for i in range(N) :
    print(q[i].s)