class Candy :
    val = 0
    vol = 0
    def __init__(self, val, vol) :
        self.val = val
        self.vol = vol
    def __lt__(self, other) :
        return self.val * other.vol < self.vol * other.val

n, w = map(int, input().split())
listGift = []
res = 0
VOL = w
for i in range(n) :
    u, v = map(int, input().split())
    listGift.append(Candy(u, v))
listGift = sorted(listGift, reverse = True)
for candy in listGift :
    if candy.vol <= VOL :
        res += candy.val
        VOL -= candy.vol
    else :
        res += (candy.val / candy.vol) * VOL
        break
print(f"{res:.1f}")
