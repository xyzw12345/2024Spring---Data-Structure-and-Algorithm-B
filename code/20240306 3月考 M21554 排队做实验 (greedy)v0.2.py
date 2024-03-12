class stu :
    def __init__(self, time, num) :
        self.time = time
        self.num = num
    def __lt__(self, other) :
        return self.time < other.time or (self.time == other.time and self.num < other.num)

n = int(input())
s = list(map(int, input().split()))
h = []
for i in range(n) :
    h.append(stu(s[i], i))
h = sorted(h)
print(" ".join(str(item.num + 1) for item in h))
sum = 0
for i in range(n) :
    sum += h[i].time * (n - 1 - i)
print(f"{sum / n :.2f}")