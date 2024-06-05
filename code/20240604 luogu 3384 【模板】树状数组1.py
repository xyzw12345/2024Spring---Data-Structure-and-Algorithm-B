def lowbit (x) :
    return x & -x
class BIT:
    def __init__(self, n):
        self.sum = [0] * (n + 1) # the occupied index are 1 ~ n
    def add(self, m, x):
        tmp = m
        while tmp < len(self.sum):
            self.sum[tmp] += x
            tmp += lowbit(tmp)
    def getPrefixSum(self, m):
        res = 0
        tmp = m
        while tmp:
            res += self.sum[tmp]
            tmp = tmp - lowbit(tmp)
        return res

n, m = map(int, input().split())
l = list(map(int, input().split()))
B = BIT(n)
for i in range(1, n + 1):
    B.add(i, l[i - 1])
for i in range(m):
    op, x, y = map(int, input().split())
    if op == 1:
        B.add(x, y)
    else:
        print(B.getPrefixSum(y) - B.getPrefixSum(x - 1))