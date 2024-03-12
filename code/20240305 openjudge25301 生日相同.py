class stu :
    def __init__(self, num, mon, day, val) :
        self.num = num
        self.mon = mon
        self.day = day
        self.val = val
    def __lt__(self, other) :
        if self.mon < other.mon :
            return True
        else :
            if self.mon == other.mon and self.day < other.day :
                return True
            else :
                if self.mon == other.mon and self.day == other.day and self.val < other.val :
                    return True
                else :
                    return False

h = []
T = int(input())
for i in range(T) :
    s = input().split()
    h.append(stu(s[0], int(s[1]), int(s[2]), i))
h = sorted(h)
nowMonth = 0
nowDay = 0
for i in range(len(h)):
    item = h[i]
    if item.mon == nowMonth and item.day == nowDay :
        print(f" {item.num}", end = "")
    else :
        if i < len(h) - 1 and h[i + 1].mon == item.mon and h[i + 1].day == item.day :
            if nowMonth != 0 and nowDay != 0 :
                print()
            print(f"{item.mon} {item.day} {item.num}", end = "")
            nowMonth = item.mon
            nowDay = item.day