class Skill :
    def __init__(self, time, hit) :
        self.time = time
        self.hit = hit
    def __lt__(self, other) :
        return (self.time < other.time) or ((self.time == other.time) and (self.hit > other.hit))
    def __str__(self) :
        return "(" + str(self.time) + ", " + str(self.hit) + ")"

nCases = int(input())
listSkill = []
for Case in range(nCases) :
    n, m, b = map(int, input().split())
    listSkill = []
    for i in range(n) :
        u, v = map(int, input().split())
        listSkill.append(Skill(u, v))
    listSkill = sorted(listSkill)
    Time = 0
    cnt = 0
    hp = b
    for skill in listSkill :
        if skill.time != Time :
            Time = skill.time
            cnt = 1
            hp -= skill.hit
        else :
            if cnt < m :
                cnt += 1
                hp -= skill.hit
            else :
                continue
        if hp <= 0 :
            print(Time)
            break
    if hp > 0 :
        print("alive")
