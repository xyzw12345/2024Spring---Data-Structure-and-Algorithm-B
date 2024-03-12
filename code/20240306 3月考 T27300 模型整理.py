class info :
    def __init__ (self, name, sizenum, sizelevel) :
        self.name = name
        self.sizenum = sizenum
        self.sizelevel = sizelevel
    def __lt__(self, other) :
        return self.name < other.name or (self.name == other.name and self.sizelevel > other.sizelevel) or (self.name == other.name and self.sizelevel == other.sizelevel and float(self.sizenum) < float(other.sizenum))

n = int(input())
h = []
for i in range(n) :
    s = input().split("-")
    h.append(info(s[0], s[1][0 : len(s[1]) - 1], s[1][len(s[1]) - 1]))
h = sorted(h)
for i in range(len(h)) :
    if i == 0 or (i != 0 and h[i].name != h[i - 1].name) :
        print(f"{h[i].name}: {h[i].sizenum}{h[i].sizelevel}", end="")
    else :
        print(f", {h[i].sizenum}{h[i].sizelevel}",end="")
    if i < len(h) - 1 and h[i].name != h[i + 1].name :
        print("")

