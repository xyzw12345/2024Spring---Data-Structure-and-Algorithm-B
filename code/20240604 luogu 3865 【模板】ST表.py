class STtable:
    def __init__ (self, s): # s[0 ~ n - 1] -> 1 ~ n
        n = len(s)
        self.logtable = [0]
        for i in range(1, n + 1):
            self.logtable.append(0)
            if (1 << (self.logtable[i - 1] + 1)) <= i:
                self.logtable[i] = self.logtable[i - 1] + 1
            else:
                self.logtable[i] = self.logtable[i - 1]
        self.table = []
        m = self.logtable[n]
        for j in range(m + 1):
            self.table.append([0])
        for i in range(n):
            self.table[0].append(s[i])
        for j in range(1, m + 1):
            for i in range(1, n - (1 << j) + 2):
                self.table[j].append(max(self.table[j - 1][i], self.table[j - 1][i + (1 << (j - 1))]))
    def query(self, l, r):
        u = self.logtable[r - l + 1]
        return max(self.table[u][l], self.table[u][r - (1 << u) + 1])

n, m = map(int, input().split())
s = list(map(int, input().split()))
T = STtable(s)
for i in range(m):
    u, v = map(int, input().split())
    print(T.query(u, v))