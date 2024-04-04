class stu :
    def __init__(self, name, days = []) :
        self.name = name
        self.days = days
    def valid(self) :
        u = sorted(self.days)
        if u[0] != 1 :
            return False
        if u[len(u) - 1] < 7 :
            return False
        for i in range(len(u) - 1) :
            if u[i + 1] - u[i] > 3 :
                return False
        return True


n = int(input())
m = int(input())
stuToSchool = dict()
stuTostu = dict()
stunames = []
school = []
for i in range(n) :
    u = input().split()
    stuToSchool[u[0]] = u[1]
    stuTostu[u[0]] = stu(u[0])
    if not u[0] in stunames :
        stunames.append(u[0])
    if not u[1] in school :
        school.append(u[1])
for i in range(m) :
    u = input().split()
    stuTostu[u[1]] = stu(u[1], stuTostu[u[1]].days + [int(u[0])])
schooltocnt = dict(zip(school, [0] * len(school)))
res = 0
mx = 0
pos = 0
for i in stunames :
    #print(i, stuTostu[i].days)
    if not stuTostu[i].valid() :
        res += 1
        schooltocnt[stuToSchool[i]] = schooltocnt[stuToSchool[i]] + 1
print(res)
for i in school :
    if schooltocnt[i] > mx :
        mx = schooltocnt[i]
        pos = i
print(i)


