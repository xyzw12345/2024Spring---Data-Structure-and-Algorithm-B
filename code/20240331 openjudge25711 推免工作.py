class stu :
    def __init__ (self, id, courses) :
        self.id = id
        self.courses = courses
        self.gpa = self.getgpa()
    def getgpa(self) :
        tot = 0
        res = 0
        for i in range((len(self.courses) // 2)) :
            x = 0
            u = float(self.courses[2 * i])
            v = float(self.courses[2 * i + 1])
            if u >= 60 :
                x = 4 - (3 / 1600) * (100 - u) * (100 - u)
            res += x * v
            tot += v
        return res / tot
    def __lt__(self, other) :
        return self.gpa > other.gpa

N, M = map(int, input().split())
q = []
for i in range(N) :
    u = input().split()
    q.append(stu(u[0], u[1 : len(u)]))
q = sorted(q)
print(' '.join(q[i].id for i in range(min(N, M))))